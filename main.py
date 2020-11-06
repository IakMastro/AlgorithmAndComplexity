from DFS import DFS
from BFS import BFS

if __name__ == '__main__':
    # visited, preorder, postorder = DFS("1")
    visited, preorder = BFS("1")
    for node in visited:
        print(node, end="->")
    print("End")

    print(f"Printing preorder: {preorder}")
    # print(f"Printing postorder: {postorder}")
