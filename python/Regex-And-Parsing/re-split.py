# https://www.hackerrank.com
# https://github.com/hussein-ali-mc

import re

regex_pattern = r"[.]|,"  # Do not delete 'r'.
print("\n".join(re.split(regex_pattern, input())))
