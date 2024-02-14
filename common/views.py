import urllib.request, json

from django.shortcuts import render
from django.views.generic import View
from django.db.models import Count
from django.utils.safestring import mark_safe
from django.conf import settings
from django.templatetags.static import static

from common.models import *
from collections import defaultdict, Counter

# import gdata.blogger.client
import iso8601
import urllib.request, urllib.error, urllib.parse

class Home(View):
    @staticmethod
    def num_format(value):
        return "{:,}".format(value)

    @staticmethod
    def lang_format(value):
        parts = value.split(" ")
        if len(parts) > 2:
            return "".join([part[0] for part in parts])
        return value

    def get(self, request):
        children = Administration.objects.values(
            "instrument__language", "dataset", "child__study_internal_id"
        ).distinct()
        num_children = len(children)
        num_children = Child.objects.all().count()
        child_counts = Counter([child["instrument__language"] for child in children])
        lang_stats = dict(child_counts)
        num_languages = len(child_counts)
        instruments = Instrument.objects.annotate(n=Count("administration"))
        num_instruments = len(instruments)
        num_admins = sum([inst.n for inst in instruments])
        data = {
            "num_children": self.num_format(num_children),
            "num_admins": self.num_format(num_admins),
            "num_languages": num_languages,
            "num_instruments": num_instruments,
            "lang_stats": lang_stats,
        }
        js_lang_stats = {
            "name": "",
            "children": [
                {"name": self.lang_format(language), "count": n}
                for language, n in lang_stats.items()
            ],
        }
        return render(
            request,
            "home.html",
            {"data": data, "lang_stats": json.dumps(js_lang_stats)},
        )


class Contributors(View):
    def get(self, request):
        sources = Dataset.objects.annotate(n=Count("administration")).order_by(
            "instrument__language"
        )
        language_sources_dict = defaultdict(lambda: defaultdict(int))
        for source in sources:
            language_sources_dict[source.instrument.language][
                (
                    source.contributor,
                    source.instrument.form,
                    source.license,
                    source.citation,
                )
            ] += source.n

        languages = sorted(language_sources_dict.keys())
        language_sources_list = [
            [language, dict(language_sources_dict[language])] for language in languages
        ]

        num_cols = 2
        col_size = (
            sum(
                [
                    len(language_sources)
                    for language, language_sources in language_sources_list
                ]
            )
            + len(language_sources_list) * 2
        ) / num_cols

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

        return render(
            request, "contributors.html", {"columns": columns, "sources": sources}
        )


class Analyses(View):
    def get(self, request):
        analyses = json.loads(
            open("wordbank/static/json/analyses.json", encoding="utf8").read()
        )
        if "name" in request.GET:
            name = request.GET["name"]
            # link = 'http://%s/%s' % (settings.SHINY_SERVER_IP, name)
            link = "%s/%s" % (settings.SHINY_SERVER_URL, name)
            return render(
                request,
                "analyses.html",
                {"name": name, "source": link, "analyses": analyses},
            )
        else:
            return render(request, "analyses_landing.html", {"analyses": analyses})


class Blog(View):
    @staticmethod
    def format_datetime(date_string):
        dt = iso8601.parse_date(date_string)
        return dt.strftime("%A, %B %d, %Y")

    def get(self, request):
        blog_url = (
            "https://www.googleapis.com/blogger/v3/blogs/"
            + settings.BLOG_ID
            + "/posts?key="
            + settings.BLOGGER_API_KEY
            + "&maxResults=100"
        )
        r = urllib.request.urlopen(blog_url)
        feed = json.loads(r.read().decode("utf-8"))
        entries = []
        for entry in feed["items"]:
            entries.append(
                {
                    "title": entry["title"],
                    "contents": mark_safe(entry["content"]),
                    "time": self.format_datetime(entry["published"]),
                    "author": entry["author"]["displayName"],
                }
            )

        events = json.loads(
            open("wordbank/static/json/events.json", encoding="utf8").read()
        )

        resources = json.loads(
            open("wordbank/static/json/resources.json", encoding="utf8").read()
        )

        return render(
            request,
            "blog.html",
            {"entries": entries, "events": events, "resources": resources},
        )


class Faq(View):
    def get(self, request):
        return render(request, "faq.html", {})


class About(View):
    def get(self, request):
        publications = json.loads(
            open("wordbank/static/json/publications.json", encoding="utf8").read()
        )
        persons = json.loads(
            open("wordbank/static/json/persons.json", encoding="utf8").read()
        )
        # publications = json.loads(urllib.request.urlopen(static('json/publications.json')).read())
        return render(
            request, "about.html", {"publications": publications, "persons": persons}
        )
