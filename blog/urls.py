from django.urls import path
from .views import about, blog, contact, detail, feature, \
    index, product, service, team, testimonial, farmersDetail

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('farmer/<slug:farmers>', farmersDetail, name="farmersDetail"),
    path('contact/', contact, name='contact'),
    path('detail/', detail, name='detail'),
    path('feature/', feature, name='feature'),
    path('product/', product, name='product'),
    path('service/', service, name='service'),
    path('team/', team, name='team'),
    path('testimonial/', testimonial, name='testimonial'),
]