from django.shortcuts import render
from .models import DarmokUser

# Create your views here.
def landing_page(request):
    # retrieve all objects
    users = DarmokUser.objects.all()
    for user in users:
        print(user.phone_number)
    # Pagination with 3 posts per page
    # paginator = Paginator(post_list, 3)
    # get the page number from the url '?page=PAGE_NUMBER'
    # page_number = request.GET.get('page', 1)
    # check if page exists
    # try:
    #     posts = paginator.page(page_number)
    # except PageNotAnInteger:
    #     # If page_number is not an integer get the first page
    #     posts = paginator.page(1)
    # except EmptyPage:
    #     # If page_number is out of range get last page of results
    #     posts = paginator.page(paginator.num_pages)

    return render(request, 'base.html', )