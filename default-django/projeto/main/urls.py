from django.contrib import admin
from django.urls import path
from main import views
from django.template.response import TemplateResponse
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static' : StaticViewSitemap,
}

urlpatterns = [
    # Todos #
    path('',views.index,name='home'),
    path('cadastra_cliente/',views.cadastraCliente,name='cadastra_cliente'),   
    path('cadastra_fornecedor/',views.cadastraFornecedor,name='cadastra_fornecedor'),   
    path('login/',views.login,name='login'),

    # Cliente #
    path('profile/',views.profileData,name='profileData'),
    path('logout/',views.logout,name='logout'),

    # Fornecedor #
    
    # Paginas especiais #
    path('admin/', admin.site.urls),
    path('terms-of-use', views.document,{"type_model":"TERMOS DE USO"}),
    path('privacy-policy', views.document,{"type_model":"POLÍTICA DE PRIVACIDADE"}),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
]