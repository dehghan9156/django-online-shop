from .models import Category

def categories_processor(request):
    return {
        'Categories': Category.objects.all()
    }
