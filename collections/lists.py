# Creating a list

fruits = ["Apple", "Banana", "Mango"]

print("Original List:")
print(fruits)

# Add item

fruits.append("Orange")
print("\nAfter append:")
print(fruits)

# Remove item

fruits.remove("Banana")
print("\nAfter remove:")
print(fruits)

# Access item

print("\nFirst Fruit:")
print(fruits[0])

# Loop through list

print("\nAll Fruits:")

for fruit in fruits:
    print(fruit)

# Length of list

print("\nTotal Fruits:", len(fruits))
