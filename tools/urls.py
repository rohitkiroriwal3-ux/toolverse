from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tools/<slug:slug>/', views.tool_detail, name='tool_detail'),
    path('word-counter/', views.word_counter, name='word_counter'),
    path('password-generator/', views.password_generator, name='password_generator'),
    path('qr-generator/', views.qr_generator, name='qr_generator'),
    path('image-to-pdf/', views.image_to_pdf, name='image_to_pdf'),
    path('pdf-merge/', views.pdf_merge, name='pdf_merge'),
    path('text-case/', views.text_case_converter, name='text_case'),
    path('random-number/', views.random_number, name='random_number'),
    path('image-compressor/', views.image_compressor, name='image_compressor'),
    path('image-resizer/', views.image_resizer, name='image_resizer'),
    path('jpg-to-png/', views.jpg_to_png, name='jpg_to_png'),
    path('png-to-jpg/', views.png_to_jpg, name='png_to_jpg'),
    path('remove-spaces/', views.remove_spaces, name='remove_spaces'),
    path('text-reverser/', views.text_reverser, name='text_reverser'),
    path('tool/<slug:slug>/online/',views.tool_landing,name='tool_landing'),
    path('about/', views.about, name='about'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms, name='terms'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path("create-admin/", views.create_admin),
    path('sitemap-page/', views.sitemap_page, name='sitemap_page'),
    
]   
