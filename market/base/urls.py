from django.urls import path
from .views import ItemListView, ItemDetailView, ItemCreateView, ItemUpdateView

app_name = 'base'

urlpatterns = [
    path('', ItemListView.as_view(), name='itemlist'),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('create/', ItemCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
]
