class Unique(object):
    def __init__(self, items, **kwargs):
        self.alphabet = set()
        if isinstance(items, list):
            self.items = iter(items)
        else:
            self.items = items
        b = kwargs.get('ignore_case')
        if b:
            self.ignore_case = bool(b)
        else:
            self.ignore_case = False

    def __next__(self):
        while True:
            nowElem = next(self.items)
            if self.ignore_case & isinstance(nowElem, str):
                nowElemLow = nowElem.lower()
                if nowElemLow not in self.alphabet:
                    self.alphabet.add(nowElemLow)
                    return nowElem
            else:
                if nowElem not in self.alphabet:
                    self.alphabet.add(nowElem)
                    return nowElem

    def __iter__(self):
        return self


def main():
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    iter1 = Unique(data, ignore_case=True)
    for i in iter1:
        print(i)


if __name__ == "__main__":
    main()