from lyrics.lyrics_graph import RhymeGraph
from lyrics.wikiscan import WikiScan

#
# def prompt_user(wiki):
#     term = input('Please enter a subject to rap about: ').strip()
#     search_results = wiki_search(term, 5)
#     wiki_chosen = None
#     if len(search_results) == 0:
#         print('Sorry no wikipedia entries were found for the term {}'.format(term))
#     elif len(search_results) > 1:
#         print('Did you mean:')
#         for index, result in enumerate(search_results):
#             print('{}) {}'.format(index + 1, result))
#         selected = int(input().strip())
#         wiki_chosen = search_results[selected - 1]
#     else:
#         wiki_chosen = search_results[0]
#     return wiki_chosen


def main():
    wiki = WikiScan()
    print('Getting all phrases...')
    all_phrases = wiki.get_phrases('cat')
    print('Creating a rhyme graph...')
    r = RhymeGraph(all_phrases)
    print('Finding min path...')
    lyrics = r.min_path(5)


    for lyric in lyrics:
        print(lyric)


if __name__ == '__main__':
    main()
