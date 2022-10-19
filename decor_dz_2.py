from functools import wraps
import datetime


def trace_decorator(some_function):  
    @wraps(some_function)  # wraps подменяет метаданные функции
    def new_function(*args, **kwargs, ):  
        print('Введите путь до файла логов')  
        path_log = input()    
        with open(f'{path_log}', 'a', encoding="UTF8") as f:
            f.write(f'{datetime.datetime.now()}: Вызываем {some_function.__name__} c аргументами {args} и {kwargs}\n')
            result = some_function(*args, **kwargs)
            f.write(f'Вернули результат {result}\n\n\n')
            return result

    return new_function


@trace_decorator
def summator(a,b):
    return a + b


log = summator(3,2)

