from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy 
from django.forms import ModelForm

# views.py
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer

class PostForm (ModelForm):
    class Meta:
        model = Post
        fields = ['title']

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    
class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    
class BlogCreateView(CreateView): 
    model = Post
    # form_class = PostForm
    template_name = "post_new.html"
    fields = ["title", "author", "body"]
    
class BlogUpdateView(UpdateView): 
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]

class BlogDeleteView(DeleteView): 
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
    
    
