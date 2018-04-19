from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from . import models
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
# Create your views here.
from django.views.generic import CreateView,ListView,DetailView,DeleteView,RedirectView
from Post.forms import PostForm
from braces.views import SelectRelatedMixin
from django.contrib import messages
from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()


class CreatePost(CreateView):
    model = models.Post
    form_class=forms.PostForm
    success_url = reverse_lazy('Group:all')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)



class PostList(SelectRelatedMixin,ListView):
    model = models.Post

    select_related = ("user", "group")
    template_name = "Post/post_list.html"

class PostDetail(SelectRelatedMixin,DetailView):
    model = models.Post
    select_related = ("user","group")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )


class PostDelete(DeleteView):
    model = models.Post
    select_related = ("user", "group")
    success_url = reverse_lazy('Group:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)
