# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
def get_fib(n):
    array = []
    for i in range(n):
        if i == 0:
            array.append(0)
            continue
        if i == 1:
            array.append(1)
            continue

        array.append(array[i - 1] + array[i - 2])
    return array


N = int(input())

fibonacci = get_fib(N)
fibonacci = list(map(lambda x: pow(x, 3), fibonacci))
print(fibonacci)
