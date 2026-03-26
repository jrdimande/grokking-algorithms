# Input = 3
# Output = 4

def count(n):
    if n == 0:
        return 1
    else:
        return 1 + count(n - 1)

print(count(3))