from django.shortcuts import render
from basic_app.forms import signUp
from basic_app.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "basic_app/index.html")

def new_user(request):
    form = signUp()
    user_list = User.objects.all()

    if request.method == "POST":
        form = signUp(request.POST)

        if form.is_valid():
            if User.objects(email=form.cleaned_data['email']).count() == 0:
                user = User(first_name=form.cleaned_data['first_name'],
                            last_name=form.cleaned_data['last_name'],
                            email=form.cleaned_data['email'])
                user.save(commit=True)
                messages.success(request, 'USER RESGISTERED!')
            else:
                messages.warning(request, 'EMAIL ALREADY EXIST!')
            user_list = User.objects.all()
            return render(request, "basic_app/user.html", {'form':form, 'user_list':user_list})
        else:
            messages.error(request, '')

    return render(request, "basic_app/user.html", {'form':form, 'user_list':user_list})
