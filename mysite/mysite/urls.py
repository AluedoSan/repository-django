from django.contrib import admin
from django.urls import include, path
from polls.views import redirect_polls  # Usando a importação absoluta

urlpatterns = [
    path('', redirect_polls),  # Redireciona a página inicial para /polls/
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
