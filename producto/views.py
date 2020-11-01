from django.shortcuts import render, redirect
from .forms import ProductForm
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(['GET', 'POST'])
def get_name(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('producto.index')
    else:
        form = ProductForm()
    
    return render(request, 'producto/views/name.html', {
        'form' : form
    })
