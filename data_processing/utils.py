from datetime import datetime
from .serializers import ProcessSerializer


def create_datetime(str_date: str, str_time: str) -> dict:
    date_formate = f"{str_date[:9][:4]}-{str_date[:9][4:6]}-{str_date[:9][6:]}"
    time_formate = f"{str_time[:2]}:{str_time[2:4]}:{str_time[4:]}"

    return dict(
        date=datetime.strptime(date_formate, "%Y-%m-%d").date(),
        time=datetime.strptime(time_formate, "%H:%M:%S").time(),
    )

def handle_uploaded_file(file):

    for line in file["file"].readlines():

        line_value = line.decode("utf-8")
        date_time_values = create_datetime(line_value[1:9], line_value[42:48])
        value = int(line_value[10:19]) / 100
        transaction = int(line_value[0])

        if transaction == 2 or transaction==3 or transaction==9:
            value*=-1

        information = dict(
            transaction_type=transaction,
            transaction_date=date_time_values["date"],
            transaction_value=value,
            cpf=line_value[19:30],
            card=line_value[30:42],
            transaction_hour=date_time_values["time"],
            store_owner=line_value[48:62],
            store_name=line_value[62:81],
        )
        serializer = ProcessSerializer(data=information)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
def check_list(list, name):
    counter = 0
    for elem in list:
        
        if name==elem['name']:
            counter += 1
    if counter == 0:
        return False    

    return True


def create_some(list):
    value = 0
    for elem in list:
        value+=elem.transaction_value
    return value
