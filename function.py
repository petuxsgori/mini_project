import pandas as pd
from datetime import date


def watch_files(data):
    global continue_r
    print(data.head(data['firstname'].count()))
    continue_r = True

def add_user(data,passwords):
    firstname = input('введите имя пользователя')
    lastname = input('введите фамилию пользователя')
    dateBirthday = input('введите день рождения пользователя')
    role = input('введите роль пользователя')
    email = input('введите email пользователя')
    password = input('введите новый 8-значный пароль')
    id = data.max()['id']+1
    login_date = date.today()
    new_data = pd.DataFrame({'id':[id], 'firstname':[firstname], 'lastname':[lastname], 'dateBirthday':[dateBirthday], 'role':[role], 'email':[email], 'login_date':[login_date]})
    new_p = pd.DataFrame({'id':[id],'password':[password]})
    data = pd.concat([data,new_data], ignore_index=True)
    passwords = pd.concat([passwords,new_p], ignore_index=True)

def update_user(data):
    s = input('введите колонки, которые хотите исправить')
    columns = s.split(",")
    #d=data.columns.tolist()
    for i in columns:

