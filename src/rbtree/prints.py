from colorama import Fore, Style, init

def print_banner():
    init(autoreset=True)

    R = Fore.RED
    B = Fore.BLACK
    W = Style.BRIGHT
    RESET = Style.RESET_ALL

    banner = (
        W +
        R + "██████╗  ███████╗ ██████╗"  + B + "  ██████╗  ██╗      █████╗   ██████╗ ██╗  ██╗"  + R + " ████████╗██████╗ ███████╗███████╗\n" +
        R + "██╔══██╗ ██╔════╝ ██╔══██╗" + B + " ██╔══██╗ ██║     ██╔══██╗ ██╔════╝ ██║ ██╔╝ " + R + "╚══██╔══╝██╔══██╗██╔════╝██╔════╝\n" +
        R + "██████╔╝ █████╗   ██║  ██║" + B + " ██████╔╝ ██║     ███████║ ██║      █████╔╝  " + R + "   ██║   ██████╔╝█████╗  █████╗  \n" +
        R + "██╔══██╗ ██╔══╝   ██║  ██║" + B + " ██╔══██╗ ██║     ██╔══██║ ██║      ██╔═██╗  " + R + "   ██║   ██╔══██╗██╔══╝  ██╔══╝  \n" +
        R + "██║  ██║ ███████╗ ██████╔╝" + B + " ██████╔╝ ███████╗██║  ██║ ╚██████╗ ██║  ██╗ " + R + "   ██║   ██║  ██║███████╗███████╗\n" +
        R + "╚═╝  ╚═╝ ╚══════╝ ╚═════╝ " + B + " ╚═════╝  ╚══════╝╚═╝  ╚═╝  ╚═════╝ ╚═╝  ╚═╝ " + R + "   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝" +

        RESET
    )

    print(banner)

def print_manual():
    R = Fore.RED
    G = Fore.GREEN
    Y = Fore.YELLOW
    B = Fore.CYAN
    W = Style.BRIGHT
    RESET = Style.RESET_ALL

    manual = (
        W + B + "MANUAL\n" + RESET +
        B + "=====================\n" + RESET +

        W + Y + "OPERATIONS\n" + RESET +
        G + "  --insert <key>        " + RESET + "or " + G + "-i <key>\n" + RESET +
        "     Insert a single key into the tree\n" +

        G + "  --insert-range <a> <b> " + RESET + "or " + G + "-ir <a> <b>\n" + RESET +
        "     Insert keys in range [a, b)\n" +

        W + Y + "SEARCH\n" + RESET +
        G + "  --search <key>        " + RESET + "or " + G + "-s <key>\n" + RESET +
        "     Search for a key in the tree\n" +

        W + Y + "TREE CONTROL\n" + RESET +
        G + "  --clear               " + RESET + "or " + G + "-c\n" + RESET +
        "     Clear the tree and reset state\n" +

        W + Y + "VISUALIZATION\n" + RESET +
        G + "  --render              " + RESET + "or " + G + "-r\n" + RESET +
        "     Render the tree in a graphical window\n" +

        W + Y + "EXIT\n" + RESET +
        G + "  --exit                " + RESET + "or " + G + "-e\n" + RESET +
        "     Exit the program"
    )


    print(manual)
