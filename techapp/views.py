from django.views.generic import TemplateView, DetailView, FormView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
class HomePageView(LoginRequiredMixin, TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')
        return context
    
    
class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = Post


class AddPostView(FormView):
    template_name = 'addpost.html'
    form_class = PostForm
    success_url = '/home'
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        new_object = Post.objects.create(
            image = form.cleaned_data['image'],
            title = form.cleaned_data['title'],
            description = form.cleaned_data['description'],
        )
        # messages.add_message(self.request, messages.SUCCESS,f'Content successfully uploaded')
        messages.add_message(self.request, messages.SUCCESS, f' {form.cleaned_data["title"]} has been successfully uploaded!.')

        return super().form_valid(form)
    
class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'description', 'image']
    template_name = 'update.html'
    success_url = '/home'
    
    
class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'description', 'image']
    template_name = 'update.html'
    success_url = '/home'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, f'{self.object.title} has been successfully updated!.')
        return response

    
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = '/home'

class ContactPageView(TemplateView):

    template_name = "contact.html"
    
class LandingPageView(TemplateView):

    template_name = "index.html"
    
    
class AboutPageView(TemplateView):
    template_name = "about.html"
    
