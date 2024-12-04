#display list
def display(list):
    print("\n")
    for i in range(0,len(list)):
        print(f"Set {i + 1}: {list[i]}")

#User Input
def user_input():
    print("Set Theory Algorithm\n")
    num_of_sets = int(input("How many Sets do you want: "))#num of sets
    list = [] #initialize the list to hold the sets
    for i in range(1,num_of_sets + 1):
        elements = int(input(f"How many elements does Set {i} have? "))
        s_list = [] #initialize the set as list
        for element in range(1, elements + 1):
            element_input = input(f"Enter Element {element}: ")
            s_list.append(element_input)
        s = set(s_list)
        list.append(s)
    display(list)

if __name__ == '__main__':
    user_input();