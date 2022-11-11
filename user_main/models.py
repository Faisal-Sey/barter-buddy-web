from django.db import models
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from datetime import datetime, timezone

class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date_of_birth = models.DateField(blank=True, null=True)
  district = models.CharField(max_length=255, blank=True, null=True)
  location = models.CharField(max_length=255, blank=True, null=True)
  skills = models.TextField(blank=True, null=True)
  about = models.TextField(blank=True, null=True)
  picture = models.ImageField(upload_to="profile", blank=True, null=True)

  def __str__(self) -> str:
    return self.user.username

  def get_age(self):
    return 21
    # return int((datetime.now(timezone.utc) - datetime(self.date_of_birth, )).days / 365.5)
  def get_skills(self):
    try:
        set_skill = self.skills.split(",")[0:3]
        three_skills = set_skill
        return ','.join(three_skills)
    except:
        return ""

  def get_skills_arr(self):
      try:
        return self.skills.split(",")
      except:
          return []

  def to_json(self):
    res = {"id": self.pk, **model_to_dict(self)}
    res["picture"] = self.picture.url if self.picture else ""
    res["age"] = self.get_age()
    res["fname"] = self.user.first_name
    res["lname"] = self.user.last_name
    res["email"] = self.user.email
    res["skills_arr"] = self.get_skills_arr()
    return res


class Connect(models.Model):
  user = models.ForeignKey(User, related_name='user_sending', on_delete=models.CASCADE)
  receiver = models.ForeignKey(User, related_name='user_receiving', on_delete=models.CASCADE)
  skill = models.CharField(max_length=50, blank=True, null=True)
  location = models.CharField(max_length=255, blank=True, null=True)
  date = models.CharField(max_length=50, blank=True, null=True)
  contact = models.CharField(max_length=50, blank=True, null=True)
  status = models.CharField(max_length=50, blank=True, null=True, default="pending")

  def __str__(self) -> str:
    return self.user.first_name + "-" + self.receiver.first_name

  def to_json(self):
    res = {"id": self.id, **model_to_dict(self)}
    res["profile"] = Profile.objects.get(user=self.receiver)
    return res

  def to_json_new(self):
    res = {"id": self.id, **model_to_dict(self)}
    return res


