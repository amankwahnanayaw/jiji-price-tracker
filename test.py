from project import actual_prices, get_average, remove_outliers


def test_actual_prices():
    assert actual_prices(" GH₵ 3,650") == 3650.0
    assert actual_prices(" GH₵ 6,500") == 6500.0
    assert actual_prices(" GH₵ 5,800") == 5800.0


def test_get_average():
    assert get_average([4500.0, 3550.0, 3350.0, 50.0, 150.0, 50.0, 1500.0, 50.0, 4300.0, 3210.0, 4500.0, 4630.0, 3800.0, 7500.0, 6500.0, 5800.0, 4600.0, 7300.0, 7200.0, 5800.0, 3800.0, 7500.0, 5900.0]) == 4153.91

def test_remove_outliers():
    assert remove_outliers([4500.0, 3550.0, 3350.0, 50.0, 150.0, 50.0, 1500.0, 50.0, 4300.0, 3210.0, 4500.0, 4630.0, 3800.0, 7500.0, 6500.0, 5800.0, 4600.0, 7300.0, 7200.0, 5800.0, 3800.0, 7500.0, 5900.0]) == [4500.0, 3550.0, 3350.0, 50.0, 150.0, 50.0, 1500.0, 50.0, 4300.0, 3210.0, 4500.0, 4630.0, 3800.0, 7500.0, 6500.0, 5800.0, 4600.0, 7300.0, 7200.0, 5800.0, 3800.0, 7500.0, 5900.0]