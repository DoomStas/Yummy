from .models import FooterItem

def footer_items(request):

    context = {}
    items = FooterItem.objects.all()
    for item in items:
        if item.title_title == 'Address':
            context['address'] = item
        elif item.title_title == 'Reservation':
            context['reservation'] = item

    return{
        'footer_items':context

    }