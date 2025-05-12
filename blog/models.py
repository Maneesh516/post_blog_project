from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Category
class Category(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.ImageField(null=True, upload_to="posts/images",blank=True )
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)  # Allow blank slugs initially
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Prevent overwriting existing slugs
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def formatted_img_url(self):
        if self.img_url:
            try:
                return self.img_url.url
            except:
                pass
        return "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
    

    def __str__(self):
        return self.title

class AboutUs(models.Model):
    content = models.TextField()
