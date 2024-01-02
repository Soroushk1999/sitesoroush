from django.db import models


class MemberModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=250)
    created = models.TimeField(auto_now_add=True)

