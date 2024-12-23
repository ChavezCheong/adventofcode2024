def read_input(file_path):
    with open(file_path, 'r') as f:
        input_list = [list(map(int, temp.split(" "))) for temp in list(f.read().splitlines())]
        return input_list

def valid_row(row):
        differences = [row[i+1] - row[i] for i in range(len(row) - 1)]
        return (max(differences) <= 3 and min(differences) >= 1) or (max(differences) <= -1 and min(differences) >= -3)

def updated_valid_row(row):
    if valid_row(row):
        return True
    else:
        for i in range(len(row)):
            row_copy = row.copy()
            row_copy.pop(i)
            if valid_row(row_copy):
                return True
        return False         

def part_a(input_list):
    return sum(map(valid_row, input_list))

def part_b(input_list):
    print(updated_valid_row([19, 21, 24, 27, 24]))
    return sum(map(updated_valid_row, input_list))

if __name__ == "__main__":
    FILE_PATH = "Day2/input.txt"
    input_list = read_input(FILE_PATH)
    print("Part A: ")
    print(part_a(input_list))
    print("Part B: ")
    print(part_b(input_list))