from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.db.models import Count
from django.utils.safestring import mark_safe
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static

from common.models import *
from collections import defaultdict, Counter
import json
import gdata.blogger.client
import rfc3339
import urllib2

class Home(View):

    @staticmethod
    def format(value):
        return "{:,}".format(value)

    def get(self, request):
        children = Administration.objects.values('instrument__language', 'source', 'child__study_id').distinct()
        num_children = len(children)
        child_counts = Counter([child['instrument__language'] for child in children])
        lang_stats = dict(child_counts)
        num_languages = len(child_counts)
        instruments = Instrument.objects.annotate(n = Count('administration'))
        num_instruments = len(instruments)
        num_admins = sum([inst.n for inst in instruments])
        data = {'num_children': self.format(num_children), 'num_admins': self.format(num_admins), 'num_languages': num_languages, 'num_instruments': num_instruments, 'lang_stats': lang_stats}
        js_lang_stats = {"name": "", "children": [{"name": language, "count": n} for language, n in lang_stats.iteritems()]}
        return render(request, 'home.html', {'data': data, 'lang_stats': json.dumps(js_lang_stats)})


class Publications(View):

    def get(self, request):
        #publications = json.loads(open('static/json/publications.json').read())
        publications = json.loads(urllib2.urlopen(static('json/publications.json')).read())
        return render(request, 'publications.html', {'publications': publications})


class Contributors(View):

    def get(self, request):
        sources = Source.objects.annotate(n = Count('administration'))
        language_sources_dict = defaultdict(lambda: defaultdict(int))
        for source in sources:
            language_sources_dict[source.instrument_language][(source.contributor, source.instrument_form, source.citation)] += source.n

        languages = sorted(language_sources_dict.keys())
        language_sources_list = [[language, dict(language_sources_dict[language])] for language in languages]

        num_cols = 2
        col_size = (sum([len(language_sources) for language, language_sources in language_sources_list]) + len(language_sources_list)*2) / num_cols

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

class Analyses(View):

    def get(self, request):
        if 'name' in request.GET:
            name = request.GET['name']
            link = 'http://%s/%s' % (settings.SHINY_SERVER_IP, name)
            return render(request, 'analyses.html', { 'source': link })
        else:
            return render(request, 'analyses_landing.html', {})

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
                    'author': entry.author[0].name.text
                    #'author_link': entry.author[0].uri.text
                   } for entry in feed.entry]

        events = json.loads(urllib2.urlopen(static('json/events.json')).read())

        resources = json.loads(urllib2.urlopen(static('json/resources.json')).read())

        return render(request, 'blog.html', {'entries': entries, 'events': events, 'resources': resources})

class Faq(View):

    def get(self, request):
        return render(request, 'faq.html', {})
