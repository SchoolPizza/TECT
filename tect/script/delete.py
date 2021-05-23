from recommend.models import Book_list, Recommended_list


def run():
	q = Book_list.objects.all()
	p = Recommended_list.objects.all()
	q.delete()
	p.delete()