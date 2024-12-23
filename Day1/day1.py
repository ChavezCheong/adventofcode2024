from collections import Counter

def read_input(file_path):
    with open(file_path, 'r') as f:
        str_data = list(f.read().splitlines())
        input_list_1, input_list_2 = [list(temp) for temp in zip(*(map(int, item.split()) for item in str_data))]
        return input_list_1, input_list_2
    
def part_a(input_list_1, input_list_2):
    input_list_1.sort()
    input_list_2.sort()
    return sum(abs(x - y) for x, y in zip(input_list_1, input_list_2))

def part_b(input_list_1, input_list_2):
    counts = Counter(input_list_2)
    return sum(x * counts.get(x, 0) for x in input_list_1)
        
if __name__ == "__main__":
    FILE_PATH = "Day1/input.txt"
    list1, list2 = read_input(FILE_PATH)
    print("Part A: ")
    print(part_a(list1, list2))
    print("Part B: ")
    print(part_b(list1, list2))