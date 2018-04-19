from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from . import models
from Group import views
from django.shortcuts import get_object_or_404
from Group.models import Group,GroupMember
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,ListView,DetailView,RedirectView,DeleteView

class CreateGroup(CreateView):
    model = models.Group
    fields = ('name','description',)
    success_url = reverse_lazy('Group:all')

class AllGroups(ListView):
    model = models.Group

class GroupDelete(DeleteView):
    model = models.Group
    success_url = reverse_lazy('Group:all')

class GroupDetail(DetailView):
    model = models.Group

class JoinGroup(LoginRequiredMixin,RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse("Group:group_detail",kwargs={'pk': self.kwargs.get('pk')})
    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Group,pk=self.kwargs.get('pk'))
        try:
            GroupMember.objects.create(user=self.request.user,group=group)
        except:
            messages.warning(self.request,'Waring!')
        else:
            messages.success(self.request,'yes now!')
        return super().get(request, *args, **kwargs)

class LeaveGroup(LoginRequiredMixin,RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse("Group:group_detail",kwargs={'pk': self.kwargs.get('pk')})
    def get(self,request,*args,**kwargs):
        try:
            membership = models.GroupMember.objects.filter(user=self.request.user,group__pk=self.kwargs.get("pk")
            ).get()
        except:
            messages.warning(self.request,"warning")
        else:
            membership.delete()
            messages.success(self.request,"success")
        return super().get(request,*args,**kwargs)
