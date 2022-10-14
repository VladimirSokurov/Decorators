from datetime import datetime


def logger(name):
    '''
    Записывает в файл дату и время вызова функции, имя функции, аргументы,
с которыми вызвалась и возвращаемое значение.
    '''

    def _logger(some_function):
        def new_function(*args, **kwargs):
            file = open(f'{name}.txt', 'a+')
            arguments = None
            if args:
                arguments = args
            elif kwargs:
                arguments = kwargs
            else:
                file.write(f'{datetime.now()}, {some_function.__name__}, {some_function(*args, **kwargs)}\n')
            file.write(f'{datetime.now()}, {some_function.__name__}, {arguments}, {some_function(*args, **kwargs)}\n')
            file.close()

        return new_function

    return _logger
