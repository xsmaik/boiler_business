from django.contrib import admin
from .models import Title, TitleSecondPage, Section, Feature, Product, Client, ContactForm, Teammate

from .models import Title, TitleSecondPage, Section, Feature, Product, Client, ContactForm, ContactMessage, TelegramUser, UnifiedImage


# Register your models here.
admin.site.register(Title)
admin.site.register(TitleSecondPage)
admin.site.register(Section)
admin.site.register(Product)
admin.site.register(Feature)
admin.site.register(UnifiedImage)
admin.site.register(Client)
admin.site.register(ContactForm)
admin.site.register(ContactMessage)
admin.site.register(TelegramUser)

admin.site.register(Teammate)

