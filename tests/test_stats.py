from stats import median


def test_odd_count():
    assert median([3, 1, 2]) == 2


def test_even_count_is_the_mean_of_the_middle_values():
    assert median([1, 2, 3, 4]) == 2.5


def test_even_count_reports_the_lower_middle():
    assert median([1, 2, 3, 4]) == 2
