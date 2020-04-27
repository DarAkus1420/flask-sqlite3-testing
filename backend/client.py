class Client:

    def __init__(self, code, name, city, debt):

        # ------------------------Properties---------------------------

        self.code = code
        self.name = name
        self.city = city
        self.debt = debt

    # -------------Getters - Setters -----------------------------

    # Getters setters code
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    # Getters setters name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
    
    # Getters setters city
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city
    
    # Getters setters debt
    @property
    def debt(self):
        return self._debt

    @debt.setter
    def debt(self, debt):
        self._debt = debt

    def to_sql(self):
        return [[key[1:], type(value).__name__] for key, value in self.__dict__.items()]
    
    def return_data(self):
        return [repr(value) for key, value in self.__dict__.items()]

    def extra_param_sql(self):
        return {
            'code': 'PRIMARY KEY',
            'name': 'NOT NULL',
            'city': 'NOT NULL',
            'debt': 'NOT NULL'

        }
