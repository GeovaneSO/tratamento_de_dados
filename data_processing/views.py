from django.shortcuts import render
from .forms import UploadFileForm
from .utils import handle_uploaded_file, create_some, check_list
from .models import Process

def home(request):
    form = UploadFileForm()

    return render(request, "form.html", {"form": form})


def upload(request):
    form = UploadFileForm(request.POST, request.FILES)

    if form.is_valid():

        handle_uploaded_file(request.FILES)

        list = []
        for obj in Process.objects.all():
            objects_filtering = Process.objects.filter(store_name=obj.store_name) 

            is_contain = check_list(list, obj.store_name)

            if not is_contain:
                a = create_some(objects_filtering)
                list.append(dict(name=obj.store_name, value=a))

        return render(
            request, "success.html", {"list": list}
        )

    else:
        form = UploadFileForm()
    return render(
        request=request, template_name="form.html", content_type={"form": form}
    )
