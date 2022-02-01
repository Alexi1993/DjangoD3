from django.db import models
from django.shortcuts import reverse


# Создаём модель
class New(models.Model):
    title = models.CharField(max_length=64, null=True, blank=True)
    text = models.TextField(max_length=356, null=True, blank=True)
    date_of_pub = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    slug = models.SlugField(max_length=128, unique=True, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
        ordering = ['-date_of_pub']