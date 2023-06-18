# ✔Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.



def param_dict(**kwargs):
    param_dict = {}
    for i, e in kwargs.items():
        try:
            param_dict[e] = i
        except:
            param_dict[f'{e}'] = i
    return param_dict


print(param_dict(a=2, b=5, trip = 't-r-i-p', massive=[1,2,3, [1,2,5]], input_dict={1:3, 3:4}))