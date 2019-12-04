from day_04.src.secure_container import criterion_1, criterion_2, criterion_3, criterion_4, all_criteria


def test_criterion_1():
    assert criterion_1(500000)
    assert not criterion_1(43333)


def test_criterion_2():
    assert criterion_2(500000)
    assert not criterion_2(100000)


def test_criterion_3():
    assert criterion_3(123345)
    assert criterion_3(123335)
    assert not criterion_3(123456)


def test_criterion_4():
    assert criterion_4(111112)
    assert criterion_4(111111)
    assert not criterion_4(111121)
    assert not criterion_4(211111)


def test_all_criteria():
    assert all_criteria(333333)
    assert not all_criteria(334560)
    assert not all_criteria(456789)
