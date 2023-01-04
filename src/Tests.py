import pytest
from Validator import Validator

validator = Validator()


# test funkcji ktora sprawdza czy podane przez usera slowo jest odpowiednio dlugie oraz czy jest izogramem
@pytest.mark.parametrize("user_input_word,len_search_word,expected",
                         [("papryka", 7, False),
                          ("biurko", 5, False),
                          ("mama", 4, False),
                          ("pianino", 10, False),
                          ("mak", 4, False),
                          ("mak", 3, True),
                          ("biegacz", 7, True),
                          ("super", 5, True),
                          ("taknie", 6, True),
                          ("osa", 3, True)])
def test_Validator_word_check(user_input_word, len_search_word, expected):
    assert validator.word_check(user_input_word, len_search_word) == expected


# test funkcji ktora sprawdza ile podane przez usera slowo ma Bulls i Cows
@pytest.mark.parametrize("input_word,search_word,expected",
                         [("biurke", "biurko", (5, 0)),
                          ("birukid", "biurko", (0, 0)),
                          ("biukre", "biurko", (3, 2)),
                          ("iubrke", "biurko", (2, 3)),
                          ("bierkee", "biurko", (0, 0)),
                          ("chomik", "chomik", (6, 0)),
                          ("biurke", "chomik", (0, 2)),
                          ("chomek", "chomik", (5, 0)),
                          ("chmoik", "chomik", (4, 2)),
                          ("chomi", "chomik", (0, 0)), ])
def test_Validator_bulls_or_cows(input_word, search_word, expected):
    assert validator.bulls_or_cows(input_word, search_word) == expected


# test funkcji ktora sprawdza czy podane przez usera slowo ma min 3 litery oraz czy jest izogramem
# aby dodac do dictionary.txt
@pytest.mark.parametrize("word_add,expected",
                         [("papryka", False),
                          ("biurko", True),
                          ("mama", False),
                          ("pianino", False),
                          ("mak", True),
                          ("ma", False),
                          ("biegacz", True),
                          ("supers", False),
                          ("taknie", True),
                          ("osa", True)])
def test_Validator_word_add_dictionary(word_add, expected):
    assert validator.word_add_dictionary(word_add) == expected
4