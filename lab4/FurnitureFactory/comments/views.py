from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from .models import Comment
from .forms import RatingForm
from login.models import ClientUser
from django.http import HttpResponseRedirect, HttpResponseNotFound
# Create your views here.


def comments(request):
    reviews = Comment.objects.all()
    context = {'comments': reviews}
    return render(request, 'comments/comments.html', context)


def add_comment(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("You do not have access to this page.")

    form = RatingForm(request.POST)

    if request.method == 'POST':
        comment = Comment.objects.create(client=ClientUser.objects.filter(email=request.user.email).first(),
                                         content=request.POST.get('text'), rating=request.POST.get('range'))
        comment.save()

        return HttpResponseRedirect("/comments/")
    else:
        return render(request, "comments/create_comment.html", {"form": form})

