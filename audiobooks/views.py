from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.template import loader
from django.urls import reverse
from django.views.generic import DetailView, ListView

from .models import Audiobook
from django.utils import timezone

class IndexView(ListView):
    template_name = 'audiobooks/index.html'
    context_object_name = 'latest_audiobooks'

    def get_queryset(self):
        return Audiobook.objects.order_by('-date_released')[:5]


class DetailsView(DetailView):
    template_name = 'audiobooks/detail.html'
    model = Audiobook


def report_error(request, audiobook):
    context = {
        'audiobook' : audiobook,
        'error_msg' : 'Rating and/or comment were missing - both are required!'
    }
    return render(request, 'audiobooks/detail.html', context)


def review(request, audiobook_id):
    audiobook = get_object_or_404(Audiobook, pk=audiobook_id)
    try:
        rating = request.POST['rating']
        comment = request.POST['comment']
    except KeyError:
        return report_error(request, audiobook)

    if rating and comment and (len(rating) > 0) and (len(comment) > 0):
        audiobook.review_set.create(comment=comment, rating=rating, timestamp=timezone.now())
        return HttpResponseRedirect(reverse('audiobooks:results', args=(audiobook.id,)))
    else:
        return report_error(request, audiobook)


class ResultsView(DetailView):
    template_name = 'audiobooks/results.html'
    model = Audiobook


# V_02
# def results(request, audiobook_id):
#     audiobook = get_object_or_404(Audiobook, pk=audiobook_id)
#     return render(request, 'audiobooks/results.html', {'audiobook':audiobook})
#


# V_01
# def results(request, audiobook_id):
#     return HttpResponse("This presents detail info, the latest review included, "
#                         "about the audiobook with id {}".format(audiobook_id))



# V_01
# def review(request, audiobook_id):
#     return HttpResponse("This view processes any review submitted for the "
#                         "audiobook with id {}".format(audiobook_id))


# V_03
# def details(request, audiobook_id):
#     audiobook = get_object_or_404(Audiobook, pk=audiobook_id)
#     return render(request, 'audiobooks/detail.html', {'audiobook':audiobook})


# V_02
# def details(request, audiobook_id):
#     try:
#         audiobook = Audiobook.objects.get(pk=audiobook_id)
#     except Audiobook.DoesNotExist:
#         raise Http404('Audiobook with id {} does not exist'.format(audiobook_id))
#     return render(request, 'audiobooks/detail.html', {'audiobook':audiobook})


# V_01
# def details(request, audiobook_id):
#     return HttpResponse("This page will provide detail information "
#                         "about the audiobook with id {}".format(audiobook_id))


# V_04
# def index(request):
#     latest_books = Audiobook.objects.order_by('-date_released')[:5]
#     context = {
#         'latest_audiobooks': latest_books
#     }
#     return render(request, 'audiobooks/index.html', context)


# V_03
# def index(request):
#     latest_books = Audiobook.objects.order_by('-date_released')
#     if latest_books and (len(latest_books) > 5):
#         latest_books = latest_books[:5]
#     context = {
#         'latest_audiobooks': latest_books
#     }
#     index_template = loader.get_template('audiobooks/index.html')
#     return HttpResponse(index_template.render(context, request))


# V_02
# def index(request):
#     latest_books = Audiobook.objects.order_by('-date_released')
#     if latest_books and (len(latest_books) > 5):
#         latest_books = latest_books[:5]
#     response = "<h3>Recently released audiobooks:</h3><ul>"
#     response += "<br/>".join(["<li>" + book.title + "</li>" for book in latest_books])
#     response += "</ul>"
#     return HttpResponse(response)


# V_01
# def index(request):
#     return HttpResponse("Hello! Welcome to the Django Audiobooks library")
