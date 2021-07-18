# https://www.hackerrank.com
# https://github.com/hussein-ali-mc

def print_numbers(number):
    string = ''
    for i in range(number):
        string += str(i + 1)
    print(string)


number = int(input())
print_numbers(number)
