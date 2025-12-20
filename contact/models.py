from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="İsim")
    email = models.EmailField(verbose_name="E-posta")
    subject = models.CharField(max_length=200, verbose_name="Konu")
    message = models.TextField(verbose_name="Mesaj")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Gönderilme Tarihi")
    is_read = models.BooleanField(default=False, verbose_name="Okunudu mu?")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "İletişim Mesajı"
        verbose_name_plural = "İletişim Mesajları"

    def __str__(self):
        return f"{self.name} - {self.subject}"

