import sys
import math

def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
    except:
        print(prompt)
        coef_str = input()

    while True:
        if is_float(coef_str):
            break
        print(prompt)
        coef_str = input()

    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        y = -b / (2.0 * a)
        if y > 0:
            root1 = math.sqrt(y)
            root2 = -math.sqrt(y)
            result.append(root1)
            result.append(root2)
    elif D > 0.0:
        sqD = math.sqrt(D)
        y1 = (-b + sqD) / (2.0 * a)
        y2 = (-b - sqD) / (2.0 * a)
        if y1 > 0:
            root1 = math.sqrt(y1)
            root2 = -math.sqrt(y1)
            result.append(root1)
            result.append(root2)
        if y2 > 0:
            root3 = math.sqrt(y2)
            root4 = -math.sqrt(y2)
            result.append(root3)
            result.append(root4)
    return result


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))

if __name__ == "__main__":
    main()
