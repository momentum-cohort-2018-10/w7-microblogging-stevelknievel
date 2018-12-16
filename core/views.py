from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.serializers import PostSerializer
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import Http404, JsonResponse
from django.template.defaultfilters import slugify
from django.shortcuts import render
from core.models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {
        'posts': posts,
    })


@api_view(['GET'])
def api_post_list(request):
    """List all things"""
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def api_post_detail(reqeust, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNoteExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)


def dataview(request, id):
    post = Post.objects.get(pk=id)
    data = serializers.serialize('json', [post])
    return JsonResponse(data, safe=False)


@login_required
def create_post(request):
    form_class = PostForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.slug = slugify(post.name)
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = form_class()

    return render(request, 'posts/create_post.html', {
        'form': form,
    })
    