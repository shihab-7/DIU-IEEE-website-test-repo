from .models import WebsiteSettings

def website_settings(request):
    try:
        settings = WebsiteSettings.objects.first()  # Get the first WebsiteSettings object
    except WebsiteSettings.DoesNotExist:
        settings = None
    return {'site_settings': settings}