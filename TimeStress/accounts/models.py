from django.db import models
from django.conf import settings

USER_TYPE_CHOICES = (
    ('user', 'User'),
    ('admin', 'Admin'),
)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='user')

    def __str__(self):
        return f'Profile for user {self.user.username}'
