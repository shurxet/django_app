from django import template
from django.utils.safestring import mark_safe
from treemenu.models import Menu


register = template.Library()


def rendered_html(menu_items):
    # Генерируем HTML-код для меню и для категорий
    rendered_menu_html = ""
    for item in menu_items:
        rendered_menu_html += \
            f"<li>\n<a href='/menu/byname/{item}/'><h2 style='color: blueviolet'>{item}</h2></a>\n</li>\n"
        for cat in item.category.all():
            rendered_menu_html += f"<li><a href='{cat.url}'><p style='color: blueviolet'>{cat}</p></a></li>\n"
    return rendered_menu_html


@register.simple_tag
def draw_menu(menu_name=None):
    """
    Данная функция:
        принимает название меню если оно передано;
        получает данные по имени меню из базы данных;
        если название не передано то получает все обекты меню;

        отдаёт сгенерированную html страницу <class 'str'>
        :return <class 'django.utils.safestring.SafeString'>

    """
    if menu_name is None:
        # Делаем запрос в базу, в котором подтягиваем данные из manytomanyfield c помощью prefetch_related('category')
        menu_items = Menu.objects.prefetch_related('category').order_by('title')
        result = rendered_html(menu_items)
        return mark_safe(result)
    else:
        menu_items = Menu.objects.filter(title=menu_name).prefetch_related('category').order_by('title')
        result = rendered_html(menu_items)
        return mark_safe(result)
