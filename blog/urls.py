from django.urls import path
from django.views import generic

from blog import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="index-page"),
    path("about/", generic.TemplateView.as_view(template_name="blog/about.html"), name="about-view"),
    path("contacts/", generic.TemplateView.as_view(template_name="blog/contacts.html"), name="contacts-view"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post-detail"),
    path("post/update/<int:pk>", views.PostUpdateView.as_view(), name="post-update"),
    path("post/create", views.PostCreateView.as_view(), name="post-create"),
    path("post/delete/<int:pk>", views.PostDeleteView.as_view(), name="post-delete"),
    path("api/posts/list/", views.PostListAPIView.as_view(), name="api-post-list"),
    path("api/posts/<int:pk>/", views.PostDetailAPIView.as_view(), name="api-post-detail"),
    path("api/posts/create/", views.PostCreateAPIView.as_view(), name="api-post-create"),
]
