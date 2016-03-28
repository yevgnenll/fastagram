"""fastagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from users.views import LoginView
from fastagram.views import HomePage
from posts.views import PostListView, PostDetailView, WritePostView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomePage.as_view(), name="home"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^posts/$', PostListView.as_view(), name="post_list"),
    url(r'^posts/(?P<pk>\d+)/$', PostDetailView.as_view(), name="post"),
    url(r'^posts/write/$', WritePostView.as_view(), name="write"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
