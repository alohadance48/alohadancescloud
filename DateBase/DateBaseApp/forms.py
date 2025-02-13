from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username:', max_length=20,min_length=5)
    email = forms.EmailField(label='Email:',max_length=30,min_length=10)
    password = forms.CharField(widget=forms.PasswordInput(),label="Password:",max_length=30,min_length=10)

class FilesDispatch(forms.Form):
    file = forms.FileField(label='Select a file:')

class FileInstall(forms.Form):
    file = forms.FilePathField(label='Select a file for installation:',path='/home/vladosl/',allow_files=True,allow_folders=True)

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username:', max_length=20,min_length=5)
    email = forms.EmailField(label='Email:',max_length=20,min_length=10,)
    password = forms.CharField(widget=forms.PasswordInput(),label="Password:",max_length=30,min_length=10)

class AdminForm(forms.Form):
    delete_user = forms.ChoiceField(label='Delete user',choices=[('delete','Delete user')])
    password = forms.CharField(widget=forms.PasswordInput(),label="Password:",max_length=30,min_length=10)
    comment = forms.CharField(widget=forms.Textarea(),label="Comment:",max_length=1000,min_length=5)


