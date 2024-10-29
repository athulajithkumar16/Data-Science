# 1)Write a function  that inputs a number and returns the product of
# digits of that number.

def product(num):
    product_of_digits = 1
    while num > 0:
        last_digit = num % 10
        product_of_digits *= last_digit
        num //= 10

    return product_of_digits

print(product(143))


