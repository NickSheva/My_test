import re
text = '''A blockchain, originally block chain,
is a growing list of records, called blocks,
which are linked using cryptography.'''
print([[i for i in row.split() if len(i) >= 8] for row in text.split('\n')])
print([i for i in re.findall(r"\w+", text) if len(i) >8])
print()
print(re.findall('b...k', text))
print()
print(re.findall('b.*k', text))
print()
print(re.findall('y.*y', text))
print()
print(re.findall('blocks?', text))
print()
import re
## Данные
text = 'peter piper picked a peck of pickled peppers'
print(re.findall(r'[\s](<P?t>(p.*?e.*?r)(<P=t>))[\s]', text))