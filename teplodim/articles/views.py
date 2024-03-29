from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator

from .helper import send_async_mail, params_list
from .models import Article


class HomeView(View):
    template_name = 'articles_template.html'

    def get(self, request, *args, **kwargs):
        articles_list = Article.objects.all().order_by('-date_created')
        paginator = Paginator(articles_list, 3)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        return render(request, self.template_name, {'page_obj': page_obj})


class ContactView(View):
    template_name = 'contact_template.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'articles': Article.objects.all()})

    def post(self, request, *args, **kwargs):
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        parameters = {}
        for m in params_list:
            if request.POST.get(m):
                parameters[m] = request.POST.get(m)
        send_async_mail(subject, message, parameters)
        return render(request, self.template_name, {'sent': True})


class AboutView(View):
    template_name = 'about_template.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)


class ServicesView(View):
    template_name = 'services_template.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ContactsView(View):
    template_name = 'contacts_template.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ArticleDetailView(View):
    template_name = 'article_detail_template.html'

    def get(self, request, article_id, *args, **kwargs):
        article = get_object_or_404(Article, pk=article_id)
        images = [a.image for a in article.images.all()]
        images.insert(0, article.image)
        files = list(article.files.all())
        return render(request, self.template_name, {'article': article,
                                                    'images': images,
                                                    'files': files})
