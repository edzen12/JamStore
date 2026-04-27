from django.db import models


class Jam(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название продукта")
    desc = models.TextField(verbose_name="Описание продукта")

    def __str__(self):
        return self.title
    
    def get_main_image(self):
        return self.images.filter(is_main=True).first()
    
    def get_second_image(self):
        return self.images.filter(is_main=False).first()

    class Meta:
        verbose_name = 'варенье'
        verbose_name_plural = 'Варенья'


class ImgJam(models.Model):
    jam = models.ForeignKey(
        Jam, on_delete=models.CASCADE, verbose_name="Продукт", related_name='images'
    )
    img = models.ImageField(upload_to='jam/', verbose_name="Фото")
    is_main = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'фотография'
        verbose_name_plural = 'Фотографии'