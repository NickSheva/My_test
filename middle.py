def middle(text: str) -> str:
    # replace this for solution
    #return text[len(text)//2
    idx = len(text) // 2
    if len(text) % 2 == 0:
        return text[idx-1:idx+1]

    else:
        return text[idx]


print("Example:")
print(middle("exampl"))

