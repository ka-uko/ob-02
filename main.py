class User:
    def __init__(self, ID, name):
        self._ID = ID
        self.__name = name  # Защищенный атрибут
        self._level = 'user'

    def enter_system(self):
        print(f'Пользователь ID {self._ID} вошел в систему')

    def exit_system(self):
        print(f'Пользователь ID {self._ID} вышел из системы')

    def upload_data(self):
        print(f'Пользователь ID {self._ID} загрузил данные')

    def info(self):
        print(f'ID пользователя: {self._ID}')
        print(f'Имя: {self.__name}')
        print(f'Уровень: {self._level}')

    # Доступы
    def get_id(self):
        return self._ID

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_level(self):
        return self._level


class Admin(User):
    def __init__(self, ID, name):
        super().__init__(ID, name)
        self._admin_level = 'admin'

    def add_user(self, user_list, user):
        user_list.append(user)
        print(f'Администратор добавил пользователя: {user.get_name()}')

    def remove_user(self, user_list, user):
        if user in user_list:
            user_list.remove(user)
            print(f'Администратор удалил пользователя: {user.get_name()}')
        else:
            print(f'Пользователь {user.get_name()} не найден в системе')

    def info_admin(self):
        self.info()  # Вызов метода info базового класса
        print(f'Уровень администратора: {self._admin_level}')

    def get_admin_level(self):
        return self._admin_level

#Объекты
user1 = User('01', "Петр")
user2 = User('02', 'Николай')

admin1 = Admin('03', 'Михаил')
admin2 = Admin('04', 'Елена')

# Список пользователей
user_list = [user1, user2]


user1.exit_system()
user1.upload_data()
user2.info()
admin1.info_admin()
admin2.add_user(user_list, User('05', 'Анна'))
admin2.remove_user(user_list, user1)
admin2.exit_system()




