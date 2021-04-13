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
    path('cadastra-cliente/',views.registerClient,name='cadastra-cliente'),   
    path('cadastra-fornecedor/',views.registerSupplier,name='cadastra-fornecedor'),   
    path('login/',views.login,name='login'),
    path('product-page/<str:product_pk>/',views.productPage,name='product-page'),
    path('search/',views.search,name='search'),
    path('search/<str:filter>',views.search,name='search-filter'),

    # Profile #
    path('profile/1',views.profileData1,name='profileData1'),
    path('profile/2',views.profileData2,name='profileData2'),
    path('carrinho/',views.carrinho,name='carrinho'),
    path('finaliza/',views.finaliza,name='finaliza'),
    path('history/',views.history,name='history'),

    # Fornecedor #
    
    # Paginas especiais #
    path('logout/',views.logout,name='logout'),
    path('delete/<str:delete_type>/<str:delete_pk>/', views.delete, name='delete'),
    path('edit/<str:edit_pk>/', views.edit, name='edit'),
    path('admin/', admin.site.urls),
    path('terms-of-use', views.document,{"type_model":"TERMOS DE USO"}),
    path('privacy-policy', views.document,{"type_model":"POLÍTICA DE PRIVACIDADE"}),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
]