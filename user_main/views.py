from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile

def home(request):
  return render(request, 'user_pages/home.html')

def dashboard(request, *args, **kwargs):
  user = request.user
  name = user.first_name + ' ' + user.last_name
  try:
    user_profile = Profile.objects.get(user=user)
    neighbours = Profile.objects.filter(district=user_profile.district).exclude(user=user)
    context = {
      "name_letters_excluding_the_first": name[1::],
      "neighbours": neighbours[0:4],
      "user": request.user
    }
  except BaseException as e:
    context = {}
  return render(request, 'user_pages/dashboard.html', context=context)


def find_buddies(request, *args, **kwargs):
  user = request.user
  name = user.first_name + ' ' + user.last_name
  try:
    user_profile = Profile.objects.get(user=user)
    neighbours = Profile.objects.filter(district=user_profile.district).exclude(user=user)
    context = {
      "name_letters_excluding_the_first": name[1::],
      "neighbours": neighbours,
      "user": request.user
    }
  except BaseException as e:
    context = {}
  return render(request, 'user_pages/find_buddies.html', context=context)