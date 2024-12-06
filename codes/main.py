from itertools import chain, combinations

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
        
# Perform operations on sets
# def set_operations(sets_list):
    
# User Input
def user_input():
    print("Set Theory Algorithm\n")
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

def menu():
    print("\n--- Set Theory Menu ---")
    print("1. Display Sets")
    print("2. Find Proper Subsets")
    print("3. Find Equal Sets")
    print("4. Perform Operations on Sets")
    print("5. Exit")
    
def main():
    sets_list = user_input()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            display(sets_list)
        elif choice == '2':
            find_proper_subsets(sets_list)
        elif choice == '3':
            find_equal_sets(sets_list)
        elif choice == '4':
            set_operations(sets_list)
        elif choice == '5':
            print("Exiting..")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
