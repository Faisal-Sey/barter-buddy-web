from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.template import loader

from user_main.models import Profile

import json


def signin(request, *args, **kwargs):

  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
      user = authenticate(username=username, password=password)
      if user is not None:
        print("authenticated")
        login(request, user)
        return redirect('/dashboard')
      else:
        context = {"error": "Invalid credentials"}
        return render(request, "auth/login.html", context=context)
    except BaseException as e:
      return redirect('/login')

  return render(request, "auth/login.html")


def register(request, *args, **kwargs):
  if request.method == 'POST':
    fname = request.POST.get("fname")
    lname = request.POST.get("lname")
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    c_password = request.POST.get("c_password")

    if c_password == password:
      user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=fname,
        last_name=lname
      )

      user.save()
      user_profile = Profile(user=user)
      user_profile.save()
      login(request, user)
      return redirect("/dashboard")
  return render(request, 'auth/register.html', context={})


def forgotten_password(request, *args, **kwargs):
  if request.method == 'POST':
    email = request.POST.get("email")
    try:
      message = "Hello <br> Please click the link below to reset password <br>"
      message += f"<a href='https://barterbuddy.pythonanywhere.com/auth/verify_email/{email}'>Reset Password</a>"
      check_user = User.objects.get(email=email)
      if check_user is not None:
        send_mail(
          subject="Reset Password",
          message="h",
          html_message= message,
          from_email=settings.EMAIL_HOST_USER,
          recipient_list = [email],
        )
    except Exception as e:
      print(e)
  return render(request, 'auth/forgotten_password.html', context={})

def reset_password(request, *args, **kwargs):
  return render(request, "auth/reset_password.html", context={})

def signout(request, *args, **kwargs):
  logout(request)
  return redirect("/auth/login")


def verify_email(request, email):
  if request.method == 'POST':
    password = request.POST.get("password")
    c_new_password = request.POST.get("c_password")
    print(password, c_new_password)
    if password == c_new_password:
      user = User.objects.get(email=email)
      user.set_password(password)
      user.save()
      return redirect("/auth/login")
  if email is not None:
    template = loader.get_template('auth/reset_password.html')
    context = {
      'email': email,
    }
    user = User.objects.get(email=email)
    login(request, user)
    return HttpResponse(template.render(context, request))
    #return render(request, "reset_password", {'useremail':email})

  else:
    return redirect("login")

def logout_user(request, *args, **kwargs):
    logout(request)
    return redirect("/login")


def reset_password(request, email):
  # if request.method == 'POST':
  #   print("Yes")
  if email is not None:
      return redirect("/auth/reset_password.html")

  else:
    return redirect("register")
