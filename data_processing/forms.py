from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    cpf = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)


class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=50)
    password = forms.CharField(max_length=50)
