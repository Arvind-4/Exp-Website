from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

# Create your views here.

from .models import Content, IpAddress


def get_client_ip(request: HttpRequest):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[-1].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def content_likes(request, slug):
    content = get_object_or_404(Content, slug=slug)
    if content.likes.filter(id=request.user.id).exists():
        content.likes.remove(request.user)
    else:
        content.likes.add(request.user)
    return HttpResponseRedirect(reverse("content-detail", args=[str(slug)]))


def index(request: HttpRequest):
    l = list(Content.objects.all())
    context = {"object_list": l}
    template = "content/home.html"
    return render(request, template, context)


def detail(request: HttpRequest, slug: str):
    liked = False
    l = get_object_or_404(Content, slug=slug)
    liked = l.likes.filter(email__iexact=request.user.email).exists()
    ip = get_client_ip(request)
    if IpAddress.objects.filter(ip=ip).exists():
        l.views.add(IpAddress.objects.get(ip=ip))
    else:
        IpAddress.objects.create(ip=ip)
        l.views.add(IpAddress.objects.get(ip=ip))
    context = {"object": l, "content_is_liked": liked}
    template = "content/detail.html"
    return render(request, template, context)
