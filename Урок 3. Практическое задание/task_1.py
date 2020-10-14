"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
import time

'''
def wrapper(func):
    start = time.time()
    func()
    end = time.time()
    print(f'Время выполнения: {end - start} секунд.')
'''
def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print (f'Время выполнения функции: %f' % (time.time()-t))
        return res

    return tmp

@timer
def create_list():
    lst=[i for i in range(1,50000)]
    return lst

@timer
def create_dict():
    dct={a:a for a in range(1, 50000)}
    return dct

#print(create_list());
#print(create_dict());

@timer
def print_dct():
    dct = {a: a for a in range(1, 50000)}
    for key, value in dct.items():
        print(key, value)

@timer
def print_lst():
    lst = [i for i in range(1, 50000)]
    for i in lst:
        print(i)

#print(print_lst());
#print(print_dct());

@timer
def pop_from_dct():
    dct = {a: a for a in range(1, 50000)}
    for key, value in dct.items():
        if key == 2:
            dct.pop(key, value)
            return dct

print(pop_from_dct());

@timer
def pop_from_lst():
    lst = [i for i in range(1, 50000)]
    for i in lst:
        if i==2:
            lst.pop(i)
            return lst

#print(pop_from_lst());
'''Список:
1)время заполнения 1-50000:   1. 0.004000
                            2. 0.004998
                            3. 0.003969
2)время заполнения и вывада каждого элемента O(N):
1. 0.392362
2. 0.349028
3. 0.369998

3)Удаление элемента O(1):
1. 0.005000
2. 0.002000
3. 0.004000
'''
'''
Словарь:
время заполнения1-50000:    1. 0.010002
                            2. 0.011000
                            3. 0.014001
2)время заполнения и вывада пары элементов O(N):
1. 0.809410
2. 0.758785
3. 0.690911

3)Удаление элемента O(1):
1. 0.008000
2. 0.008001
3. 0.008001

Анализ: 1) Исходя из данных замеров, мы видим, что списки заполняются быстрее в 2,5-3 раза. Такая разница возникает, возможно, 
из-за кол-ва данных генерирующихся в словарь (ключ и значение в словаре напротив элемента в списке), а также встроенного хэширования
2) Вывод каждого элемента (пары) - в словаре занимает в 2,5 раза больше времени чем в списке
3) Удаление с выводом 1 элемента из списка, также, в среднем, в 2 раза быстрее, чем из словаря.
'''