from django.shortcuts import render
from Events.models import Event
from Members.models import MemberProfile, Projects
from django.db.models import Q



def home(request):
    events = Event.objects.all().order_by('-event_date')
    advisors = MemberProfile.objects.filter(member_type='advisor')
    core_posts = MemberProfile.objects.filter(member_type='committee', club_position__in=['chairperson', 'vice-chairperson', 'general secretary', 'treasurer'])
    operating_posts = MemberProfile.objects.filter(member_type='committee', club_position__in=['webmaster', 'event coordinator', 'public & social media coordinator', 'public relationship secretary', 'women activities coordinator', 'membership & outreach coordinator', 'technical coordinator'])
    
    #member search
    search_query = request.GET.get('q')
    member = None
    if search_query:
        member = MemberProfile.objects.filter(
            Q(user__username__icontains=search_query) |
            Q(member_id__icontains=search_query) |
            Q(user__email__icontains=search_query)
        )
    else:
        member = MemberProfile.objects.none()

    return render(request, 'home.html', {'events': events, 'advisors': advisors,'core_posts': core_posts,'operating_posts': operating_posts,'member': member})


def research(request):
    projects = Projects.objects.all()
    return render(request, 'research_works.html', {'research_works': projects})