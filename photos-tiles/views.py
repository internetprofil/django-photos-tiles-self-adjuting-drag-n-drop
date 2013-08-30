from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404

from .models import Story, PhotosStory

__author__ = 'wojtek'


def story_list(request):
    #pobac z modeli elementy
    listOfWeddings = Story.objects.all()
    context={'entries': listOfWeddings}
    return TemplateResponse(request, 'weddings.html', context=context)

def story_detail(request, slug):
    #pobrac z modeli element na podstawie sluga
    entry = get_object_or_404(Story, slug=slug)

    photos = PhotosStory.objects.filter(story=entry, published=True)

    context={'entry': entry, 'listOfPhotos': photos}

    return TemplateResponse(request, 'weddingInside.html', context=context)


