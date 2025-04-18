from django.shortcuts import render
from .models import (
    Title, TitleSecondPage, Feature, Product, Section,
    Client, ContactForm, Teammate, TelegramUser, UnifiedImage
)
from django.http import JsonResponse

def index(request):
    title = Title.objects.all()
    text_description = Title.objects.values_list('description', flat=True)

    title_second = TitleSecondPage.objects.all()
    description_second = TitleSecondPage.objects.values_list('description_second', flat=True)

    sections = Section.objects.all()
    product = Product.objects.all()
    feature = Feature.objects.first()
    clients = Client.objects.all()
    contacts = ContactForm.objects.first()
    teammates = Teammate.objects.all()

    # ⚙️ Новые изображения
    main_bg = UnifiedImage.objects.filter(image_type='main_bg').first()
    upload_img = UnifiedImage.objects.filter(image_type='upload').first()
    second_bg = UnifiedImage.objects.filter(image_type='second_bg').first()

    context = {
        'title': title,
        'description': text_description,

        'title_second': title_second,
        'description_second': description_second,

        'sections': sections,
        'product': product,
        'feature': feature,

        # 🖼 Новые ключи вместо background / images / second_images
        'main_bg': main_bg,
        'upload_img': upload_img,
        'second_bg': second_bg,

        'clients': clients,
        'contacts': contacts,
        'teammates': teammates,
    }

    return render(request, 'index.html', context)

def chat_ids_api(request):
    chat_ids = list(TelegramUser.objects.values_list('chat_id', flat=True))
    return JsonResponse(chat_ids, safe=False)
