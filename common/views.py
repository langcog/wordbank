from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.db.models import Count
from django.utils.safestring import mark_safe

from common.models import *
from wordbank import settings
from collections import defaultdict

import gdata.blogger.client
import rfc3339

class Home(View):

    def get(self, request):
        return render(request, 'home.html', {})


class About(View):

    def get(self, request):
        return render(request, 'about.html', {})


class Contributors(View):

    def get(self, request):
        sources = Source.objects.annotate(n = Count('administration'))
        language_sources_dict = defaultdict(lambda: defaultdict(list))
        for source in sources:
            language_sources_dict[source.instrument_language][(source.contributor, source.instrument_form, source.citation)].append(source.n)

        languages = sorted(language_sources_dict.keys())
        language_sources_list = [[language, dict(language_sources_dict[language])] for language in languages]

        num_cols = 2
        col_size = (sum([sum([len(sources) for contributor, sources in language_sources.iteritems()]) for language, language_sources in language_sources_list]) + len(language_sources_list)*2) / num_cols

        columns = {}
        col_index = 1
        item_buffer = []
        buffer_size = 0
        for language, language_sources in language_sources_list:
            item_buffer.append([language, language_sources])
            buffer_size += len(language_sources) + 2
            if buffer_size >= col_size:
                columns[col_index] = item_buffer
                col_index += 1
                item_buffer = []
                buffer_size = 0
            columns[col_index] = item_buffer

        return render(request, 'contributors.html', {'columns': columns})

class Reports(View):

    def get(self, request):
        if 'name' in request.GET:
            name = request.GET['name']
            link = 'http://%s/%s' % (settings.SHINY_SERVER_IP, name)
            return render(request, 'reports.html', { 'source': link })
        else:
            return render(request, 'reports_landing.html', {})

class Blog(View):

    @staticmethod
    def format_datetime(date_string):
        dt = rfc3339.parse_datetime(date_string)
        return dt.strftime("%A, %B %d, %Y")

    def get(self, request):
        blog_id = "4368769871770527749"
        blogger_service = gdata.blogger.client.BloggerClient()
        feed = blogger_service.GetFeed('http://www.blogger.com/feeds/' + blog_id + '/posts/default')
        entries = [{'title': entry.title.text,
                    'contents': mark_safe(entry.content.text),
                    'time': self.format_datetime(entry.published.text),
                    'author': entry.author[0].name.text,
                    'author_link': entry.author[0].uri.text
                   } for entry in feed.entry]
        return render(request, 'blog.html', {'entries': entries})

class Tutorial(View):

    def get(self, request):
        return render(request, 'tutorial.html', {})
