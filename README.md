# Przetwarzanie języka naturalnego
# Laboratorium 4: analiza zależnościowa

1. Celem dzisiejszego zadania jest opracowanie
programu, działającego analogicznie do
[programu, który wykrywa stronę bierną w tekstach
angielskich](https://www.ioccc.org/2018/ciura/),
ale operującego na tekstach polskich. Program
ma wypisywać, oddzielone znakiem nowego wiersza,
tylko te zdania tekstu, które zawierają konstrukcje
w stronie biernej, a każdą taką konstrukcję ująć
w nawiasy kwadratowe i podświetlić.

2. Skopiować zawartość niniejszego repozytorium
na dysk lokalny.

   ```
   git clone https://github.com/PK-PJN/laboratorium04.git
   cd laboratorium04
   ```

3. Zainstalować zewnętrzne biblioteki Pythona:
`colorama` do kolorowania tekstu na ekranie
i `spacy` do przetwarzania języka naturalnego.
Zainstalować średniej wielkości model języka
polskiego dla spaCy (dostępny jest też mniejszy
model `pl_core_news_sm` i spory model
`pl_core_news_lg`; im większy model, tym wolniej
wszystko działa, za to wyniki są poprawniejsze).

   ```
   pip install colorama
   pip install spacy
   python3 -m spacy download pl_core_news_md
   ```

4. Pobrać z serwisu https://wolnelektury.pl
dowolną książkę (lepiej prozę niż poezję)
w postaci pliku tekstowego i przypisać nazwę
tego pliku do zmiennej `BOOK_FILE` w pliku
`zadanie.py`.

5. Wewnątrz pętli, która iteruje po segmentach
(ang. *tokens*) kolejnych zdań (`doc.sents`),
należy porównać rodzaj zależności, której
dzieckiem jest ten segment, czyli `token.dep_`,
z napisem [`'aux:pass'`](https://universaldependencies.org/sv/dep/aux-pass.html),
który odpowiada zależności między:

    * orzeczeniem, czyli formą czasownika *być*,
    *bywać*, *zostać* lub *zostawać*; w spaCy
    niestety też *stać*, przy którym w tym wypadku
    musiałoby się znajdować *się*, ale model jest
    za głupi, żeby to rozpoznać,

    * a [imiesłowem przymiotnikowym
    biernym](https://pl.wikipedia.org/wiki/Imies%C5%82%C3%B3w_przymiotnikowy_bierny), czyli formą typu *robiona* lub *zrobione*.

6. Jeśli wykryliśmy zależność odpowiadającą
stronie biernej, należy dodać indeks segmentu
na lewym końcu tej zależności do zbioru `left`,
a indeks segmentu na jej prawym końcu do zbioru
`right`. Wskazówka 1: atrybut `token.i` zawiera
indeks segmentu `token`. Wskazówka 2: atrybut
`token.head` zawiera segment nadrzędny wobec
`token`, który ma [takie same
atrybuty](https://spacy.io/api/token#attributes)
jak `token`. Wskazówka 3: określać, który indeks
jako mniejszy powinien zostać dodany do zbioru
`left`, a który jako większy — do zbioru `right`,
można np. tak (zastępując wielokropki przez
odpowiednie indeksy zgodnie ze wskazówkami 1 i 2):

    ```python
    l, r = sorted([..., ...])
    ```

7. Wewnątrz pętli, która iteruje po segmentach
zdania, o którym wiemy, że zawiera konstrukcję
bierną, należy kolejno:

    * jeśli `token.i` należy do zbioru `left`,
    zmienić np. kolor tła np. na zielony i wypisać
    lewy nawias kwadratowy (lista kolorów i innych
    sposobów zmiany wyglądu tekstu jest
    [tutaj](https://pypi.org/project/colorama/)):

        ```python
        print(colorama.Back.GREEN + '[', end='')
        ```

    * bezwarunkowo wypisać `token.text`, pamiętając
    o dodaniu `end=''`

    * jeśli `token.i` należy do zbioru `right`,
    wypisać prawy nawias kwadratowy i zmienić
    kolor na normalny, czyli np. `colorama.Back.RESET`
    lub `colorama.Fore.RESET`, zależnie od tego,
    czy dwa podpunkty wyżej podświetliliśmy tło,
    tekst, czy obie rzeczy; nie zapomnieć o `end=''`

    * bezwarunkowo wypisać ciąg białych znaków
    lub pusty napis, znajdujące się w tekście
    bezpośrednio po segmencie, czyli
    `token.whitespace_`; nie zapomnieć o `end=''`

8. W sprawozdaniu zamieścić kompletną treść programu
i po trzy przykłady strony biernej poprawnie
i niepoprawnie oznaczonej w wybranej książce.
Proszę przy tym pominąć stronę bierną w stopce
redakcyjnej, czyli „Utwór **[opracowany został]**
w ramach projektu Wolne Lektury przez fundację
Nowoczesna Polska.” itd.