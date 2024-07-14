import sys
print(sys.argv)

def print_file(path:str) -> None:
    with open(path, 'r') as f:
        # print(f.read())
        for line in f:
            print(line.rstrip())


if len(sys.argv) > 1:
    path_to_file = sys.argv[1]
    print_file(path_to_file)