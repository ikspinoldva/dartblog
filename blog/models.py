from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=255, verbose_name='Slug Category', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']



class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    slug = models.SlugField(max_length=50, verbose_name='Slug Tag', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=255, verbose_name='Slug Post', unique=True)
    author = models.CharField(max_length=100, verbose_name='Author')
    content = models.TextField(blank=True, verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Published')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True, verbose_name='Photo')
    views = models.IntegerField(default=0, verbose_name='Views')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts', verbose_name='Category')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name='Tags')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']