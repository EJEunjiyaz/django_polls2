from django.db import models

class Item(models.Model):
    item_text = models.CharField(max_length=100)

    def __str__(self):
        return self.item_text

class Choice(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    pub_date = models.DateField('Date published')
    price = models.IntegerField(default=0)
    sells = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def compute(self):
        return self.price*self.sells