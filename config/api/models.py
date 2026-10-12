from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255, unique=True)
    durations = models.SmallIntegerField(default=4)

    def __str__(self):
        return self.type




class Job(models.Model):
    name = models.CharField(max_length=255)
    introduction = models.CharField(max_length=255, null=True, blank=True)
    salary = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

User = get_user_model()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    text = models.TextField(verbose_name="Izoh matni")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Vaqti")

    def __str__(self):
        return f"{self.user.username}: {self.text[:20]}"