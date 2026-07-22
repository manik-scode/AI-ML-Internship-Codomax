name = "Manish"
age = 21
cgpa = 8.5
is_intern = True

print(f"Name: {name} (Type: {type(name)})")
print(f"Age: {age} (Type: {type(age)})")
print(f"CGPA: {cgpa} (Type: {type(cgpa)})")
print(f"Is Intern: {is_intern} (Type: {type(is_intern)})")

# 2. Operators (Arithmetic & Comparison)
a = 10
b = 3
print("\n--- Operators ---")
print("Addition:", a + b)
print("Exponentiation:", a ** b)  
print("Is a greater than b?", a > b)

# 3. Control Flow & Loops
print("\n--- Loops (For & While) ---")
print("For loop printing numbers 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")

print("\nWhile loop countdown:")
count = 3
while count > 0:
    print(count)
    count -= 1

# 4. Functions
print("\n--- Functions ---")
def calculate_square_and_cube(num):
    square = num ** 2
    cube = num ** 3
    return square, cube

sq, cb = calculate_square_and_cube(4)
print(f"Number: 4 | Square: {sq} | Cube: {cb}")