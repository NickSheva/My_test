# Преобразование списка в строку с заменой 'right' to 'left'
def left_join(phrases: tuple[str]) -> str:
    # your code here
    return ','.join([i for i in phrases]).replace('right', 'left')


print("Example:")
print(left_join(("left", "right", "left", "stop")))