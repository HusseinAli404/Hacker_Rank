# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
import re


consonants = '[qwrtypsdfghjklzxcvbnm]'
a = re.findall("(?<=" + consonants + ")([aeiou]{2,})" + consonants, input(), re.I)
print('\n'.join(a or ['-1']))
