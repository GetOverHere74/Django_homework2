from django.db import models

NULLABLE = {"blank": True, "null": True}


# Create your models here.
class Product(models.Model):
    """Класс для описания модели продуктов"""
    name = models.CharField(
        max_length=100, verbose_name="Товар", help_text="Введите название товара"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание товара", **NULLABLE
    )
    image = models.ImageField(
        upload_to="product/",
        verbose_name="Изображение товара",
        height_field="Загрузите фото товара",
        **NULLABLE,
    )
    product_category = models.ForeignKey(
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        **NULLABLE,
        related_name="products",
    )
    price = models.ImageField(
        max_length=10, verbose_name="Цена за покупку", help_text="Введите цену"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["-created_at"]


class Category(models.Model):
    """Класс для описания модели категорий"""
    name = models.CharField(
        max_length=100, verbose_name="Категория", help_text="Введите название категории"
    )
    category_description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]
