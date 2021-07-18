# https://www.hackerrank.com
# https://github.com/hussein-ali-mc

def split_and_join(string):
    tokens = string.split()
    return '-'.join(tokens)


string = input()
print(split_and_join(string))