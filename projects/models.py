from django.db import models
from skills.models import Skill

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Proje Adı")
    description = models.TextField(verbose_name="Açıklama")
    image = models.ImageField(upload_to='projects/', blank=True, verbose_name='Görsel')
    url = models.URLField(blank=True, verbose_name="Proje Linki")
    github_url = models.URLField(blank=True, verbose_name="GitHub Linki")
    skills = models.ManyToManyField(Skill, verbose_name="Kullanılan Teknolojiler")
    order = models.IntegerField(default=0, verbose_name="Sıralama")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Proje"
        verbose_name_plural = "Projeler"
    
    def __str__(self):
        return self.title