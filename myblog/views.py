from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from myblog.models import Article, Category
import markdown
from comments.forms import CommentForm
from .forms import MDEditorModleForm
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify

def editor(request):
	form = MDEditorModleForm
	return render(request, 'editor.html', {'form':form})

class HomepageView(ListView):
	model = Article
	template_name = 'index.html'
	context_object_name = 'articles'

class CategoryView(HomepageView):
	def get_queryset(self):
		cate = get_object_or_404(Category, id=self.kwargs.get('id'))
		return super(CategoryView, self).get_queryset().filter(category=cate)

class ArchivesView(HomepageView):
	def get_queryset(self):
		return super(ArchivesView, self).get_queryset().filter(created_time__year=self.kwargs.get('year'), created_time__month=self.kwargs.get('month'))	
	
def postdetail(request,post_id):
	article = get_object_or_404(Article,id = post_id)
	article.increase_numread()
	article.body = markdown.markdown(article.body,extensions = ['markdown.extensions.extra','markdown.extensions.codehilite','markdown.extensions.toc'])
	form = CommentForm()
	comment_list = article.comment_set.all()
	context = {'article': article,
				'form': form,
				'comment_list': comment_list
	}
	return render(request, 'single.html', context=context)	
def postdetail_(request,post_id):
	article = get_object_or_404(Article,id = post_id)
	article.body = markdown.markdown(article.body,extensions=['markdown.extensions.codehilite','markdown.extensions.extra','markdown.extensions.toc'])#,extension = ['markdown.extensions.extra','markdown.extensions.codehilite','markdown.extensions.toc']
	
	return render(request, 'text.html', {'article':article})

class PostDetailView(DetailView):
	model = Article
	template_name = 'single.html'
	context_object_name = 'article'
	
	def get(self, request, *args, **kwargs):
		response = super(PostDetailView, self).get(request, *args, **kwargs)
		self.object.increase_numread()
		return response

	def get_object(self, queryset=None):
		post = super(PostDetailView, self).get_object(queryset=None)
		md = markdown.Markdown(extensions=[
			'markdown.extensions.extra',
			'markdown.extensions.codehilite',
			TocExtension(slugify=slugify),
		])
		post.body = md.convert(post.body)
		post.toc = md.toc
		return post
	
	def get_context_data(self, **kwargs):
		context = super(PostDetailView, self).get_context_data(**kwargs)
		form = CommentForm()
		comment_list = self.object.comment_set.all()
		context.update({
			'form': form,
			'comment_list': comment_list
		})
		return context
	