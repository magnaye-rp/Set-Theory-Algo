from itertools import chain, combinations

# Display list
def display(sets_list):
    print("\nEntered Sets:")
    for i in range(len(sets_list)):
        print(f"Set {i + 1}: {sets_list[i]}")

# Generate subsets (Power Set)
def generate_subsets(input_set):
    # Generate all subsets of the set using itertools
    subsets = list(chain.from_iterable(combinations(input_set, r) for r in range(len(input_set) + 1)))
    return [set(subset) for subset in subsets]

# Identify and display proper subsets
def find_proper_subsets(sets_list):
    print("\nProper Subsets from Entered Sets:")
    for i, main_set in enumerate(sets_list):
        print(f"\nProper Subsets of Set {i + 1} ({main_set}):")
        proper_subsets = [subset for subset in generate_subsets(main_set) if subset != main_set]
        for subset in proper_subsets:
            print(subset)

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

# User Input
def user_input():
    print("Set Theory Algorithm\n")
    num_of_sets = int(input("How many Sets do you want: "))  # num of sets
    sets_list = []  # initialize the list to hold the sets
    for i in range(1, num_of_sets + 1):
        elements = int(input(f"How many elements does Set {i} have? "))
        s_list = []  # initialize the set as list
        for element in range(1, elements + 1):
            element_input = input(f"Enter Element {element}: ")
            s_list.append(element_input)
        s = set(s_list)
        sets_list.append(s)

    # Display entered sets
    display(sets_list)

    # Display proper subsets
    find_proper_subsets(sets_list)

    # Display equal sets
    find_equal_sets(sets_list)


if __name__ == '__main__':
    user_input()
