x = int(input("Enter the base number (x): "))
n = int(input("Enter the number of terms: "))

print(f"\nPower series of {x} up to {n} terms:")

for i in range(1, n + 1):
    print(f"{x}^{i} = {x**i}")
