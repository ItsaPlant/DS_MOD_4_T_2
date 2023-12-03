import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')


def add(n, m):
    return n + m


def sub(n, m):
    return n - m


def mult(n, m):
    return n * m


def div(n, m):
    return n / m


actions = {
    '1': 'Dodawanie',
    '2': 'Odejmowanie',
    '3': 'Dzielenie',
    '4': 'Mnożenie'
}


if __name__ == "__main__":
    action = input(
        "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    n = input('number 1: ')
    m = input('number 2: ')
    try:
        n = float(n)
        m = float(m)
    except:
        logging.info(f'nan: {n, m}')
        exit()

    if action == '1':
        sol = add(n, m)
    elif action == '2':
        sol = sub(n, m)
    elif action == '3':
        sol = mult(n, m)
    elif action == '4':
        sol = div(n, m)
    else:
        logging.info(f'Action {action} not supported. Abort program.')
        exit()
        
    logging.info(f"{actions[action]} of: {n} and {m}")
    print(sol)
