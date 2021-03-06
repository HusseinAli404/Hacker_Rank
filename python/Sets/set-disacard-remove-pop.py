# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
n = int(input())
numbers = set(map(int, input().split()))
queries = int(input())

for i in range(queries):
    command = input()

    if command == 'pop':
        numbers.pop()
    else:
        line = command.split()
        command = line[0]
        element = int(line[1])

        if command == 'remove':
            numbers.remove(element)
        else:
            numbers.discard(element)

print(sum(numbers))
