from django.db import models
from django.db.models.fields import CharField, TextField


class Title(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название тайтла')
    description = models.TextField(max_length=300, verbose_name='Описание', default="Нет описания")

    class Meta:
        verbose_name = 'Описание главной страницы'
        verbose_name_plural = 'Описания главной страницы'

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
    FIRST = 'твердотопливные'
    SECOND = 'газовые'
    THIRD = 'электрические'
    FOURTH = 'комбинированные'

    CHOICE_GROUP = [
        (FIRST, 'твердотопливные'),
        (SECOND, 'газовые'),
        (THIRD, 'электрические'),
        (FOURTH, 'комбинированные'),
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


from django.db import models

class UnifiedImage(models.Model):
    IMAGE_TYPE_CHOICES = [
        ('main_bg', 'Фон главной страницы'),
        ('upload', 'Просто изображение'),
        ('second_bg', 'Фон следующей страницы'),
    ]

    image = models.ImageField(upload_to='media/', verbose_name="Изображение")
    image_type = models.CharField(max_length=20, choices=IMAGE_TYPE_CHOICES, verbose_name="Тип изображения")

    class Meta:
        verbose_name = "Объединённое изображение"
        verbose_name_plural = "Объединённые изображения"

    def __str__(self):
        return f"{self.get_image_type_display()} ({self.id})"



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


class ContactMessage(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Сообщение от {self.name}"


class TelegramUser(models.Model):
    chat_id = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "telegram_users"
        verbose_name = "телеграм_бот"
        verbose_name_plural = "телеграм_боты"

    def __str__(self):
        return self.username

