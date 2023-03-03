from django import template
from django.http import HttpRequest
from django.urls import NoReverseMatch
from django.urls import reverse
from django.utils.html import mark_safe

from app.models import Tree
from app.models import TreeItem

register = template.Library()


def _render_level(items, current: TreeItem, parent: TreeItem = None):
    def _get_level_by_parent(items, parent):
        return list(filter(lambda item: item.parent == parent, items.all()))

    def _parent_allowed(current: TreeItem, parent: TreeItem, branch: list = []):

        if parent is None:
            return True
        if parent in branch:
            return True

        return False

    def _get_url(to: str):
        try:
            return reverse(to)
        except NoReverseMatch:
            pass
        return to

    def _get_branch(items, current):
        if current is None:
            return []
        result = [
            current,
        ]
        while current.parent is not None:
            current = current.parent
            result.append(current)
        return result

    level_items = _get_level_by_parent(items, parent)
    branch = _get_branch(items, current)
    if len(level_items) == 0:
        return ""
    if not _parent_allowed(current, parent, branch):
        return ""
    html = "<ul>"
    for item in level_items:
        html = html + f'<li><a href="{_get_url(item.to)}">{item.name}</a></li>'
        html = html + _render_level(items, current, item)
    html = html + "</ul>"
    return html


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_slug: str, *args, **kwargs):
    try:
        menu_main_obj = Tree.objects.get(slug=menu_slug)
    except Tree.DoesNotExist:
        return mark_safe("[ дерево на найдено ]")
    request: HttpRequest = context.request
    current_named_route_name = request.resolver_match.url_name
    current_tree_item = menu_main_obj.items.get_by_to(
        [
            request.build_absolute_uri(),
            request.get_full_path(),
            current_named_route_name,
        ]
    )
    html: str = _render_level(menu_main_obj.items, current_tree_item)
    return mark_safe(html)
