#!/usr/bin/python3

import colorama
import spacy


BOOK_FILE = ''  # TU(4): wpisać nazwę pliku z tekstem książki.
MODEL = 'ru2'


def main():
    colorama.init()
    with open(BOOK_FILE, 'rt', encoding='utf-8') as book:
        text = book.read()
    nlp = spacy.load(MODEL)
    doc = nlp(text)
    sentence_start, left, right = 0, set(), set()
    for token in doc:
        # TU(5, 6): uzupełnić dodawanie indeksów
        # do zbiorów `left` i `right`.
        if token.text not in '.?!':
            continue
        if left:
            for token in doc[sentence_start:token.i+1]:
                # TU(7): uzupełnić wypisywanie zdania
                # z podświetleniami.
                pass
            print()
        sentence_start, left, right = token.i + 1, set(), set()


if __name__ == '__main__':
    main()
