from django.shortcuts import render
from .models import Item
from .forms import ItemForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpRequest, HttpResponse
# Create your views here.


def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'item_list.html', context)


@login_required
@permission_required('market.add_item', raise_exception=True)
def add_item(request):
    if request.method =='POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('item-list')
    form = ItemForm()
    return render(request, 'new_item.html', {'form': form})
