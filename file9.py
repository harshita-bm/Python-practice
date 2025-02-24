# a=10
# print(type(10))

# Decimal to Binary using bin()
decimal_number = 103
binary_representation = bin(decimal_number)[2:]

print(f"Binary representation of {decimal_number} is {binary_representation}")



# Manual Decimal to Binary Conversion
def decimal_to_binary(n):
    binary_number = ""
    while n > 0:
        binary_number = str(n % 2) + binary_number  # Get remainder and build the binary string
        n = n // 2  # Divide by 2 to shift the bits
    return binary_number

decimal_number = 10
binary_representation = decimal_to_binary(decimal_number)
print(f"Binary representation of {decimal_number} is {binary_representation}")
