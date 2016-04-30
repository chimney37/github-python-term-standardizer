import wikipedia
import datetime

class wikiScraper(object):
    """
        A wrapper class for scraping wikipedia using a simple Media Wiki API
        https://pypi.python.org/pypi/wikipedia/
        """

    def __init__(self, lang):
        """
            Initializes the wikiScraper class, given a language.
            """
        # set rate limit
        wikipedia.set_rate_limiting(True, min_wait=datetime.timedelta(0, 0, 500000))
        # set language
        wikipedia.set_lang(lang)

    def getPage(self,title):
        """
            Get the page object given a title (the title must exist in wiki for a given language)
            """
        return wikipedia.page(title)

    def getPageTitle(self,title):
        """
            Get the title from a page object given a title (the title must exist in the wiki for a given language)
            """
        return self.getPage(title).title

    # get the summary
    def getSummary(self,title):
        return self.getPage(title).summary

    # search for keyword
    def searchKw(self, kw):
        return wikipedia.search(kw)

