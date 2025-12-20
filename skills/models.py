from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Yetenek Adı")
    level = models.IntegerField(default=50, verbose_name="Seviye (0-100)")
    category = models.CharField(max_length=50, verbose_name="Kategori")
    icon = models.ImageField(upload_to='skills/', blank=True, verbose_name='İkon')
    order = models.IntegerField(default=0, verbose_name="Sıralama")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")

    class Meta: 
        ordering = ['order', 'name']
        verbose_name = "Yetenek"
        verbose_name_plural = "Yetenekler"

    def __str__(self):
        return self.name