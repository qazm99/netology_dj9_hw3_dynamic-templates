from django.shortcuts import render

def index_view(request, page='home'):
    template_name = 'app/index.html'
    if page == 'examples':
        items = [{
            'title': 'Apple II',
            'text': 'Легенда',
            'img': 'ii.jpg'
        }, {
            'title': 'Macintosh',
            'text': 'Свежие новинки октября 1983-го',
            'img': 'mac.jpg'
        }, {
            'title': 'iMac',
            'text': 'Оригинальный и прозрачный',
            'img': 'imac.jpg'
        }]
    else:
        items = ''
    return render(request, template_name, context={'page': page, 'items': items})
