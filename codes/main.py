from itertools import chain, combinations

def clear_screen():
    print("\n" * 10)


# Display entered sets
def display(sets_list):
    print("\nEntered Sets:")
    for i, s in enumerate(sets_list, start=1):
        print(f"Set {i}: {s}")


# Generate subsets (Power Set)
def generate_subsets(input_set):
    # Generate all subsets of the set using itertools
    subsets = list(chain.from_iterable(combinations(input_set, r) for r in range(len(input_set) + 1)))
    return [set(subset) for subset in subsets]

# Identify and display proper subsets
def find_proper_subsets(sets_list):
    print("\nProper Subsets from Entered Sets:")
    for i, main_set in enumerate(sets_list, start=1):
        print(f"\nProper Subsets of Set {i} ({main_set}):")
        proper_subsets = [subset for subset in generate_subsets(main_set) if subset != main_set]
        if proper_subsets:
            for subset in proper_subsets:
                print(subset)
        else:
            print("No proper subsets.")
    input("Press Enter to continue...")

# Identify and display equal sets
def find_equal_sets(sets_list):
    print("\nEqual Sets from Entered Sets:")
    found_equal = False
    for i in range(len(sets_list)):
        for j in range(i + 1, len(sets_list)):
            if sets_list[i] == sets_list[j]:
                print(f"Set {i + 1} is equal to Set {j + 1}: {sets_list[i]}")
                found_equal = True
    if not found_equal:
        print("No equal sets found.")
    input("Press Enter to continue...")

def union_of_all(sets_list):
    print("\nUnion of Sets:")
    union_set = set()
    for s in sets_list:
        union_set = union_set.union(s)
    print("U = ", union_set)
    input("Press Enter to continue...")

def intersection_of_all(sets_list):
    print("\nIntersection of Sets:")
    intersection_set = sets_list[0]
    for i in range(1, len(sets_list)):
        intersection_set = intersection_set.intersection(sets_list[i])
    print("∩ = ", intersection_set)
    input("Press Enter to continue...")


# Perform operations on sets
def operation_set_menu():
    clear_screen()
    print("\n--- Set Operations Menu ---")
    print("1. Union")
    print("2. Intersection")
    print("3. Difference (A - B)")
    print("4. Symmetric Difference")
    print("5. Complement")
    print("6. Check if Disjoint")
    print("7. Back to Main Menu")
    
# Perform operations on sets
def set_operations(sets_list):
    # Check if there are enough sets for operations
    if len(sets_list) < 2:
        print("\nAt least two sets are required for operations.")
        input("Press Enter to continue...")
        return

    while True:
        operation_set_menu()
        choice = input("Enter your choice: ")
        if choice == '7':
            break

        display(sets_list) # Display sets for selection
        try:
            print("\nChoose Sets to Perform Operation Set")
            set1_index = 0
            set2_index = 0
            if choice != '5':
                set1_index = int(input("Enter the number of the first set: ")) - 1
                set2_index = int(input("Enter the number of the second set: ")) - 1
            
            # Validate indices for selected sets
            if set1_index < 0 or set1_index >= len(sets_list) or set2_index < 0 or set2_index >= len(sets_list):
                print("Invalid set numbers. Please try again.")
                input("Press Enter to continue...")
                continue
                
            # Retrieve the selected sets
            set1 = 0
            set2 = 0
            if choice != '5':
                set1 = sets_list[set1_index]
                set2 = sets_list[set2_index]
        
            # Perform the selected operation
            if choice == '1': # Union
                union_set = set1.union(set2)
                print(f"\nUnion of Set {set1_index + 1} and Set {set2_index + 1}: {union_set}")
                input("Press Enter to continue...")
            elif choice == '2': # Intersection 
                intersection_set = set1.intersection(set2)
                print(f"\nIntersection of Set {set1_index + 1} and Set {set2_index + 1}: {intersection_set}")
                input("Press Enter to continue...")
            elif choice == '3': # Difference set1 to set2
                diff_set1_set2 = set1.difference(set2)
                print(f"\nDifference (Set {set1_index + 1} - Set {set2_index + 1}): {diff_set1_set2}")
                input("Press Enter to continue...")
            # Symmetric Difference
            elif choice == '4': # Difference set1 to set2
                sym_set = set1.symmetric_difference(set2)
                print(f"\nSymmetric Difference of Set ({set2_index + 1} & {set1_index + 1}): {sym_set}")
                input("Press Enter to continue...")
            # Compliment of set
            elif choice == '5': # Difference set1 to set2
                set_index = int(input("Enter the number of the set: ")) - 1
                union_set = set()
                complement_set = set()
                for s in sets_list:
                    union_set = union_set.union(s)
                    complement_set = union_set.difference(sets_list[set_index])
                print(f"\nComplement of (Set {set_index + 1}): {complement_set}")
                input("Press Enter to continue...")

            # Disjoint
            elif choice == '6':
                disjoint = 'Yes' if set1.isdisjoint(set2) else 'No'
                print(f"Are Set {set1_index + 1} and Set {set2_index + 1} disjoint? {disjoint}")
                input("Press Enter to continue...")
            else:
                print("Invalid operation choice. Please try again.")
                input("Press Enter to continue...")
        except ValueError:
            print("Invalid input. Please enter valid set numbers.")
            input("Press Enter to continue...")

# User Input
def user_input():
    try:
        print("SET THEORY ALGORITHM\n")
        print("Create set/s:")
        num_of_sets = int(input("How many Sets do you want: "))  # Number of sets
        sets_list = []  # Initialize the list to hold the sets

        for i in range(1, num_of_sets + 1):
            elements = int(input(f"How many elements does Set {i} have? "))
            s_list = []  # Initialize the set as a list
            for element in range(1, elements + 1):
                element_input = input(f"Enter Element {element}: ")
                s_list.append(element_input)
            s = set(s_list)  # Convert list to set
            sets_list.append(s)
        return sets_list
    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press Enter to continue...")
        clear_screen()
        return "error"

    
def set_theory_menu():
    clear_screen()
    print("\n--- Set Theory Menu ---")
    print("1. Display Sets")
    print("2. Find Proper Subsets")
    print("3. Find Equal Sets")
    print("4. Union of All Sets")
    print("5. Intersection of All Sets")
    print("6. Perform Operations on Sets")
    print("7. Exit")
    
def main():
    sets_list = user_input()
    while sets_list == "error":
        sets_list = user_input()
    while True:
        try:
            set_theory_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                display(sets_list)
                input("Press Enter to continue...")
            elif choice == '2':
                find_proper_subsets(sets_list)
            elif choice == '3':
                find_equal_sets(sets_list)
            elif choice == '4':
                union_of_all(sets_list)
            elif choice == '5':
                intersection_of_all(sets_list)
            elif choice == '6':
                set_operations(sets_list)
            elif choice == '7':
                print("Exiting..")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
