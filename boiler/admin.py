from django.contrib import admin
from .models import Title, TitleSecondPage, Section, Feature, Product, PageBackground, ImageModel, SecondImageModel, Client, ContactForm, Teammate

from .models import Title, TitleSecondPage, Section, Feature, Product, PageBackground, ImageModel, SecondImageModel, \
    Client, ContactForm, ContactMessage, TelegramUser


# Register your models here.
admin.site.register(Title)
admin.site.register(TitleSecondPage)
admin.site.register(Section)
admin.site.register(Product)
admin.site.register(Feature)
admin.site.register(PageBackground)
admin.site.register(ImageModel)
admin.site.register(SecondImageModel)
admin.site.register(Client)
admin.site.register(ContactForm)
admin.site.register(ContactMessage)
admin.site.register(TelegramUser)


admin.site.register(Teammate)

