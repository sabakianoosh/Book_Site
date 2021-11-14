from django.db import models
from django.db.models.deletion import CASCADE

class category(models.Model):
   
    category_name=models.CharField(max_length=50,null=True)
    

    def __str__(self):
        return f"ID: {self.category_name}"
   
class Book(models.Model):
    title = models.CharField(max_length=100,null=True)
    cover_image = models.ImageField(upload_to = 'img', blank = True , null = True)
    genre = models.CharField(max_length=128,null=True)
    author=models.CharField(max_length=128,null=True)
    summary=models.TextField(max_length=1000,null=True)
    category = models.ForeignKey(category,related_name="book_categories",on_delete=CASCADE,null=True)

    def __str__(self):
        return f"ID:  {self.title} , {self.cover_image} ,{self.author},{self.summary},{self.genre}"

