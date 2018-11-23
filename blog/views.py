from django.shortcuts import render
from .models import Illust

def post_list(req):
    posts = Illust.objects.all()
    return render(req, 'post_list.html', {'posts':posts})

# Create your views here.