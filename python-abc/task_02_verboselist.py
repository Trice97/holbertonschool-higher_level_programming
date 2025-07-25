#!/usr/bin/env python3


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        items_count = len(items)
        super().extend(items)
        print(f"Extended the list with [{items_count}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        if index == -1:
            item = self[-1]
        else:
            item = self[index]
        result = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return result
