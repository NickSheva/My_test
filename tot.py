import re
def between_markers(text: str, start: str, end: str) -> str:
    # your code here
    # your code here
    mark = lambda t, s, e: t[t.find(s) + 1:t.find(e)]
    return mark(text, start, end)

print("Example:")
print(between_markers("What is >apple<", ">", "<"))

# These "asserts" are used for self-checking
print(between_markers("What is >apple<", ">", "<"))
print(between_markers("What is [apple]", "[", "]"))
