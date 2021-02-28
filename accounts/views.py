from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.conf import settings
from .forms import UserCreationForm
from .models import Image, Log
from .serializers import ImageSerializer, LogSerializer
from .email import send_notification

from rest_framework import viewsets


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'


def home(request):
    images = Image.objects.filter(user=request.user).order_by('-created_at') if request.user.is_authenticated else ''
    return render(request, 'accounts/home.html', {'images': images})


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


def fetch(request):
    if request.method == 'GET':
        images = Image.objects.filter(user=request.user).order_by('-created_at')
        output = ''
        for id, image in enumerate(images):
            output += '<tr>'
            output += '<td>' + str(id + 1) + '</td>'
            output += '<td>' + '<div class="image" style="background:url(' + image.image.url + '); background-size: 150px;"></div>' + '</td>'
            output += '<td>' + '<span>To see image, click on: </span><a href="' + image.image.url + '">' + image.image.url + '</a><br><br><a href="' + 'http://127.0.0.1:8000/images/' + str(
                image.id) + '" class="btn-sm btn-info">SEE IMAGE</a>' + '</td>'
            output += '<td>' + str(image.created_at) + '</td>'
            output += '</tr>'
        return JsonResponse(output, safe=False)


def image(request, pk):
    if request.method == 'GET':
        try:
            image = Image.objects.get(id=pk)
            logs = Log.objects.filter(image_id=pk)
            host = settings.HOST
            return render(request, 'accounts/image.html', {'image': image, 'logs': logs, 'host': host})
        except Exception as e:
            raise e
    else:
        return HttpResponse(status=404)


class LogViewSet(viewsets.ModelViewSet):
    serializer_class = LogSerializer
    queryset = Log.objects.all()


def delete_image(request):
    if request.method == 'POST':
        image_id = request.POST['image_id_delete']
        Image.objects.get(id=image_id).delete()
        return redirect('home')
    else:
        return HttpResponse(status=404)


def send_email(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.POST['login'])
        login = user.username
        email = user.email
        created_at = request.POST['created_at']
        location = request.POST['location']
        body = login + ';' + str(created_at) + ';' + location + ';'
        # print(body)

        send_notification(str(email), body)
        return JsonResponse({'status': 'SENT!'}, safe=False)
    else:
        return HttpResponse(status=404)
