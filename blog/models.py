from django.db import models


class BlogPost(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        help_text="Введите заголовок",
    )
    slug = models.CharField(
        max_length= 50,
        verbose_name="Ссылка",
        help_text="Введите ссылку",
        unique=True,
        blank=True,
    )
    content = models.TextField(
        verbose_name="Содержимое",
        help_text="Введите текст",
    )
    preview = models.ImageField(
        upload_to="blog/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото"
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True,
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано",
        help_text="Опубликовать запись"
    )

    view_count = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите кол-во просмотров",
        default=0
    )

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"

    def __str__(self):
        return self.title
