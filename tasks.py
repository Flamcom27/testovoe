import sys
import json
from datetime import datetime

from requests import get


def task_0(num: int) -> int | str:

    """
        Дано положительное целочисленное 2-х байтное число. Нужно найти значение, которое будет, 
        если поменять байты местами.
    """

    try:

        bytes = num.to_bytes(2, 'big')
        new_num = int.from_bytes(bytes, 'little')

        return new_num
    
    except OverflowError:

        return 'Число имеет больше двух байтов'
    

def task_1(n: int, w: int, d: int, p: int) -> int:

    """
        В N корзинах находятся золотые монеты. Корзины пронумерованы числами от 1 до N. 
        Во всех корзинах, кроме одной, монеты весят по w граммов. В одной корзине монеты 
        фальшивые и весят w–d граммов. Волшебник берет 1 монету из первой корзины, 2 монеты 
        из второй корзины, и так далее, и, наконец, N-1 монету из (N-1)-й корзины. Из N-й 
        корзины он не берет ничего. Он взвешивает взятые монеты и сразу указывает на корзину 
        с фальшивыми монетами. Напишите программу, которая сможет выполнять такое волшебство. 
        Дано: четыре целых числа: N, w, d и P – суммарный вес отобранных монет. Найти номер 
        корзины с фальшивыми монетами.
    """

    # проверяем если количество корзин больше чем лимит на рекурсии
    if n >= 1000:

        sys.setrecursionlimit(n+2)

    def get_ideal_sum(w, n):

        """
            Получить идеальную сумму монет, среди которых нет фальшивых 
        """

        if n == 1:

            return w

        return w*(n) + get_ideal_sum(w, n-1)
    
    # получаем разницу между идеальной суммой и суммой с фальшивыми монетами
    difference = get_ideal_sum(w, n-1) - p

    return difference // d


def task_2(link: str) -> None:

    """
        Необходимо получить HTML-код страницы www.python.org, и посчитать сколько раз какие символы 
        встречается в коде страницы. Формат вывода определяете сами. Вывод программы разместите в 
        файле readme.md.
    """

    html = get(link).text
    chars = set(html) # получаем из страницы только уникальные символы

    with open('readme.md', 'w') as file:
        
        for char in tuple(chars):

            file.write(f'"{char}": {html.count(char)}\n')

    print('результаты 3-его задания записаны в файл "readme.md')
    

def task_3(key) -> None:

    """
        Дан json файл. Найдите в нём все поля "updated" и поменяйте значение на текущие дату и 
        время в формате ISO 8601.
    """

    def search(data):

        if type(data) == dict:
            
            if key in data:

                date = datetime.now().isoformat()
                data[key] = date

            elms = data.values()

        elif type(data) == list:

            elms = data

        else:

            return
        
        for elm in elms:

            if type(elm) in (dict, list):

                search(elm)

            else: 
                
                continue

    with open('example.json') as file:

        data: dict = json.load(file)
    
    search(data)

    with open('result.json', 'w') as file:
        
        json.dump(data, file, indent=3)
    
    print('результаты 4-ого задания записаны в файл "readme.md')


if __name__ == '__main__':

    print(f"значение: {task_0(3)}")
    print(f"монеты в корзине №{task_1(8000, 30, 12, 959879400)} - фальшивые")
    task_2('https://www.python.org')
    task_3('updated')
