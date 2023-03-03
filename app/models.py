from django.db import models

from app.managers import TreeItemManager
from app.managers import TreeManager


class Tree(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название дерева")
    slug = models.SlugField(unique=True, verbose_name="Текстовый id")

    objects = TreeManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дерево"
        verbose_name_plural = "Деревья"


class TreeItem(models.Model):
    menu = models.ForeignKey(
        Tree, on_delete=models.CASCADE, related_name="items", verbose_name="Меню"
    )
    name = models.CharField(max_length=128, verbose_name="Название")
    to = models.CharField(
        unique=True,
        verbose_name="Ссылка",
        help_text="URL полный или относительный или имя в роутах джанго",
        max_length=128,
    )
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    order_index = models.PositiveIntegerField(default=0, verbose_name="Сортировка")

    objects = TreeItemManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ветка дерева"
        verbose_name_plural = "Ветки деревьев"
        ordering = [
            "order_index",
        ]
