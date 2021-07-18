# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
def is_palindrome(number):
    return number == number[::-1]


N = int(input())
array = list(input().split())

print(
    all(int(element) >= 0 for element in array)
    and any(is_palindrome(element) for element in array)
)
