# includes: [saerch function, ]

# imports
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Profile, Skill


def paginateProfiles(request, profiles, results):
    # quetying pg number from front_end
    page = request.GET.get("page")
    # passing(queryset, number of items)
    paginator = Paginator(profiles, results)
    # handling errors
    try:
        profiles = paginator.page(page)
    # if pageNo is not passs in
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    # pg_no doesn't eixst
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)
    # dynamic range window for pages
    leftIndex = (int(page)-4)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page)+4)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
    custom_range = range(leftIndex, rightIndex)
    return custom_range, profiles


def searchProfiles(request):
    search_query = ""
    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")
    # query set of skills
    skills = Skill.objects.filter(name__iexact=search_query)
    # query set to do case sensitive search, 
    # with distinct objects to handel skill query's causing duplicate
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains = search_query) |
        Q(skill__in=skills)
    )

    return profiles, search_query
