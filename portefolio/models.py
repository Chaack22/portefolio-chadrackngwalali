from django.db import models
from django.core.validators import EmailValidator, RegexValidator

# Create your models here.

phone_ = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Le numero de telephone doit etre au format : +999999"
)

class Message(models.Model):
    nom = models.CharField(max_length=100)
    post_nom = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator(message="Adresse invalide.")])
    telephone = models.CharField(validators=[phone_],max_length=17)
    message = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} {self.post_nom}"

