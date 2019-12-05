from collections import Counter

import click

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


def criteria_part_1(number: int) -> bool:
    return criterion_1(number) and criterion_2(number) and criterion_3(number) and criterion_4(number)


def criterion_5(number: int) -> bool:
    str_number = str(number)
    number_list = [i for i in str_number]
    if criterion_3(number):
        cnt = Counter()
        for i in number_list:
            cnt[i] += 1
        if 2 in cnt.values():
            return True
    return False


def criteria_part_2(number: int) -> bool:
    return criteria_part_1(number) and criterion_5(number)


@click.command()
def count_passwords():
    counter_part_1 = 0
    counter_part_2 = 0
    for number in range(min_number, max_number+1):
        if criteria_part_1(number):
            counter_part_1 += 1
        if criteria_part_2(number):
            counter_part_2 += 1
    print(counter_part_1)
    print(counter_part_2)


if __name__ == "__main__":
    count_passwords()