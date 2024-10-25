from .models import FooterItem

def footer_items(request):

    context = {}
    items = FooterItem.objects.all()
    for item in items:
        if item.item_title == 'Address':
            context['address'] = item
        elif item.item_title == 'Reservation':
            context['reservation'] = item

    return{
        'footer_items':context

    }