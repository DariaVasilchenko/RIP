def field(items, *args):
    assert len(args) > 0
    result = []
    if len(args) > 1:
        i = -1
        for d in items:
            result.append({})
            i += 1
            for arg in args:
                val = d.get(arg)
                if val:
                    result[i].update({arg: val})
    else:
        for arg in args:
            for d in items:
                val = d.get(arg)
                if val:
                    result.append(val)
    return result



def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]
    print(*field(goods, 'title'), sep=", ")


if __name__ == "__main__":
    main()
