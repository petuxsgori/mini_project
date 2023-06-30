import pandas as pd
import keyboard

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

data = pd.read_csv('C://Users/ayuanisimov/Desktop/VUZ/PROJECT_SYSTEM/data/file_with_data.csv')
passwords = pd.read_csv('C://Users/ayuanisimov/Desktop/VUZ/PROJECT_SYSTEM/data/password.csv')
def preprocessing():
    d = data.set_index('id').join(passwords.set_index('id'))
    return d

allData = preprocessing()
exit_from_programm = False
def on_key_press(event):
    if(event.name == '1'):
        print(data.head(data['firstname'].count()))
    if (event.name == '2'):
        print('b')
    if (event.name == '3'):
        print('c')
    if (event.name == '4'):
        print('d')
    if (event.name == '5'):
        print('e')
    if (event.name == 'esc'):
        exit_from_programm = True
        return exit_from_programm

def run():
    user_in_system = pd.DataFrame()
    while user_in_system.empty:
        user_in_system = authorization()
    while 1:
        print('для просмотра всех пользователей нажимите 1 \n'
            'для добавления пользователя нажмите 2 \n'
            'для внесения изменений в учетную запись определенного пользователя нажмите 3\n'
            'для удаления пользователя нажмите 4 \n'
            'для сортировки данных по определенному значению нажмите 5 \n'
            'для выхода из программы нажмите esc \n')
        keyboard.on_press(on_key_press)
        if not exit_from_programm:
            keyboard.wait()

def authorization():
    #email = input("Введите свой email: ")
    #password = input("Введите свой пароль:")
    email = 'anisimov@gmail.com'
    password = 'A9sG6j2R'
    user = allData.loc[((allData['email'] == email) & (allData['password'] == password))]
    if(user['firstname'].count() == 1):
        print('Добро пожаловать в систему!')
    else:
        print('Неверно введены email или пароль')
    return user


run()