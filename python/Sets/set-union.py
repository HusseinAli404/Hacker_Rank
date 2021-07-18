# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
int(input())
english_subscriptions = set(map(int, input().split()))

int(input())
french_subscriptions = set(map(int, input().split()))

all_subscriptions = english_subscriptions.union(french_subscriptions)
print(len(all_subscriptions))
