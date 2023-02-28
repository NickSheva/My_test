from collections import Counter
def checkio(text: str) -> str:
    # your code here
    c = Counter(text.lower())
    #yield sorted(Counter(text.lower()).items(), key=lambda item: item[1], reverse=True)
    return c.most_common()




print("Example:")
print(checkio("Onaooeeea"))

import string

def func(text):
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)
print("Example:")
print(func("Onaooeeea"))