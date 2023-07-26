from django.db import models

# Create your models here.
class Item(models.Model):

    # explicitly defining the string representation of this model
    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=1000, default="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.everestkitchenpa.com%2Fassets%2Fpages%2FfriedRice.html&psig=AOvVaw3bo40h87K4yQFhxXHtj6UJ&ust=1690480342652000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCMCwnJX4rIADFQAAAAAdAAAAABAD")