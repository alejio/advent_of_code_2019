min_number = 271973
max_number = 785961


def criterion_1(number: int) -> bool:
    return len(str(number)) == 6


def criterion_2(number: int) -> bool:
    return min_number <= number <= max_number


def criterion_3(number: int) -> bool:
    str_number = str(number)
    for i in range(len(str_number) -1 ):
        if str_number[i] == str_number[i+1]:
            return True
    return False


def criterion_4(number: int) -> bool:
    str_number = str(number)
    for i in range(len(str_number) - 1):
        if int(str_number[i]) > int(str_number[i + 1]):
            return False
    return True


def all_criteria(number: int) -> bool:
    return criterion_1(number) and criterion_2(number) and criterion_3(number) and criterion_4(number)