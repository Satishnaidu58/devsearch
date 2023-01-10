from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Project, Tag


def paginateProject(request, projects, results):
    # quetying pg number from front_end
    page = request.GET.get("page")
    # passing(queryset, number of items)
    paginator = Paginator(projects, results)
    # handling errors
    try:
        projects = paginator.page(page)
    # if pageNo is not passs in
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    # pg_no doesn't eixst
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)
    # dynamic range window for pages
    leftIndex = (int(page)-4)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page)+4)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
    custom_range = range(leftIndex, rightIndex)
    return custom_range, projects


def searchProjects(request):
    search_query = ""
    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")
    # tag's ManyToManyField of projects, 
    # "tags__in=tags" query tags in project or not
    tags = Tag.objects.filter(name__icontains=search_query)
    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
        )
    return projects, search_query