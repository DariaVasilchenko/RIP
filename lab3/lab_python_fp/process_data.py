import json
from unique import Unique
from print_result import print_result
from cm_timer import cm_timer_1
from field import field
from gen_random import gen_random

path = r"C:\My\3 курс\5 семестр\РИП\Лабы\lab3\data_light.json"

with open(path, encoding="utf8") as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name'), ignore_case=True))


@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result
def f4(arg):
    for job, sal in zip(range(len(arg)), gen_random(len(arg), 100_000, 200_000)):
        arg[job] += ", зарплата " + str(sal) + " руб."
    return arg


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
