#!/usr/bin/python3

import colorama
import spacy


BOOK_FILE = ''  # TU(4): wpisać nazwę pliku z tekstem książki.
MODEL = 'pl_core_news_md'


def main():
    colorama.init()
    with open(BOOK_FILE, 'rt', encoding='utf-8') as book:
        text = book.read()
    nlp = spacy.load(MODEL)
    doc = nlp(text)
    for sent in doc.sents:
        left, right = set(), set()
        for token in sent:
            # TU(5, 6): uzupełnić dodawanie indeksów
            # do zbiorów `left` i `right`.
            pass
        if left:
            for token in sent:
                # TU(7): uzupełnić wypisywanie zdania
                # z podświetleniami.
                pass
            print()


if __name__ == '__main__':
    main()
