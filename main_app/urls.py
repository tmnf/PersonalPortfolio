from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
                  path('', views.index, name='home_view'),
                  path('contacts/', views.contacts, name='contacts_view'),
                  path('skills/', views.skills, name='skills_view'),
                  path('downloads/', views.downloads, name='downloads_view'),
                  path('portfolio/', views.portfolio, name='portfolio_view'),
                  path('project/<str:title>', views.project, name='project_view'),
                  path('email/', views.send_email, name='send_email_view'),
                  path('lg/', views.change_lang, name='change_lang_view'),
                  path('temp/', views.server_temp, name='server_temp'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
