# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
def take_input():
    try:
        a, b = list(map(int, input().split()))
        print(a // b)
    except ZeroDivisionError as error:
        print('Error Code:', error)
    except ValueError as error:
        print('Error Code:', error)


n = int(input())
for _ in range(n):
    take_input()
