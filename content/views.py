from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction

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

@transaction.atomic
def index(request: HttpRequest):
    l_ = tuple(Content.objects.values('title', 'slug'))
    paginator = Paginator(l_, 10)
    page = request.GET.get('page', 1)
    try:
        l = paginator.page(page)
    except PageNotAnInteger:
        l = paginator.page(1)
    except EmptyPage:
        l = paginator.page(paginator.num_pages)
    context = {"object_list": l}
    template = "content/home.html"
    return render(request, template, context)


def detail(request: HttpRequest, slug: str):
    liked = False
    l = get_object_or_404(Content, slug=slug)
    try:
        liked = l.likes.filter(email__iexact=request.user.email).exists()
        ip = get_client_ip(request)
        obj = IpAddress.objects.filter(ip=ip)
        if obj.exists():
            l.views.add(obj)
        else:
            obj_new = IpAddress.objects.create(ip=ip)
            l.views.add(obj_new)
    except:
        pass
    context = {"object": l, "content_is_liked": liked}
    template = "content/detail.html"
    return render(request, template, context)
