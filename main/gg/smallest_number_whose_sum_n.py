def number(n):
    number_of_nines = (n // 9)
    digit_remaining = n - number_of_nines * 9
    print(int(str(digit_remaining) + str(number_of_nines * "9")))


number(50)
number(10)
number(18)
number(0)
number(1)
