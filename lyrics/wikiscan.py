import re
from wikipedia import wikipedia
import pickle


class WikiScan:
    def __init__(self):
        self.article_cache = 'lyrics/cache/article_cache.pickle'
        self.search_cache = 'lyrics/cache/search_cache.pickle'

    def search(self, term, max_results):
        cached_result = self._get_search_cache(term)
        if cached_result:
            return cached_result

        result = wikipedia.search(term, query=max_results)
        self.cache_search_result(term, result)
        return result

    def get_phrases(self, article_name):
        cached_article = self._get_article_cache(article_name)
        if cached_article:
            print('Read cache')
            return cached_article

        page = wikipedia.page(article_name).content
        processed_page = self._process_wikipedia_text(page)
        self.cache_article(article_name, processed_page)
        return processed_page

    @staticmethod
    def _process_wikipedia_text(wiki_content):
        garbage_matching_regex = r'(=+\s(References|External links)\s=+(.|\s)*$)|' \
                                 r'(=+.+=+)'

        page_without_garbage = re.sub(string=wiki_content, pattern=garbage_matching_regex, repl='')
        sentences = [re.sub(pattern='\n', repl='', string=sentence) for sentence in page_without_garbage.split('.')]
        return sentences

    @staticmethod
    def _read_cache(file, key):
        try:
            with open(file, mode='rb') as pickle_file:
                cache = pickle.load(file=pickle_file)
            return cache.get(key)
        except (FileNotFoundError, EOFError):
            return None

    @staticmethod
    def _write_cache(file, key, value):
        with open(file, mode='rb') as pickle_file:
            try:
                cache = pickle.load(file=pickle_file)
            except EOFError:
                cache = {}

        cache[key] = value

        with open(file, mode='wb') as pickle_file:
            pickle.dump(cache, pickle_file)

    def cache_search_result(self, term, result):
        return self._write_cache(self.search_cache, term, result)

    def cache_article(self, article_name, contents):
        return self._write_cache(self.article_cache, article_name, contents)

    def _get_article_cache(self, article_name):
        return self._read_cache(self.article_cache, article_name)

    def _get_search_cache(self, term):
        return self._read_cache(self.search_cache, term)
