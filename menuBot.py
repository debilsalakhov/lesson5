from telebot import types


class Menu:
    hash = {}  # все экземпляры класса
    cur_menu = {}  # текущий экземпляр класса, текущее меню
    extendedParameters = {}  # место хранения доп параметров для передачи в inline кнопки

    def __init__(self, name, buttons=None, parent=None, action=None):
        self.parent = parent
        self.name = name
        self.buttons = buttons
        self.action = action

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
        markup.add(*buttons)
        self.markup = markup
        self.__class__.hash[name] = self  # обновляем словарь с классами

    @classmethod
    def getExtPar(cls, id):
        return cls.extendedParameters.pop(id, None)

    @classmethod
    def setExtPar(cls, parameter):
        import uuid
        id = uuid.uuid4().hex
        cls.extendedParameters[id] = parameter
        return id

    @classmethod
    def getMenu(cls, chat_id, name):
        menu = cls.hash.get(name)
        if menu is not None:
            cls.cur_menu[chat_id] = menu
        return menu

    @classmethod
    def getCurMenu(cls, chat_id):
        return cls.cur_menu.get(chat_id)


m_main = Menu('Главное меню', buttons=['Развлечения', 'Игры', 'ДЗ', 'Помощь'])
m_games = Menu('Игры', buttons=['Камень, ножницы, бумага', 'Игра в 21', 'Угадай кто?', 'Выход'], parent=m_main)
m_game_21 = Menu('Игра в 21', buttons=['Карту!', 'Стоп!', 'Выход'], parent=m_games, action='game_21')
m_game_rsp = Menu('Камень, ножницы, бумага',  buttons=['Камень', 'Ножницы', 'Бумага', 'Выход'], parent=m_games,
                  action='game_rsp')
m_entertainment = Menu('Развлечения', buttons=['Прислать собаку', 'Прислать анекдот', 'Прислать фильм', 'Выход'], parent=m_main)
m_DZ = Menu("ДЗ", buttons=["Задание-1", "Задание-2", "Задание-3", "Задание-4", "Задание-5", "Задание-6", "Выход"], parent=m_main)
