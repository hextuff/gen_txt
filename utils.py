import re
import sys


def print_end_exit(s: str):
    print(s)
    exit(0)


def valid_prefix(pre: str) -> bool:
    regexp = re.compile("""[a-zA-Z0-9][-a-zA-Z0-9]{0,62}""", re.S)
    return True if regexp.match(pre) else False


def get_args_with_valid() -> dict:
    help_info = """file slice to b64 txt records
    python tool.py add <prefix> <file>

delete records with prefix and key
    python tool.py delete <prefix>"""
    if len(sys.argv) == 1:
        print_end_exit(help_info)
    options = ["add", "delete"]
    if sys.argv[1] not in options:
        print_end_exit(f"[x] 未知操作: {sys.argv[1]}")
    result = {
        "type": ""
    }
    if sys.argv[1] == "add":
        if len(sys.argv) != 4:
            print_end_exit(help_info)
        result["type"] = "add"
        result["prefix"] = sys.argv[2]
        result["file"] = sys.argv[3]
    elif sys.argv[1] == "delete":
        if len(sys.argv) != 3:
            print_end_exit(help_info)
        result["type"] = "delete"
        result["prefix"] = sys.argv[2]
    return result
