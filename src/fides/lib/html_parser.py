from bs4 import (BeautifulSoup, )


class FidesHtmlParser():

    parser = None
    page_url = None

    def __init__(self, page_url, html, html_parsing_library):
        self.page_url = page_url
        self.parser = BeautifulSoup(html, html_parsing_library)


    def extract_local_urls(self):
        urls = self.extract_urls()

        return self.filter_local_urls(urls)


    def extract_urls(self):
        urls = []
        page_urls = self.parser.find_all('a', href=True)
        for url in page_urls:
            urls.append(url['href'])

        return urls


    def filter_local_urls(self, urls):
        local_urls = []

        for url in urls:
            if self.is_local_url(url):
                local_urls.append(url)

        return local_urls


    def is_local_url(self, url):
        if url and url[0] == '/':
            return True

        if url.startswith(self.page_url):
            return True

        return False