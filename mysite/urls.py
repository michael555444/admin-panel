from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import RedirectView
from django.urls import path, include

from mysite.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('admin/', views.secret_page, name='secret'),
    # path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))
    # path('admin/', admin.site.urls),
    # path('hello/', request_page)
]
