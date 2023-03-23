from django.core.management.base import BaseCommand
from blogapp.models import Category, Post

class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = Category.object.all()
        post = Post.objects.first()
        category = post.category
        Category.object.create(name="Новая", description='Что-то')
        category = Category.object.get(name='Новая')
        category.name = "Измененная"
        category.save()
        category.delete()
        categories = Category.object.all()




