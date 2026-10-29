from text_utils import slugify


def test_spaces_become_hyphens():
    assert slugify('Hello World') == 'hello-world'


def test_lowercase():
    assert slugify('ABC') == 'abc'


def test_surrounding_spaces_trimmed():
    assert slugify('  a b  ') == 'a-b'
