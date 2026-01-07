from utility.models import SocialLink
from .models import Category
# to fetch these variable or attiribute any where in the webpage i.e between multiple webpage
def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)


def get_social_links(request):
    social_links = SocialLink.objects.all()
    return dict(social_links= social_links) # next registers these link in templates of blog_main setting