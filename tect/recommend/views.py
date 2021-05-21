from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
from .models import Book_list, Recommended_list
import scripts.db as db
import scripts.delete as delete

# Create your views here.
def index(request):
	all_books = Book_list.objects.all()
	context = {'all_books':all_books}
	return render(request, 'recommend/index.html',context)

def details(request, book_id):
	book = Recommended_list.objects.get(idx=book_id)
	all_books = Book_list.objects.all()
	li = []
	li.append(all_books[book.rec1-1].name)
	li.append(all_books[book.rec2-1].name)
	li.append(all_books[book.rec3-1].name)
	li.append(all_books[book.rec4-1].name)
	li.append(all_books[book.rec5-1].name)
	
	context = {'book':book, 'li':li}
	return render(request, 'recommend/details.html', context)


def dbinstall(request):
	db.run()
	return redirect('index')



def dbdelete(request):
	delete.run()
	return redirect('index')
 
 