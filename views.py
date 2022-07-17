from abc import ABC, abstractmethod
from terminaltables import AsciiTable


class AbstractView(ABC):
    def __init__(self):
        self.repositories = {}

    @abstractmethod
    def draw(self):
        pass

    def set_repository(self, name, repository):
        self.repositories[name] = repository


class AddView:
    def get_category_id(self, repository):
        found_category = False
        while not found_category:
            try:
                category_name = input('Kategoria')
                category_id, _ = repository.get_by_name(category_name)
                found_category = True
            except TypeError:
                found_category = False

        return category_id


class AddCost(AbstractView, AddView):
    SHORTCUT = 'dk'
    LABEL = 'Dodaj koszt'

    def draw(self):
        print(AddCost.LABEL)
        name = input('Tytul')
        amount = float(input('Wartosc'))
        category_id = self.get_category_id(self.repositories['category'])
        self.repositories['entry'].save(name, category_id, amount * -1)

class ListCosts(AbstractView):
    SHORTCUT = 'wk'
    LABEL = 'Wypisz koszty'

    def draw(self):
        print(ListCosts.LABEL)
        rows = [
            ['tytuł', 'data dodania', 'kwota', 'kategoria']
        ]
        for cost_id, name, created_at, amount, category in self.repositories['entry'].get_costs():
            rows.append([name, created_at, amount, category])

        table = AsciiTable(rows)
        print(table.table)

class AddIncome(AbstractView, AddView):
    SHORTCUT = 'dp'
    LABEL = 'Dodaj przychody'

    def draw(self):
        print(AddIncome.LABEL)
        name = input('Tytul')
        amount = float(input('Wartosc'))
        category_id = self.get_category_id(self.repositories['category'])
        self.repositories['entry'].save(name, category_id, amount)


class ListIncomes(AbstractView):
    SHORTCUT = 'wp'
    LABEL = 'Wypisz przychody'

    def draw(self):
        print(ListIncomes.LABEL)
        rows = [
            ['tytuł', 'data dodania', 'kwota', 'kategoria']
        ]
        for cost_id, name, created_at, amount, category in self.repositories['entry'].get_incomes():
            rows.append([name, created_at, amount, category])

        table = AsciiTable(rows)
        print(table.table)


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
