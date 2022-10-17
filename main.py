from recipes_reader import *


@logger('test')
def summator(x, y):
    return x + y


if __name__ == '__main__':
    recipes('recipes.txt')
    get_shop_list_by_dishes(dishes_names, 3)


    three = summator(1, 2)
    five = summator(2, 3)

    result = summator(three, five)

    print('result: ', result)
    print('result type: ', type(result))
