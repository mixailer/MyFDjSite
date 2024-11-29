from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book
from .forms import ClientForm

def home(request):
    return HttpResponse('''<h1>Привет!</h1>
<p>Добро пожаловать на главную страницу.</p>''')

def employee_info(request, employee_id):
    return HttpResponse(f"Здесь будет полезная информация для сотрудника {employee_id}.")

def book_detail(request, bool_id):
    book = Book.objects.get(id='book_is')
    return render(request, 'book_detail.html', {'book': book})

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление на главную страницу после успешного создания клиента
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})