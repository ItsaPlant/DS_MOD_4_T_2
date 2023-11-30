import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

actions = {
    '1': 'Dodawanie',
    '2': 'Odejmowanie',
    '3': 'Dzielenie',
    '4': 'Mnożenie'
}
action = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
arg_1 = input('number 1')
arg_2 = input('number 2')
if type(arg_1) and type(arg_2) is not (int or float):
    logging.info(f'nan: {arg_1, arg_2}')
    exit()
if action == '1':
    sol = arg_1 + arg_2
elif action == '2':
    sol = arg_1 - arg_2
elif action == '3':
    sol = arg_1 * arg_2
elif action == '4':
    sol = arg_1 / arg_2
logging.info(f"{actions[action]} of: {arg_1} and {arg_2}")
print(sol)