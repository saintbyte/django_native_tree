from typing import Union

from django.db import models
from django.db.models import Q


class TreeManager(models.Manager):
    def items(self):
        return self.annotate()


class TreeItemManager(models.Manager):
    def get_by_to(self, to: Union[list, str]):
        """Поиск элемента по ссылке или списку"""
        if isinstance(to, str):
            to = [
                to,
            ]
        q = Q(to=to.pop())
        for search_item in to:
            q = q | Q(to=search_item)
        query = self.filter(q)
        if query.count() > 0:
            return query[0]
        return None
