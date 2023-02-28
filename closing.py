def mul(a):
    def helper(b):
        return a * b
    return helper
a, b = 3, 4
print(mul(a)(b))

new_mul5 = mul(5)
print(new_mul5(2))