from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title


class Menu(models.Model):
    title = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
