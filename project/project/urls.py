"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp.views import AgentViewRetrieveUpdate,AgentViewCreate, AgentViewDestroy



app_name = 'mainapp'
urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/agent/<int:pk>', AgentViewRetrieveUpdate.as_view(), name='test'),
    path('api/agent', AgentViewRetrieveUpdate.as_view(), name='test'),
    path('api/test', AgentViewCreate.as_view(), name='test'),
    path('api/test/<int:pk>', AgentViewDestroy.as_view(), name='test')
]
