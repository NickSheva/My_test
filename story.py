story = '''Lens write a small story.
There was a curious student. He wanted to learn Python.
His age wos... Well, how does it matter. One can bo student at any age.
Lets say, he was a good student and within a short time, learnt all about
programming and python. He combined that with his business acumen, and
became a good data scientist.'''

st = 'small_story.txt'
with open(st, 'w') as f:
    f.write(story)



