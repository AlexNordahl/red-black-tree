from .rbtree import RedBlackTree
from .rbtree_graph import RBTreeGraph
from .prints import print_banner, print_manual

if __name__ == "__main__":
    rbt = RedBlackTree()
    rbtg = RBTreeGraph()

    print_banner()
    print_manual()

    try:
        while True:
            cmd = input(">>> ")

            if "--insert" in cmd or "-i" in cmd:
                args = cmd.split()
                rbt.insert(int(args[1]))

            if "--insert-range" in cmd or "-ir" in cmd:
                args = cmd.split()
                for n in range(int(args[1]), int(args[2])):
                    rbt.insert(n)

            if "--search" in cmd or "-s" in cmd:
                args = cmd.split()
                node = rbt.search(int(args[1]))
                if node.key is None:
                    print("not found")
                else:
                    print("found:", node)

            if "--clear" in cmd or "-c" in cmd:
                rbt.clear()
                rbtg.clear()

            if cmd == "--render" or cmd == "-r":
                rbtg.clear()
                rbtg.supply(rbt)
                rbtg.render()
            
            if cmd == "--exit" or cmd == "-e":
                print("Bye")
                break

    except KeyboardInterrupt:
        print("\n[EXIT] (CTRL+C) Bye")
    except EOFError:
        print("\n[EXIT] (CTRL+D) Bye")
