from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', views.index, name='home_view'),
                  path('contacts/', views.contacts, name='contacts_view'),
                  path('skills/', views.skills, name='skills_view'),
                  path('portfolio/', views.portfolio, name='portfolio_view'),
                  path('email/', views.send_email, name='send_email_view'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
