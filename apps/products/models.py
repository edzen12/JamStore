from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название категории")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='категория'
        verbose_name_plural='Категории'


class Jam(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, 
        related_name='products', verbose_name="Категория"
    )
    title = models.CharField(max_length=200, verbose_name="Название продукта")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(default=0, verbose_name="Кол-во товара вообще")
    desc = models.TextField(verbose_name="Описание продукта")
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_main_image(self):
        return self.images.filter(is_main=True).first()
    
    def get_second_image(self):
        return self.images.filter(is_main=False).first()

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'Продукты'


class ImgJam(models.Model):
    jam = models.ForeignKey(
        Jam, on_delete=models.CASCADE, verbose_name="Продукт", related_name='images'
    )
    img = models.ImageField(upload_to='jam/', verbose_name="Фото")
    is_main = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'фотография'
        verbose_name_plural = 'Фотографии'