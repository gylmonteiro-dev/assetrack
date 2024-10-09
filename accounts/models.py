from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='user')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Data de atualização")
    person_registration_number = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="CPF", default="SEM CADASTRO"
    )
    

    def __str__(self):
        return self.user.first_name or self.user.username