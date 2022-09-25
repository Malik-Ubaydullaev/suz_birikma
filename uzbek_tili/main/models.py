from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Nomi', max_length=50)
    full_text = models.TextField('Soz birikma')
    date = models.DateTimeField('Kiritish sanasi')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Lug'at"
        verbose_name_plural = "Lug'atlar"
