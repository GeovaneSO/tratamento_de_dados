from django.shortcuts import render
from .forms import UploadFileForm
from .utils import handle_uploaded_file
from .models import FormModel
from django.views.generic import CreateView
from django.urls import reverse_lazy
import ipdb
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.views import APIView, Request, Response, status
import os

def home(request):
    # ipdb.set_trace()
    return render(request, "form.html")


def upload(request):
    form = UploadFileForm(request.POST, request.FILES)
    # ipdb.set_trace()
    
    if form.is_valid():
        # o = request.path
        # ipdb.set_trace()
    
        handle_uploaded_file(request.FILES)
    else:
        form = UploadFileForm()
    return render(
        request=request, template_name="form.html", content_type={"form": form}
    )
