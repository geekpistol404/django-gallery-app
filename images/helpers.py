from django.shortcuts import render
from numpy import array_split


def image_grid(request, images_list):
    """ Return three lists of images, one for each column """
    images_list = array_split(images_list, 3)

    return render(request, 'blocks/feed.html', {'images': images_list})


def get_model_fields(custom_model):
    return custom_model.meta.fields
