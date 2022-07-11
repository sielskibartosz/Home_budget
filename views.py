from abc import ABC, abstractmethod


class AbstractView(ABC):
    def __init__(self):
        self.repositories = {}

    @abstractmethod
    def draw(self):
        pass

    def set_repository(self, name, repository):
        self.repositories[name] = repository


class AddCost(AbstractView):
    SHORTCUT = 'dk'
    LABEL = 'Dodaj koszt'

    def draw(self):
        print(AddCost.LABEL)
        name = input('Tytul')
        category_name = input('Kategoria')
        amount = float(input('Wartosc'))

        category_id, name = self.repositories['category'].get_by_name(category_name)
        self.repositories['entry'].save(name, category_id, amount * -1)


class ListCosts(AbstractView):
    SHORTCUT = 'wk'
    LABEL = 'Wypisz koszty'

    def draw(self):
        print(ListCosts.LABEL)


class AddIncome(AbstractView):
    SHORTCUT = 'dp'
    LABEL = 'Dodaj przychody'

    def draw(self):
        print(AddIncome.LABEL)


class ListIncomes(AbstractView):
    SHORTCUT = 'wp'
    LABEL = 'Wypisz przychody'

    def draw(self):
        print(ListIncomes.LABEL)


class MainMenu:
    OPTIONS = {
        AddCost.SHORTCUT: AddCost(),
        ListCosts.SHORTCUT: ListCosts(),
        AddIncome.SHORTCUT: AddIncome(),
        ListIncomes.SHORTCUT: ListIncomes()
    }

    def get_screen(self):
        option = None
        while option not in MainMenu.OPTIONS:
            option = input('Wybierz opcje: ')

        return MainMenu.OPTIONS[option]

    def draw(self):
        print('Co zrobic: ')
        for shortcut, screen in MainMenu.OPTIONS.items():
            print(f'[{shortcut}] - {screen.LABEL}')


