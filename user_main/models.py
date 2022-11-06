from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone

class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date_of_birth = models.DateTimeField(blank=True, null=True)
  district = models.CharField(max_length=255, blank=True, null=True)
  location = models.CharField(max_length=255, blank=True, null=True)
  skills = models.TextField(blank=True, null=True)
  about = models.TextField(blank=True, null=True)
  picture = models.ImageField(upload_to="profile", blank=True, null=True)

  def __str__(self) -> str:
    return self.user.username

  def get_age(self):
    return int((datetime.now(timezone.utc) - self.date_of_birth).days / 365.5)
  
  def get_skills(self):
    three_skills = self.skills.split(",")[0:3]
    return ','.join(three_skills)
