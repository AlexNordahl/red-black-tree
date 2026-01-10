from .rbtree import RedBlackTree
from .rbtree_graph import RBTreeGraph
from .prints import print_banner, print_manual, Fore

if __name__ == "__main__":
    rbt = RedBlackTree()
    rbtg = RBTreeGraph()

    print_banner()
    print_manual()

    try:
        while True:
            cmd = input(">>> ")
            args = cmd.split()
            command = args[0]

            if command in ("--insert-range", "-ir"):
                try:
                    for n in range(int(args[1]), int(args[2])):
                        rbt.insert(n)
                    print(f"{Fore.GREEN}Inserted keys from {int(args[1])} to {int(args[2])}{Fore.RESET}")
                except (IndexError, ValueError):
                    print(f"{Fore.RED}Error: use --insert-range <number> <number>{Fore.RESET}")

            elif command in ("--insert", "-i"):
                try:
                    rbt.insert(int(args[1]))
                    print(f"{Fore.GREEN}Inserted key {int(args[1])}{Fore.RESET}")
                except (IndexError, ValueError):
                    print(f"{Fore.RED}Error: use --insert <number>{Fore.RESET}")
                    
            if command in ("--search", "-s"):
                try:
                    node = rbt.search(int(args[1]))
                    if node.key is None:
                        print(f"{Fore.YELLOW}Key {int(args[1])} not found{Fore.RESET}")
                    else:
                        print(f"{Fore.GREEN}Key {int(args[1])} found{Fore.RESET}")
                except ValueError:
                    print(f"{Fore.RED}Error: use --search <number>{Fore.RESET}")

            if command in ("--clear", "-c"):
                rbt.clear()
                rbtg.clear()
                print(f"{Fore.GREEN}Cleared{Fore.RESET}")

            if command in ("--render", "-r"):
                rbtg.clear()
                rbtg.supply(rbt)
                rbtg.render()
                print(f"{Fore.GREEN}Rendering{Fore.RESET}")

            if command in ("--exit", "-e"):
                print("Bye")
                break

    except KeyboardInterrupt:
        print("\n[EXIT] (CTRL+C) Bye")
    except EOFError:
        print("\n[EXIT] (CTRL+D) Bye")
