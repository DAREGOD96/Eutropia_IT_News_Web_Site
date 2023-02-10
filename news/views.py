from django.shortcuts import render,redirect
from django.views import View
from .models import News
from django.contrib import messages
import os

# Create your views here.

class Homepage(View):
    def get(self, request):

        all_news = News.objects.all()
        context = {
            'news' : all_news,
        }
        return render(request, 'home.html' , context)

class NewsDetail(View):
    def get(self, request, pk):
        news_details = News.objects.get(id=pk)
        return render(request, 'news_details.html', {'news': news_details})

class DeleteNews(View):
    def get(self,request, pk):
        delete_news= News.objects.get(id=pk)
        delete_news.delete()
        return redirect('home')
         
def PublishNews(request):
    if request.method == "POST":
        title = request.POST.get('news_title')
        description = request.POST.get('news_description')
        if len(request.FILES) !=0:
            image = request.FILES['news_image']
        news = News(news_title=title, news_image = image, news_description=description)
        news.save()
        messages.success(request, "News Added Successfully.")
        return redirect('home')
    return render(request, 'publish_news.html')

def UpdateNews(request, pk):

    news = News.objects.get(pk = pk)
    context = {
        'news': news,
    }

    if request.method == "POST":
        news.news_title = request.POST.get('news_title')
        if len(request.FILES) != 0:
            if len(news.news_image) > 0:
                os.remove(news.news_image.path)
            news.news_image = request.FILES['news_image']
        news.news_description = request.POST.get('news_description')
        news.save()
        messages.success(request, "News Updated Succeessfully ")
        return redirect('home')

    return render(request, 'update_news.html', context)

# class UpdateNews(View):
#     def get(self,request,pk):


#         update_news=News.objects.get(id=pk)
#         context ={
#             'update_news':update_news,
#         }
        # if request.method == "POST":
        #     title = request.POST.get('news_title')
        #     description = request.POST.get('news_description')
        #     if len(request.FILES) !=0:
        #         image = request.FILES['news_image']
            
        #     news = News(news_title=title, news_image = image, news_description=description)
        #     news.save()
        #     messages.success(request, "News Updated Successfully.")
        #     return redirect('home')
#         return render(request, 'update_news.html', context)
       

# def UpdateNews(request, pk):
#     news = News.objects.get(pk=pk)

#     if request.method == "POST":
#         title = request.POST.get('news_title')
#         description = request.POST.get('news_description')
#         if len(request.FILES) !=0:
#             image = request.FILES['news_image']
            
#         news = News(news_title=title, news_image = image, news_description=description)
#         news.save()
#         messages.success(request, "News Updated Successfully.")
#         return redirect('home')

#     return render(request, 'update_news.html', {'news': news})