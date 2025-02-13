# contacts/models.py
from django.db import models
from django.core.validators import RegexValidator

class Contact(models.Model):
    fullname = models.CharField(max_length=255)
    
    phone_regex = RegexValidator(
        regex=r'^\+998\s\(\d{2}\)\s\d{3}\s\d{2}\s\d{2}$',
        message="Номер телефона должен быть в формате: '+998 (XX) XXX XX XX'."
    )
    phone = models.CharField(validators=[phone_regex], max_length=20)
    
    text = models.TextField(help_text="Ваш текст")
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fullname
    
    
    class Meta: 
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']
