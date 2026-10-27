from django.shortcuts import render
from .models import Todo
from .forms import TodoForm
from django.shortcuts import get_object_or_404, redirect

def post_list(request):
    posts = Todo.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Todo, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = TodoForm()
    return render(request, 'post_create.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = TodoForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'post_delete.html', {'post': post})