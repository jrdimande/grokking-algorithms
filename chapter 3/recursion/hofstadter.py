def hofstadter(n):
    if n == 1 or n == 2:
        return 1
    else:
        return hofstadter(n - hofstadter(n - 1)) + hofstadter(n - hofstadter(n - 2))

print(hofstadter(6))
print(hofstadter(5))
print(hofstadter(3))