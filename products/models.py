from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя категории', unique=True)
    description = models.TextField(max_length=1000, verbose_name='Описание категории')
    slug = models.SlugField(max_length=70, unique=True, verbose_name='URL-имя')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name',] #сортировка

    
    def __str__(self) -> str:
        return self.name
    
    def get_url(self):
        return reverse('category_detail', args=[self.slug])
    


class SubCategory(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя подкатегории')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ['name',]



class Products(models.Manager):
    name = models.CharField(max_length=128, unique=True, verbose_name='Имя продукта')
    description = models.TextField(max_length=1000, verbose_name='Описание продукта')
    price = models.FloatField(verbose_name='Цена продукта')
    slug = models.SlugField(max_length=148, unique=True, verbose_name='URL-имя')
    is_available = models.BooleanField(default=True, verbose_name='Доступность товара')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория')


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name', '-price']


    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
    
    def __str__(self):
        return self.name