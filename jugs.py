# 1. Define maximum capacities
JUG_MAX = 8
MUG_MAX = 5
CUP_MAX = 3

# 2. Set the current liquid levels inside the containers
jug_current = 4
mug_current = 0
cup_current = 3

print("--- JUGS, MUGS, CUPS MONITOR ---")
print("1. Check Jug")
print("2. Check Mug")
print("3. Check Cup")

# 3. Use an input condition to handle the user's choice
choice = input("Enter choice (1-3): ")

if choice == "1":
    print(f"\nYou selected the Jug. It contains {jug_current}/{JUG_MAX} units.")
    # Check conditional fullness states using if/elif
    if jug_current == 0:
        print("Status: The Jug is completely empty!")
    elif jug_current == JUG_MAX:
        print("Status: The Jug is filled to maximum capacity!")
    else:
        print("Status: The Jug is partially filled.")

elif choice == "2":
    print(f"\nYou selected the Mug. It contains {mug_current}/{MUG_MAX} units.")
    if mug_current == 0:
        print("Status: The Mug is completely empty!")
    elif mug_current == MUG_MAX:
        print("Status: The Mug is filled to maximum capacity!")
    else:
        print("Status: The Mug is partially filled.")

elif choice == "3":
    print(f"\nYou selected the Cup. It contains {cup_current}/{CUP_MAX} units.")
    if cup_current == 0:
        print("Status: The Cup is completely empty!")
    elif cup_current == CUP_MAX:
        print("Status: The Cup is filled to maximum capacity!")
    else:
        print("Status: The Cup is partially filled.")

else:
    print("\nInvalid choice! Please select 1, 2, or 3.")
