from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # เชื่อมโยงกับ User
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # ตัวอย่างข้อมูลเพิ่มเติม
    address = models.TextField(blank=True, null=True)  # ตัวอย่างข้อมูลเพิ่มเติม

    def __str__(self):
        return self.user.username
