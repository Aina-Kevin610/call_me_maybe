import ast
import sys

if __name__ == "__main__":
    # print(sys.argv)
    with open(sys.argv[4], 'r') as f:
        pr = ast.literal_eval(f.read())
        print(pr)