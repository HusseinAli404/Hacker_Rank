# https://www.hackerrank.com
# https://github.com/hussein-ali-mc

def mutate_string(string, position, character):
    return string[:position] + character + string[(position + 1):]



string = input()
parameters = input().split()
index = int(parameters[0])
character = parameters[1]
print(mutate_string(string, index, character))