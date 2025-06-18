from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse
from django.utils import timezone
from .models import Record, Status, Type, Category, Subcategory
from .forms import RecordForm, StatusForm, TypeForm, CategoryForm, SubcategoryForm

class RecordListView(ListView):
    model = Record
    template_name = 'records.html'
    context_object_name = 'records'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset().select_related(
            'status', 'type', 'category', 'subcategory'
        )
        
        # Фильтрация
        filters = {}
        for param in ['status', 'type', 'category', 'subcategory']:
            value = self.request.GET.get(param)
            if value:
                filters[f"{param}_id"] = value
        
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        if date_from:
            queryset = queryset.filter(date__gte=date_from)
        if date_to:
            queryset = queryset.filter(date__lte=date_to)
        
        return queryset.filter(**filters).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['types'] = Type.objects.all()
        context['categories'] = Category.objects.all()
        context['subcategories'] = Subcategory.objects.all()
        return context

def create_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('records')
    else:
        form = RecordForm()
        form.initial['date'] = timezone.now().date()  # Установка текущей даты
    return render(request, 'record_form.html', {'form': form})

def update_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('records')
    else:
        form = RecordForm(instance=record)
    return render(request, 'record_form.html', {'form': form})

def delete_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('records')
    return render(request, 'confirm_delete.html', {'object': record})

def get_categories(request):
    type_id = request.GET.get('type_id')
    categories = Category.objects.filter(type_id=type_id)
    return JsonResponse(list(categories.values('id', 'name')), safe=False)

def get_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = Subcategory.objects.filter(category_id=category_id)
    return JsonResponse(list(subcategories.values('id', 'name')), safe=False)

class DictionaryListView(ListView):
    template_name = 'dictionaries.html'
    
    def get(self, request, *args, **kwargs):
        context = {
            'statuses': Status.objects.all(),
            'types': Type.objects.all(),
            'categories': Category.objects.all(),
            'subcategories': Subcategory.objects.all(),
        }
        return render(request, self.template_name, context)

# Управление справочниками
class StatusCreateView(CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'dictionary_form.html'
    
    def get_success_url(self):
        return reverse('dictionaries') + '#statuses'

class StatusUpdateView(UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'dictionary_form.html'
    
    def get_success_url(self):
        return reverse('dictionaries') + '#statuses'

class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'confirm_delete.html'
    
    def get_success_url(self):
        return reverse('dictionaries') + '#statuses'

class TypeCreateView(CreateView):
    model = Type
    form_class = TypeForm
    template_name = 'dictionary_form.html'
    
    def get_success_url(self):
        return reverse('dictionaries') + '#types'

class TypeUpdateView(UpdateView):
    model = Type
    form_class = TypeForm
    template_name = 'dictionary_form.html'
    
    def get_success_url(self):
        return reverse('dictionaries') + '#types'

class TypeDeleteView(DeleteView):
    model = Type
    template_name = 'confirm_delete.html'
    
    def get_success_url(self):
        return reverse('dictionaries') + '#types'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'dictionary_form.html'
    
    def get_success_url(self):
        return reverse('dictionaries') + '#categories'
    
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'dictionary_form.html'
    
    def get_success_url(self):
        return reverse('dictionaries') + '#categories'
    
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'confirm_delete.html'
    
    def get_success_url(self):
        return reverse('dictionaries') + '#categories'
    
class SubcategoryCreateView(CreateView):
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'dictionary_form.html'
    
    def get_success_url(self):
        return reverse('dictionaries') + '#subcategories'
    
class SubcategoryUpdateView(UpdateView):
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'dictionary_form.html'
    
    def get_success_url(self):
        return reverse('dictionaries') + '#subcategories'
    
class SubcategoryDeleteView(DeleteView):
    model = Subcategory
    template_name = 'confirm_delete.html'
    
    def get_success_url(self):
        return reverse('dictionaries') + '#subcategories'  
