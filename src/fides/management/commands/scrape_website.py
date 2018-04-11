import requests

from django.core.management.base import BaseCommand

from fides.lib.html_parser import FidesHtmlParser
from fides.lib.html_retriever import FidesHtmlRetriever
from fides.models.project import (Project, ProjectPage, )


class Command(BaseCommand):
    """
    Custom command that scrapes a website and stores all internal URLs
    """
    help = 'Scrape website and store internal URLs.'    
    urls = []
    project = None

    def handle(self, *args, **options):
        self.project = Project.get_project_for_scraping()

        if self.project:
            self.urls.append(self.project.url)

        self.crawl()


    def crawl(self):
        while self.urls:
            url = self.urls.pop()
            url = self.make_url_absolute(url)
            is_url_stored = ProjectPage.create(self.project, url)

            if is_url_stored:
                self.explore_url(url)


    def make_url_absolute(self, url):
        if url and url[0] == '/':
            url = "{}{}".format(self.project.url, url)

        return url


    def explore_url(self, url):
        page_parser = self.get_page_parser(url)
        local_urls = page_parser.extract_local_urls()
        self.urls = self.urls + local_urls


    def get_page_parser(self, url):
        page_html = self.get_page_html(url)

        return FidesHtmlParser(url, page_html, 'html5lib')


    def get_page_html(self, url):
        html_retriever = FidesHtmlRetriever(url)

        return html_retriever.get_html()
                

