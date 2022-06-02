from django.shortcuts import render, redirect

from .forms import BlogForm
from .models import Blog


def index(request):
    if request.method == "POST":
        form_data = BlogForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            blog = form_data.save(commit=False)
            blog.avtor.user = request.user
            blog.fajlovi = form_data.cleaned_data['fajlovi']
            blog.save()
            return redirect("blogs")
    queryset = Blog.objects.filter(avtor__user=request.user).all()
    context = {"blogs": queryset, "form": BlogForm}
    return render(request, "index.html", context=context)
