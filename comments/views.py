from django.shortcuts import render, get_object_or_404, redirect
from myblog.models import Article
from .models import Comment
from .forms import CommentForm
from django.urls import reverse
from django.http import HttpResponse


def post_comment(request, post_pk):
	post = get_object_or_404(Article, pk=post_pk)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			print(1)
			return redirect(post)
		else:
			comment_list = post.comment_set.all()
			context = {'article': post,
						'form': form,
						'comment_list': comment_list
			}
			print(2)
			return render(request, 'single.html', context=context)
	print(3)
	return redirect(post)
def hello(request):
	return HttpResponse("hello")