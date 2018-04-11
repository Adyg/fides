import requests

class FidesHtmlRetriever():

    retriever = None

    def __init__(self, url):
        self.retriever = requests.get(url)


    def get_html(self):

        return self.retriever.content
