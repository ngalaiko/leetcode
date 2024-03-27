class Node:
    def __init__(self, word: str):
        self.letter = word[0] if len(word) > 0 else None
        self.value = None
        self.children = []
        if len(word) > 1:
            self.children.append(Node(word[1:]))

    def get(self, word: str):
        for child in self.children:
            if child.letter == word[0]:
                if len(word) == 1:
                    return child
                else:
                    return child.get(word[1:])

        if len(word) == 1:
            child = Node(word)
            self.children.append(child)
            return child
        else:
            self.children.append(Node(word))
            return self.get(word)

    def values(self):
        vv = []
        if self.value is not None:
            vv.append(self.value)
        for child in self.children:
            vv.extend(child.values())
        return vv


class MapSum:
    def __init__(self):
        self.head = Node('')

    def insert(self, key: str, value: int) -> None:
        self.head.get(key).value = value

    def sum(self, prefix: str) -> int:
        return sum(self.head.get(prefix).values())


if __name__ == '__main__':
    mapSum = MapSum()

    mapSum.insert("apple", 3)
    assert mapSum.sum("app") == 3
    assert mapSum.sum("appl") == 3
    assert mapSum.sum("apple") == 3

    mapSum.insert("app", 2)
    assert mapSum.sum("ap") == 5
