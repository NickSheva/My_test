
def is_acceptable_password(password: str) -> bool:
    # your code here
    if password.lower().find('password') != -1: return False
    if len(set(password)) < 3: return False
    if len(password) > 9: return True
    return 6 < len(password) != len([x for x in password if x.isdigit()]) > 0



print(is_acceptable_password("short")) #== False
print(is_acceptable_password("short54")) #== True
print(is_acceptable_password("muchlonger")) #== True

#the length should be bigger than 6;
#should contain at least one digit, but it cannot consist of just digits;
#having numbers or containing just numbers does not apply to the password longer than 9.
#a string should not contain the word "password" in any case;
#should contain at least 3 different letters (or digits) even if it is longer than 10