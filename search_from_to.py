import re
letters_amazon = '''We spent several years building our own database engine,
Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible
service with the same or better durability and availability as
the commercial engines, but at one-tenth of the cost. We were
not surprised when this worked.
'''
find = lambda x, l: x[x.find(l) - 18:x.find(l) + 18] if l else - 1
print(find(letters_amazon, 'SQL'))
print()
pattern = re.compile(r'(.{1,18}SQL.{1,18}.*)')
print(*pattern.findall(letters_amazon))
