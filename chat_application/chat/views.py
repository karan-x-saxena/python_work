from django.http import HttpResponse , JsonResponse
from django.shortcuts import redirect, render
from .models import Permission, Space,Message, SpaceX, room
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'enter correct username or password!')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect ("login")

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken!")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email address already taken!')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                redirect('login')
        else:
            messages.info(request,'enter same password in both!')
            return redirect('signup')
    return render(request,'signup.html')

def index(request):
    if request.user.is_authenticated:
        spaces = SpaceX.objects.all()
        return render(request,'index.html',{'space':spaces})
    else: return redirect('login')

def space(request,space):
    username = request.GET.get('username')
    if request.user.is_authenticated and username == request.user.username:
        space_details = SpaceX.objects.get(name=space)
        permissions = Permission.objects.filter(user=username,space=space_details.id).first()
        if permissions.check_user == True or permissions.user == permissions.superuser:
            context = {
                'username':username,
                'space':space,
                'space_details':space_details
            }    
            return render(request,'space.html',context)
        else:
            messages.info(request,"you are not permited in the lobby!")
            return redirect('index')
    else: return redirect('login')

def checkspace(request):
    space = request.POST['room_name']
    username = request.POST['username']

    if SpaceX.objects.filter(name=space).exists():
        roomid = SpaceX.objects.get(name=space)
        if Permission.objects.filter(superuser=roomid.user,space=roomid.id,user=username).exists():
            pass
        else:
            Permission.objects.create(superuser=roomid.user,space=roomid.id,user=username).save()

    else:
        new_space = SpaceX.objects.create(name=space,user=username)
        new_space.save()
        Permission.objects.create(superuser=username,space=new_space.id,user="username").save()
    return redirect('/'+space+'/?username='+username)


def send(request):
    method = request.POST['message']
    space_id = request.POST['space_id']
    username = request.POST['username']

    new_message = Message.objects.create(value=method,user=username,room=space_id)
    new_message.save()
    return HttpResponse('message sent successfully!') 

def getMessages(request,space):
    space_details =  SpaceX.objects.get(name=space)

    messages = Message.objects.filter(room=space_details.id)
    return JsonResponse({'messages':list(messages.values())})
