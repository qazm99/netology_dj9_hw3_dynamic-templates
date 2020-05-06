from django.shortcuts import render
import csv
from .settings import BASE_DIR


def inflation_view(request):
    template_name = 'inflation.html'
    with open(f'{BASE_DIR}\inflation_russia.csv', encoding='utf-8') as file:
        inf_list = [list(map(lambda value_in_list: float(value_in_list) if len(value_in_list) > 0 else '-',
                             list_in_list)) for list_in_list in list(csv.reader(file, delimiter=';'))[1:]]
        inf_list = [([int(list_in_list[0]), ] + list_in_list[1:]) for list_in_list in inf_list]
        print(inf_list)
    context = {'years': inf_list}
    return render(request, template_name, context)