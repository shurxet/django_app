from django.shortcuts import render


def menu(request, menu_name=None):
    return render(request, '../templates/menu.html', {'menu_name': menu_name})
