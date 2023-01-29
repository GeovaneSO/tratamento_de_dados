from django.shortcuts import render
from .forms import UploadFileForm
from .utils import handle_uploaded_file, create_some, check_list, get_operations
from .models import Process
from collections import Counter


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
                operations = get_operations(obj.store_name, objects_filtering)

                some_value = create_some(objects_filtering)
                Counter(operations).elements
                list.append(
                    dict(name=obj.store_name, operations=operations, value=some_value)
                )

        return render(request, "success.html", {"list": list})

    else:
        form = UploadFileForm()
    return render(
        request=request, template_name="form.html", content_type={"form": form}
    )
