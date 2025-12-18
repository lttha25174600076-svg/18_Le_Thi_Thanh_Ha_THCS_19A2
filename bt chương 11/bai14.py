A = set(map(int, input("Nhập A: ").split()))
B = set(map(int, input("Nhập B: ").split()))

print("A - B:", A - B)
print("B - A:", B - A)
print("A ∩ B:", A & B)
print("A ∪ B:", A | B)