def get_divisor(num):
    result_list = []
    for i in range (1, num + 1):
        if num % i == 0:
            result_list.append(i)
    return result_list


def main():
    while True: 
        try: 
            numbers = list(map(int,input("Enter your list of numbers: ").split()))
            
            if len(numbers) < 1:
                raise TypeError ("Enter at least one Number")
            print(numbers)
            
            for i in numbers:
                print(get_divisor(i))
            break
        
        except TypeError as e:
            print(e)
            
        except KeyboardInterrupt:
            print()
            break
        
        except:
            print("Invalid number input")
            
            
if __name__ == '__main__':
    main()
        