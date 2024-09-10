from django.core.exceptions import ValidationError
from django.db import models

class Product(models.Model):
    name = models.CharField(
        max_length=255, 
        blank=False, 
        null=False, 
        verbose_name='название'
    )
    description = models.TextField(
        verbose_name='описание'
    )
    price = models.PositiveIntegerField(
        default=0,
        verbose_name='цена'
    )


    def clean(self):
        if len(self.description) < 20:
            raise ValidationError('Описание должно быть больше 20 символов!')
        if self.price <= 0:
            raise ValidationError('Цена должна быть больше 0')


    def save(self, *args, **kwargs):
        self.clean()  # Применяем валидацию перед сохранением
        super().save(*args, **kwargs)
