from django.shortcuts import render, get_object_or_404
from .models import FarmerHome
# Create your views here.
def index(request):
    farmers = FarmerHome.objects.all()
    context = {
        "farmers": farmers
    }
    return render(request, 'index.html', context=context)
def farmersDetail(request, farmers):
    farmer = get_object_or_404(FarmerHome, slug=farmers)
    context = {
        'farmer': farmer
    }
    return render(request, 'farmersDetail.html', context=context)
def about(request):
    return render(request, 'about.html', context={})
def blog(request):
    return render(request, 'blog.html', context={})
def contact(request):
    return render(request, 'contact.html', context={})
def detail(request):
    return render(request, 'detail.html', context={})
def feature(request):
    return render(request, 'feature.html', context={})
def product(request):
    return render(request, 'product.html', context={})
def service(request):
    return render(request, 'service.html', context={})
def team(request):
    return render(request, 'team.html', context={})
def testimonial(request):
    return render(request, 'testimonial.html', context={})
