from django.shortcuts import render, HttpResponse, Http404, HttpResponseRedirect
from django.views import View
from datetime import datetime
from .generator import get_all_data, set_data, get_searched_data
from .forms import PostText, Search


class MainPageView(View):
    def get(self, request):
        return HttpResponseRedirect('/news/')


class NewsPageView(View):
    def get(self, request):
        form = Search()
        if request.method == 'GET' and 'q' in request.GET:
            search = request.GET['q']
            news = get_searched_data(search)
            news = self.format(news)
        else:
            news = get_all_data()
            news = self.format(news)
        return render(request, 'news/index.html', {'news': news, 'form': form})

    def format(self, news):
        for post in news:
            date_format = datetime.strptime(post['created'], '%Y-%m-%d %H:%M:%S')
            post['created'] = datetime.strftime(date_format, '%Y-%m-%d')
        news.sort(key=lambda e: e['created'])
        news.reverse()
        return news


class PostView(View):
    def get(self, request, link):
        status = 'error'
        news = get_all_data()
        for post in news:
            if link == str(post['link']):
                status = 'ok'
                active_post = post
        if status != 'ok':
            raise Http404  # or return HttpResponse(status=404)
        posts_info = {
            'title': active_post['title'],
            'created': active_post['created'],
            'text': active_post['text']
        }
        return render(request, "news/posts.html", posts_info)


class PostCreateView(View):
    def get(self, request):
        form = PostText()
        return render(request, 'news/create.html', {'form': form})

    def post(self, request):
        error = ''
        # create a form instance and populate it with data from the request:
        form = PostText(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            set_data(form.cleaned_data['text'], form.cleaned_data['title'])
            # redirect to a new URL:
            return HttpResponseRedirect('/news/')
        return HttpResponseRedirect('/news/')


