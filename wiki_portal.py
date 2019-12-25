import re
from wikipedia import wikipedia
import pickle


def preprocess_wikipedia_text(wiki_content):
    garbage_matching_regex = r'(=+\s(References|External links)\s=+(.|\s)*$)|' \
                             r'(=+.+=+)'

    return re.sub(string=wiki_content, pattern=garbage_matching_regex, repl='')


def wiki_search(term, max_results):
    cached_result = get_search_cache(term)
    if cached_result:
        return cached_result
    else:
        result = wikipedia.search(term, query=max_results)
        cache_search_result(term, result)
        return result


def get_phrases(term):
    subject_text = preprocess_wikipedia_text(wikipedia.page(term).content)

    sentences = [re.sub(pattern='\n', repl='', string=sentence) for sentence in subject_text.split('.')]
    return sentences


def cache_search_result(term, result):
    pass


def cache_article():
    pass


def get_article_cache():
    pass


def get_search_cache(term):
    try:
        with open('wikicache.pickle', mode='r') as wiki_pickle:
            cache = pickle.load(file=wiki_pickle)
        return cache.get(term, default=None)
    except FileNotFoundError:
        return None
