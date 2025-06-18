from django.urls import path
from . import views

urlpatterns = [
    # Записи ДДС
    path('', views.RecordListView.as_view(), name='records'),
    path('create/', views.create_record, name='create_record'),
    path('update/<int:pk>/', views.update_record, name='update_record'),
    path('delete/<int:pk>/', views.delete_record, name='delete_record'),
    
    # Справочники
    path('dictionaries/', views.DictionaryListView.as_view(), name='dictionaries'),
    
    path('status/create/', views.StatusCreateView.as_view(), name='create_status'),
    path('status/update/<int:pk>/', views.StatusUpdateView.as_view(), name='update_status'),
    path('status/delete/<int:pk>/', views.StatusDeleteView.as_view(), name='delete_status'),

    path('type/create/', views.TypeCreateView.as_view(), name='create_type'),
    path('type/update/<int:pk>/', views.TypeUpdateView.as_view(), name='update_type'),
    path('type/delete/<int:pk>/', views.TypeDeleteView.as_view(), name='delete_type'),

    path('category/create/', views.CategoryCreateView.as_view(), name='create_category'),
    path('category/update/<int:pk>/', views.CategoryUpdateView.as_view(), name='update_category'),
    path('category/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='delete_category'),

    path('subcategory/create/', views.SubcategoryCreateView.as_view(), name='create_subcategory'),
    path('subcategory/update/<int:pk>/', views.SubcategoryUpdateView.as_view(), name='update_subcategory'),
    path('subcategory/delete/<int:pk>/', views.SubcategoryDeleteView.as_view(), name='delete_subcategory'), 

    # AJAX
    path('get_categories/', views.get_categories, name='get_categories'),
    path('get_subcategories/', views.get_subcategories, name='get_subcategories'),
]
