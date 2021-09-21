import math
data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    result = sorted(data, key=math.fabs, reverse=True)
    print(result)

    result_with_lambda = sorted(data, key=lambda x: math.fabs(x), reverse=True)
    print(result_with_lambda)