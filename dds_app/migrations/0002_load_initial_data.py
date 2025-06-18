from django.db import migrations

def load_initial_data(apps, schema_editor):
    Status = apps.get_model('dds_app', 'Status')
    Type = apps.get_model('dds_app', 'Type')
    Category = apps.get_model('dds_app', 'Category')
    Subcategory = apps.get_model('dds_app', 'Subcategory')

    # Создаем статусы
    statuses = ['Бизнес', 'Личное', 'Налог']
    for status in statuses:
        Status.objects.get_or_create(name=status)

    # Создаем типы
    types = ['Пополнение', 'Списание']
    for type_name in types:
        Type.objects.get_or_create(name=type_name)

    # Создаем категории и подкатегории
    spending_type = Type.objects.get(name='Списание')
    
    infrastructure = Category.objects.create(name='Инфраструктура', type=spending_type)
    Subcategory.objects.create(name='VPS', category=infrastructure)
    Subcategory.objects.create(name='Proxy', category=infrastructure)
    
    marketing = Category.objects.create(name='Маркетинг', type=spending_type)
    Subcategory.objects.create(name='Farpost', category=marketing)
    Subcategory.objects.create(name='Avito', category=marketing)

class Migration(migrations.Migration):
    dependencies = [
        ('dds_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]
