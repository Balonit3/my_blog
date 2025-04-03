from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='Название категории')
    def __str__(self):
        return self.name
    class Meta():
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Post(models.Model):
    title =models.CharField(max_length=200,verbose_name='Заголовок поста')
    content =models.TextField(verbose_name='Текст поста')
    date =models.DateTimeField(verbose_name='Дата создания',auto_now_add=True)
    category =models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Категория')
    def __str__(self):
        return self.title
    class Meta():
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-date']




# Create your models here.
