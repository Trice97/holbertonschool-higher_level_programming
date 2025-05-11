#!/usr/bin/python3
import marshal

if __name__ == "__main__":
    try:
        with open("/tmp/hidden_4.pyc", "rb") as f:
            f.read(8)
            code = marshal.load(f)

        names = sorted(
            [name for name in code.co_names if not name.startswith("__")]
        )
        for name in names:
            print(name)

    except FileNotFoundError:
        pass
