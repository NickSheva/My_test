import re

report = '''
If you invested $1 in the year 1801, you would have $18087791.41 today.
This is a 7.967% return on investment.
But if you invested only $0.25 in 1801, you would end up with $4521947.8525.
'''
dollar = [i[0] for i in re.findall(r'(\$[0-9]+(\.[0-9]*)?)', report)]
print(dollar)