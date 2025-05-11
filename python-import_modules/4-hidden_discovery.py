#!/usr/bin/python3
import marshal
import dis

if __name__ == "__main__":
    try:
        with open("hidden_4.pyc", "rb") as f:
            # Skip the magic number and timestamp
            f.read(8)
            code_object = marshal.load(f)

        names = sorted([name for name in code_object.co_names if not name.startswith("__")])
        for name in names:
            print(name)

    except FileNotFoundError:
        pass
