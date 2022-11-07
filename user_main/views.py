from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from .models import Profile, Connect
from datetime import datetime
from .forms import ImageForm


import json, os

def home(request):
  return render(request, 'user_pages/home.html')

def dashboard(request, *args, **kwargs):
  user = request.user
  name = user.first_name + ' ' + user.last_name
  try:
    user_profile = Profile.objects.get(user=user)
    neighbours = Profile.objects.filter(district=user_profile.district).exclude(user=user)
    connections = Connect.objects.filter(user=user)
    skills_shared = Connect.objects.filter(receiver=user)
    context = {
      "name_letters_excluding_the_first": name[1::],
      "neighbours": neighbours[0:4],
      "connections": len(connections),
      "skills_shared": len(skills_shared),
      "friends_near_your": len(neighbours),
      "user": request.user,
      "user_profile": user_profile
    }
    print(context)
  except BaseException as e:
    print(e)
    context = {}
  return render(request, 'user_pages/dashboard.html', context=context)


def find_buddies(request, *args, **kwargs):
  if request.method == "GET":
    user = request.user
    name = user.first_name + ' ' + user.last_name
    try:
      user_profile = Profile.objects.get(user=user)
      neighbours = Profile.objects.filter(district=user_profile.district).exclude(user=user)
      connects = Connect.objects.filter(user=user)
      context = {
        "name_letters_excluding_the_first": name[1::],
        "neighbours": neighbours,
        "user": request.user,
        "user_profile": user_profile,
        "connects": connects,
      }
    except BaseException as e:
      context = {}
    return render(request, 'user_pages/find_buddies.html', context=context)

  if request.method == 'POST':
    data = request.POST
    try:
      connection = Connect(
        user=User.objects.get(id=data.get("user_id")),
        receiver=User.objects.get(id=data.get("receiver_id")),
        skill=data.get("skill"),
        location = data.get("location"),
        contact = data.get("phone"),
        date=data.get("date")
      )
      connection.save()
      user = request.user
      name = user.first_name + ' ' + user.last_name
    
      user_profile = Profile.objects.get(user=user)
      neighbours = Profile.objects.filter(district=user_profile.district).exclude(user=user)
      context = {
        "name_letters_excluding_the_first": name[1::],
        "neighbours": neighbours,
        "user": request.user
      }
      return render(request, 'user_pages/find_buddies.html', context=context)

    except BaseException as e:
      print(e)
    return render(request, 'user_pages/find_buddies.html', context={})


@csrf_exempt
def get_profile(request, *args, **kwargs):
  data = json.loads(request.body)
  id = data.get("id")
  if id is not None:
    profile = Profile.objects.get(id=id)
    print(profile.to_json())
    return JsonResponse({ "profile": profile.to_json() })
  
  else:
    return JsonResponse({ "profile": {} })

@csrf_exempt
def create_connection(request, *args, **kwargs):
  data = json.loads(request.body)
  
  try:
    first_option = Connect.objects.get(user=data.get("user_id")) & Connect.objects.get(receiver=data.get("receiver_id"))
    second_option = Connect.objects.get(receiver=data.get("user_id")) & Connect.objects.get(user=data.get("receiver_id"))

    if first_option or second_option:
      return JsonResponse({ "response": "Already connected" })
    else:
      connection = Connect(
        user=User.objects.get(user=data.get("user_id")),
        receiver=User.objects.get(user=data.get("receiver_id")),
        skill=data.get("skill"),
        location = data.get("location"),
        contact = data.get("contact"),
        date=datetime.now()
      )
      connection.save()
      return JsonResponse({ "response": "Connected Successfully" })
  
  except BaseException as e:
    return JsonResponse({ "response": "An error occured" })


def account_settings(request, *args, **kwargs):
  if request.method == 'POST':
    user = request.user
    if 'account' in request.POST:
      first_name = request.POST.get("first_name")
      last_name = request.POST.get("last_name")
      email = request.POST.get("email")
      username = request.POST.get("username")
      user = User.objects.get(email=user.email)
      user.first_name = first_name
      user.last_name = last_name
      user.email = email
      user.username = username
      user.save()
      return redirect("account_settings")
    if 'password' in request.POST:
      old_password = request.POST.get("old_password")
      new_password = request.POST.get("new_password")
      confirm_password = request.POST.get("confirm_password")
      check_password = authenticate(username=user.username, password=old_password)
      if check_password:
        if new_password == confirm_password:
          if old_password == new_password:
            print("New Password cannot be same as old password")
          else:
            user = User.objects.get(username=user.username)
            user.set_password(new_password)
            user.save()
        else:
          print("Passwords do not match")
      else:
        print("Wrong User Password")
      return redirect("login")
    if 'profile' in request.POST:
      about = request.POST.get("about")
      location = request.POST.get("location")
      district = request.POST.get("district")
      skills = request.POST.get("skills")
      date_of_birth = request.POST.get("dob")
      user_profile = Profile.objects.get(user=user)
      user_profile.about = about
      user_profile.location = location
      user_profile.district = district
      user_profile.skills = skills
      user_profile.date_of_birth = date_of_birth
      user_profile.save()
      return redirect("account_settings")
    if 'picture' in request.POST:
      old_image = Profile.objects.get(user=user)
      print(old_image.picture)
      form = ImageForm(request.POST, request.FILES, instance=old_image)
      if form.is_valid():
        image_path = old_image.picture.path
        if os.path.exists(image_path):
          os.remove(image_path)
        form.save()
        return redirect("account_settings")
  user = request.user
  name = user.first_name + ' ' + user.last_name
  try:
    user_profile = Profile.objects.get(user=user)
    neighbours = Profile.objects.filter(district=user_profile.district).exclude(user=user)
    context = {
      "name_letters_excluding_the_first": name[1::],
      "neighbours": neighbours,
      "user": request.user,
      "user_profile": user_profile
    }
  except BaseException as e:
    context = {}
  return render(request, 'user_pages/account_settings.html', context=context)
