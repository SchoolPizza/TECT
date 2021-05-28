from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
from .models import Book_list, Recommended_list
import script.db as db
import script.delete as delete
from django.views.generic import FormView
from .forms import SearchForm
from django.db.models import Q
from .paginator import my_paginator


# Create your views here.
def index(request):
	all_book = Book_list.objects.all()
	page = request.GET.get('page', 1)
	all_books, page_range = my_paginator(all_book, page, num=20, page_num_range=10)
	
	context = {'all_books' : all_books,'page_range':page_range}
	return render(request, 'recommend/index.html', context)


def details(request, book_id):
	book = Recommended_list.objects.get(idx=book_id)
	all_books = Book_list.objects.all()
	li = []
	li.append(all_books[book.rec1-1])
	li.append(all_books[book.rec2-1])
	li.append(all_books[book.rec3-1])
	li.append(all_books[book.rec4-1])
	li.append(all_books[book.rec5-1])
	print(type(book.idx.genre))
	print(book.idx.genre)

	context = {'book':book, 'li':li}
	return render(request, 'recommend/details.html', context)


def dbinstall(request):
	db.run()
	return redirect('index')



def dbdelete(request):
	delete.run()
	return redirect('index')


# FormView
class SearchFormView(FormView):
	form_class = SearchForm
	template_name = 'recommend/search.html'
	
	# FormView : POST요청에서 데이터 유효성 검사 자동으로 실행
	def form_valid(self, form):
		# form 유효성 검증에 통과한 값을 dictonary 타입으로 저장 
		searchWord = form.cleaned_data['search_word']
		# Q 객체 사용, 검색 -> 대소문자 구분 없이 해당 단어가 포함되었는지 검사
		# distinct() : 중복 제거
		book_list = Book_list.objects.filter(Q(name__icontains=searchWord)).distinct()

		# 검색 결과 context 변수에 저장 
		context = {}
		context['form'] = form
		context['search_term'] = searchWord
		context['object_list'] = book_list

		return render(self.request, self.template_name, context)