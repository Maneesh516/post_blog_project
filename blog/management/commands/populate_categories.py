from django.core.management.base import BaseCommand
from blog.models import Category
from django.utils.text import slugify

class Command(BaseCommand):
    help = "This command inserts Category data"

    def handle(self, *args, **options):
      
        Category.objects.all().delete()

        categories=[
            'sports',
            'Technology',
            'Science',
            'Art',
            'Food'
        ]

        for category_name in categories:
            Category.objects.create(name=category_name)

        self.stdout.write(self.style.SUCCESS("✅ Data Insertion Completed!"))
