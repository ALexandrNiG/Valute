from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=16, unique=True, verbose_name='Name' )
    description = models.TextField(blank=True, verbose_name='Desc')
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=32, unique=True)
    text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_img = models.ImageField(upload_to='blogapp', null=True, blank=True)

    def has_image(self):
        # print('my image:', self.image)
        # print('type', type(self.image))
        return bool(self.post_img)