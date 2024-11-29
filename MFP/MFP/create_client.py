from django.shortcuts import render, redirect
from .forms import ClientForm

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление на главную страницу после успешного создания клиента
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})