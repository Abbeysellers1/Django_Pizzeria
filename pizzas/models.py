from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)
    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    pizza=models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name= models.TextField()

    def __str__(self):
        return self.topping_name

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True,blank=True)
    

    class Meta:
        ordering=['date_added']

    def __str__(self):
        return 'Comment {} by {}'.format(self.text, self.name)