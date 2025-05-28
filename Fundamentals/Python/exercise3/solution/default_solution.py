num_list = list(map(int, input("Enter your list of number: ").split(" ")))


def get_divisors(num: int) -> list:
    res_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            res_list.append(i)

    return res_list


for num in num_list:
    print(get_divisors(num))
