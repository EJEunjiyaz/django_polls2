from django.db import models

class Item(models.Model):
    item_text = models.CharField()

class Choice(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    pub_date = models.DateField('date published')
    price = models.IntegerField(default=0)
    sells = models.IntegerField(default=0)

