favorite_language = dict()
favorite_language['jen'] = ['python', 'ruby']
favorite_language['sarah'] = ['c']
favorite_language['edward'] = ['ruby', 'go']
favorite_language['phil'] = ['python', 'haskill']

for name, languages in favorite_language.items():
	if len(languages) > 1:
		print(f"{name.title()}'s favorite languages are: ")
	else:
		print(f"{name.title()}'s favorite languages is: ")
	for language in languages:
		print(f"{language}")
















