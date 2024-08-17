from django.db import models

from users.models import User

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
        upload_to="media/product/",
        verbose_name="Изображение товара",
        help_text="Загрузите фото товара",
        **NULLABLE,
    )
    product_category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        **NULLABLE,
        related_name="products",
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена за покупку", help_text="Введите цену"
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="products",
        **NULLABLE,
        verbose_name="Владелец",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["created_at"]


class Category(models.Model):
    """Класс для описания модели категорий"""
    name = models.CharField(
        max_length=100, verbose_name="Категория", help_text="Введите название категории"
    )
    description = models.TextField(
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


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="version",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Версия",
    )
    v_num = models.CharField(
        max_length=100,
        verbose_name="№ версии",
        help_text="Введите № версии",
    )
    v_name = models.CharField(
        max_length=100,
        verbose_name="Название версии",
        help_text="Введите название версии",
    )
    curr_v = models.BooleanField(
        verbose_name="Признак текущей версии",
        help_text="Активно?"
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["product"]

    def __str__(self):
        return f"Наименование продукта - {self.product}, Версия - {self.v_num}"

