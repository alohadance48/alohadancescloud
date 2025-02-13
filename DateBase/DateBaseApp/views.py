from django.shortcuts import render
from django.http import HttpResponseForbidden,HttpResponse,HttpResponseBadRequest
from DateBaseApp.forms import LoginForm,FileInstall,FilesDispatch,RegisterForm,AdminForm

# Create your views here.
def login(request):
    login_form = {'login_form': LoginForm()}
    return render(request, 'DateBaseApp/login.html',context=login_form)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
        else :
            return HttpResponseBadRequest('<h1>Ошибка при регистрации </h1>')
    else :
        form = RegisterForm()
        date = {'form': form}
        return render(request, 'DateBaseApp/Registr.html',context=date)


def file_install(request):
    file_install_form = FileInstall()
    date = {'files': file_install_form}
    return render(request, 'DateBaseApp/FileInstall.html',context=date)

def file_dispatch(request):
    if request.method == 'POST':
        file_dispatch =  FilesDispatch(request.POST, request.FILES)
        if file_dispatch.is_valid():
            return HttpResponse('<h1>Файл отправлен</h1>')
        else :
            return HttpResponseBadRequest(request,'Errors/ErrorForm.html')
    else:
        files = FilesDispatch()
        date = {'form': files}
        return render(request, 'DateBaseApp/FileDispatch.html',context=date)

def admin_form(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            comment = form.cleaned_data.get('comment')
            password = form.cleaned_data.get('password')
        else :
            return HttpResponseForbidden(request,'Errors/ErrorDelete.html')
    else:
        form = AdminForm()
        date = {'form': form}
        return render(request, 'DateBaseApp/admin.html',context=date)

