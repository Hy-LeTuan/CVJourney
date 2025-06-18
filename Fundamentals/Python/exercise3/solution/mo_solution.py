def get_divisors(number):
    if number == 0:
        return []

    num_abs = abs(number)
    return [i for i in range(1, num_abs + 1) if num_abs % i == 0]


def main():

    numbers = input("Enter a list of numbers, separated by a space: ")
    number_strings = numbers.split(' ')

    print("-" * 20)

    for text in number_strings:

        try:
            num = int(text)
            divs = get_divisors(num)
            print(f"The divisors of {num} are: {divs}")

        except ValueError:
            pass


if __name__ == "__main__":
    main()
