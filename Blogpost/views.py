from django.shortcuts import render
from .models import Blogpost, Video
from django.http import HttpResponse
from taggit.models import Tag
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import BlogpostForm, VideoForm, CommentForm, contactForm
from django.conf import settings
from django.core.mail import message, send_mail

def post_list(request):
    queryset = Blogpost.objects.order_by('-publish')[:3]
    context={
        'object_list': queryset,
    }
    return render(request, 'blog.html', context)
    

from django.utils import timezone
from django.views.generic.detail import DetailView



class postDetailView(DetailView):

    model = Blogpost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def post_by_tag(request):
    queryset = Blogpost.objects.filter('tags')
    context = {'object_list': queryset

}
    return render(request,                  
                        'post_by_tags.html',                  
                                context     )
    
def comment(request):
    form = CommentForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'comment.html', {'form' :form})

def contact_us(request):
    
    form = contactForm(request.POST)
    if form.is_valid():
        #send mail code .
        sender_name = form.cleaned_data['name']
        sender_email = form.cleaned_data['email']
        message = "{0}has sent a new message:\n\n{1}"
        format =(sender_name, form.cleaned_data ['message'])
        send_mail ('New enquiry', message, sender_email, ['samuelokwu85@gmail.com'])
        return HttpResponse('Thanks for Contacting Us!')
    else:
        form = contactForm()
        return render (request, 'contact.html', {'form':form})




# video display


def showvideo(request):
    
    video= Video.objects.all()

    #videofile= lastvideo.videofile


    my_form= VideoForm(request.POST or None, request.FILES or None)
    if my_form.is_valid():
        my_form.save()

    
    context= {#'lastvideo': lastvideo,
            'object_list': video,
              'form': my_form
              }
    
      
    return render(request, 'video.html', context)
