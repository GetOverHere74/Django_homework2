import psycopg2
from django.core.management import BaseCommand
import json
from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Подключение к базе данных
        with psycopg2.connect(database='catalog', user='postgres', password='Admin1') as conn:
            with conn.cursor() as cur:
                # Удаление данных из таблицы Category и Product
                cur.execute('TRUNCATE TABLE catalog_product RESTART IDENTITY')
                conn.commit()
                cur.execute('TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE')
                conn.commit()

        # Соединение с файлом
        with open('C:/PyCharm/Django_homework2.1/fixtures/catalog_data.json', 'r', encoding='utf-8') as info_json:
            info_python = json.load(info_json)

            # Заполнение таблицы Category
            category_fill = []
            product_fill = []
            for c in info_python:
                if c['model'] == 'catalog.category':
                    category_fill.append(Category(**c['fields']))
            Category.objects.bulk_create(category_fill)

            # Заполнение таблицы Product
            pk_ = 1
            for c in info_python:
                if c['model'] == 'catalog.product':
                    fields = c['fields']
                    if 'catalog.category' in fields:
                        i = {
                            'pk': pk_,
                            'name': fields['name'],
                            'description': fields['description'],
                            'image': fields['image'],
                            'price': fields['price'],
                            'created_at': fields['created_at'],
                            'updated_at': fields['updated_at'],
                            'catalog.category': Category.objects.get(pk=fields['catalog.category'])
                        }
                        pk_ += 1
                        product_fill.append(Product(**i))
            Product.objects.bulk_create(product_fill)
