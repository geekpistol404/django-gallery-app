from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from numpy import array_split

from .forms import UserImageForm
from images.models import Image
from .helpers import image_grid


class UserListView(LoginRequiredMixin, ListView):

    model = User
    template_name = 'blocks/users.html'


def index(request):
    """Return a welcome block, redirects to feed block if authenticated"""
    if request.user.is_authenticated:
        return redirect('feed')
    return render(request, 'index.html', status=200)


def images(request):
    """Return public image grid if user is verified, otherwise redirect to welcome block"""
    images_list = Image.objects.order_by('-created')

    return image_grid(request, images_list)


@login_required
def upload(request):
    """Return image upload form"""
    if request.method == 'POST':
        form = UserImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.height, form.instance.width = get_image_dimensions(form.cleaned_data.get('image'))
            form.save()

            # Getting the current instance object to display in the template
            img_object = form.instance

            return render(request, 'blocks/upload.html', {'form': form, 'img_obj': img_object})
    else:
        form = UserImageForm()

    return render(request, 'blocks/upload.html', {'form': form})


@login_required
def delete(request, image_id):
    """Delete image by PK"""
    image = get_object_or_404(Image, pk=image_id)

    if request.method == 'POST':  # if method is POST
        image.delete()  # delete the image
        return redirect('feed')  # redirect to the feed

    return images(request)


@login_required
def profile(request, username):
    """Return profile block by user id"""
    profile_user = get_object_or_404(User, username=username)

    user_images = array_split(Image.objects.filter(author_id=profile_user.id).order_by('-created'), 3)

    return render(request, 'blocks/profile.html', {'profile': profile_user,
                                                   'images': user_images})
