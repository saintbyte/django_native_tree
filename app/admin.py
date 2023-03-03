from django.contrib import admin

from app.models import Tree
from app.models import TreeItem


class TrueItemInline(admin.StackedInline):
    model = TreeItem
    extra = 0


class TreeAdmin(admin.ModelAdmin):
    inlines = [
        TrueItemInline,
    ]


admin.site.register(Tree, TreeAdmin)
