from django.db import models
from django.urls import reverse

class Category(models.Model):
    """Категории, к которым относятся товары"""
    name = models.CharField(max_length=150, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=150, unique=True)
    is_published = models.BooleanField(verbose_name='Опубликован', default=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Площадки'
        verbose_name_plural = 'Площадки'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('shop:product_list_by_category', args=[self.slug])


class SubCategory(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание подкатегории', blank=True)
    created_at = models.DateTimeField(verbose_name='Время создания подкатегории', auto_now_add=True)
    category = models.ForeignKey(Category, verbose_name='Вид', on_delete=models.CASCADE, null=True) 

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Форма Баннеров'
        verbose_name_plural = 'Формы баннеров'
        db_table = 'subcategories'
        ordering = ['-created_at']


class Product(models.Model):
    """Модель описания продукта"""
    # category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,verbose_name='Выберите категорию')
    subcategory = models.ForeignKey(SubCategory, verbose_name='Подкатегория', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наменование')
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Фото')
    description = models.TextField(blank=True, verbose_name='Описание')
    # price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True, verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Вид'
        verbose_name_plural = 'Виды рекламных баннеров'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('shop:product_detail', args=[self.id, self.slug])