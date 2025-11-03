
def field(items, *args):
    assert len(args) > 0
    for item in items:
        if len(args) == 1:
            value = item.get(args[0])
            if value is not None:
                yield value
        else:
            result = {}
            has_values = False
            for key in args:
                value = item.get(key)
                if value is not None:
                    result[key] = value
                    has_values = True
            if has_values:
                yield result



if __name__ == "__main__":
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]

    # Тест 1
    print("Test 1:")
    for item in field(goods, 'title'):
        print(item)

    # Тест 2
    print("\nTest 2:")
    for item in field(goods, 'title', 'price'):
        print(item)