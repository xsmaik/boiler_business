from django.shortcuts import render
from .models import Title, TitleSecondPage, Feature, Product, Section, PageBackground, ImageModel, SecondImageModel


# Create your views here.
def index(request):
    title = Title.objects.all()
    text_description = Title.objects.values_list('description', flat=True)

    title_second = TitleSecondPage.objects.all()
    description_second = TitleSecondPage.objects.values_list('description_second', flat=True)

    sections = Section.objects.all()

    product = Product.objects.all()

    feature = Feature.objects.first()

    background = PageBackground.objects.last()

    images = ImageModel.objects.all()

    second_images = SecondImageModel.objects.all()

    context = {
        'title': title,
        'description': text_description,

        'title_second': title_second,
        'description_second': description_second,

        'sections': sections,

        'product': product,

        'feature': feature,

        'background': background,

        'images': images,

        'second_images': second_images,
    }

    return render(request, 'boiler/index.html', context)
