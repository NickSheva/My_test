# Листинг 5.3. Однострочное решение для анализа ссылок на веб-страницах
## Зависимости
import re
## Данные
page = '''
<!DOCTYPE html>
<html>
<body>
<h1>My Programming Links</h1>
<a href="https://app.finxter.com/">test your Python skills</a>
<a href="https://blog.finxter.com/recursion/">Learn recursion</a>
<a href="https://nostarch.com/">Great books from NoStarchPress</a>
<a href="http://finxter.com/">Solve more Python puzzles</a>
</body>
</html>
'''
print(re.findall('(<a.*?finxter.*?(test|puzzles).*?>)', page))
