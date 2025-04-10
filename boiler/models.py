from django.db import models
from django.db.models.fields import CharField, TextField


class Title(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название тайтла')
    description = models.TextField(max_length=300, verbose_name='Описание', default="Нет описания")

    class Meta:
        verbose_name = 'Тайтл'
        verbose_name_plural = 'Тайтлы'  # Добавлено

    def __str__(self):
        return self.title


class TitleSecondPage(models.Model):
    title_second = models.CharField(max_length=100, verbose_name='Название тайтла')
    description_second = models.TextField(max_length=300, verbose_name='Описание', default="Нет описания")

    class Meta:
        verbose_name = 'Наша услуга'
        verbose_name_plural = 'Наши услуги'  # Добавлено

    def __str__(self):
        return self.title_second


class Section(models.Model):
    # Поля для первого абзаца
    first_title = models.CharField(max_length=100, verbose_name='Название тайтла 1')
    first_description = models.TextField(max_length=300, verbose_name='Описание 1', default="Нет описания")

    # Поля для второго абзаца
    second_title = models.CharField(max_length=100, verbose_name='Название тайтла 2')
    second_description = models.TextField(max_length=300, verbose_name='Описание 2', default="Нет описания")

    # Поля для третьего абзаца
    third_title = models.CharField(max_length=100, verbose_name='Название тайтла 3')
    third_description = models.TextField(max_length=300, verbose_name='Описание 3', default="Нет описания")

    # Поля для четвертого абзаца
    fourth_title = models.CharField(max_length=100, verbose_name='Название тайтла 4')
    fourth_description = models.TextField(max_length=300, verbose_name='Описание 4', default="Нет описания")

    class Meta:
        verbose_name = 'Наша услуга главная страница'
        verbose_name_plural = 'Наши услуги главная страница'

    def __str__(self):
        return f"Секция с тайтлами: {self.first_title}, {self.second_title}, {self.third_title}, {self.fourth_title}"


class Product(models.Model):
    FIRST = '1 вид'
    SECOND = '2 вид'
    THIRD = '3 вид'
    FOURTH = '4 вид'

    CHOICE_GROUP = [
        (FIRST, '1 вид'),
        (SECOND, '2 вид'),
        (THIRD, '3 вид'),
        (FOURTH, '4 вид'),
    ]

    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена")
    availability = models.BooleanField(verbose_name="Наличие")
    group = models.CharField(max_length=50, choices=CHOICE_GROUP, default=FIRST, verbose_name="Категория")
    img = models.ImageField(default='no_image.png', upload_to='img/', verbose_name="Изображение")

    class Meta:
        verbose_name = 'Наш Котел'
        verbose_name_plural = 'Наши Котлы'


    def __str__(self):
        return self.name


from django.db import models

class Feature(models.Model):
    title1 = models.CharField(max_length=255, verbose_name="Заголовок 1 (h2)")
    description1 = models.TextField(verbose_name="Описание 1 (p)")

    title2 = models.CharField(max_length=255, verbose_name="Заголовок 2 (h3)")
    description2 = models.TextField(verbose_name="Описание 2 (p)")

    title3 = models.CharField(max_length=255, verbose_name="Заголовок 3 (h3)")
    description3 = models.TextField(verbose_name="Описание 3 (p)")

    title4 = models.CharField(max_length=255, verbose_name="Заголовок 4 (h3)")
    description4 = models.TextField(verbose_name="Описание 4 (p)")

    class Meta:
        verbose_name = "Наша услуга 2-я страница"
        verbose_name_plural = "Наши услуги 2-я страница"

    def __str__(self):
        return "Секция с заголовками"


class PageBackground(models.Model):
    image = models.ImageField(upload_to='backgrounds/', verbose_name="Фон страницы")

    class Meta:
        verbose_name = "Изображение для главной страницы сайта"
        verbose_name_plural = "Изображения для главной страницы сайта"

    def __str__(self):
        return f"Фон страницы {self.id}"


class ImageModel(models.Model):
    image = models.ImageField(upload_to='uploads/', verbose_name="Изображение")

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return self.image.name


class SecondImageModel(models.Model):
    second_image = models.ImageField(upload_to='backgrounds/', verbose_name="Изображение")

    class Meta:
        verbose_name = "Изображение для следующей страницы"
        verbose_name_plural = "Изображения для следующей страницы"

    def __str__(self):
        return self.second_image.name


class Client(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='client_logos/')
    website = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Наш клиент"
        verbose_name_plural = "Наши клиенты"

    def __str__(self):
        return self.name



class ContactForm(models.Model):
    contact = models.CharField(max_length=20, verbose_name='Контакты')
    hour = models.CharField(max_length=50, verbose_name='Время работы')
    email = models.EmailField(max_length=255, verbose_name='EMAIL')
    location = models.CharField(max_length=255, verbose_name='Локация', default="")

    class Meta:
        verbose_name = "Контактная форма"
        verbose_name_plural = "Контактные формы"

    def __str__(self):
        return self.contact


class Teammate(models.Model):
    teammate_image = models.ImageField(upload_to='media/')
    teammate_name = models.CharField(max_length=255)
    teammate_description = models.CharField(max_length=255)
    teammate_position = models.CharField(max_length=255, default="")

    class Meta:
        verbose_name = "Член команды"
        verbose_name_plural = "Члены команды"

    def __str__(self):
        return self.teammate_image.name


