from django.shortcuts import render,redirect
from .models import Assets
# Create your views here.

def list_asset(request):
    assets = Assets.objects.all()
    context ={
        'assets':assets
    }
    return render(request, 'core/base.html',context)

def add_assets(request):
    if request.method == 'POST':
        asset_name = request.POST.get('asset_name')
        asset_type = request.POST.get('asset_type')
        asset_quantity = request.POST.get('asset_quantity')

        assets = Assets(
            asset_name=asset_name,
            asset_type = asset_type,
            asset_quantity = asset_quantity
        )
        assets.save()
        return redirect('home')

    return render(request, 'core/base.html')


def edit_asset(request):
    assets = Assets.objects.all()

    context = {
        'assets':assets
    }
    return render(request, 'core/base.html', context)


def update_asset(request,id):
    
    if request.method == 'POST':
        asset_name = request.POST.get('asset_name')
        asset_type = request.POST.get('asset_type')
        asset_quantity = request.POST.get('asset_quantity')

        assets = Assets(
            id = id,
            asset_name=asset_name,
            asset_type = asset_type,
            asset_quantity = asset_quantity
        )
        assets.save()
        return redirect('home')


def delete_asset(request,id):
    assets = Assets.objects.filter(id=id)
    assets.delete()
    return redirect('home')
    
