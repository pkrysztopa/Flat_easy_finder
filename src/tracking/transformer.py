class Transformer:
    def price(self, expr):
        if expr == 'brak informacji' or expr == 'Zapytaj' or expr == 'Zapytaj o cenę':
            expr = None
        else:
            return float(expr.text.replace('zł', '').replace(' ', ''))

    def year_built(self, expr):
        if expr != None:
            return int(expr)
        else:
            return None

    def city(self, *arg):
        for elem in arg:
            if elem[0].isupper():
                return elem
        return None

    def rooms(self, expr):
        if expr != None:
            return int(expr)
        else:
            return None

    def rent(self, expr):
        if expr != None:
            return float(expr.split(' ')[0].replace(',', '.'))
        else:
            return None

    def area(self, expr):
        if expr != None:
            return float(expr.split(' ')[0].replace(',', '.'))
        else:
            return None

    def localisation(self, *arg):
        city = None
        district = None
        street = None

        for elem in arg:
            if elem.startswith("ul") or elem.startswith("al"):
                street = elem
        for elem in arg:
            if elem[0].isupper():
                city = elem
        for elem in arg:
            if elem != street and elem != city:
                district = elem

        return city, district, street

    def clean_text(self, expr):
        if expr == None:
            return None
        else:
            data = expr.get_text("/*").split('/*')[1].strip()
            if data == 'brak informacji' or data == 'Zapytaj' or data == 'Zapytaj o cenę':
                return None
            else:
                return data