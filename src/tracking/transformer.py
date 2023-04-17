from enumeration import MagicData


class Transformer:

    def __strip_letters(self, expr):
        if expr is not None:
            chars = "0123456789.,"
            output = "".join(char for char in expr if char in chars)
            if output == '':
                return None
            else:
                return output
        else:
            return None

    def clean_price(self, expr):
        if expr is not None:
            data = self.__strip_letters(expr.text)
            return None if data is None else float(data.replace(",", "."))
        return None

    def clean_integer(self, expr):
        if expr is not None:
            data = self.__strip_letters(expr.get_text("/*").split("/*")[1])
            return None if data is None else int(data)
        return None

    def clean_float(self, expr):
        if expr is not None:
            data = self.__strip_letters(expr.get_text("/*").split("/*")[1])
            return None if data is None else float(data.replace(",", "."))
        return None

    def clean_string(self, expr):
        if expr is not None:
            data = expr.get_text("/*").split("/*")[1].strip()
            magic_values = [item.value for item in MagicData]
            if data.lower() in magic_values:
                return None
            return data
        return None

    def localize(self, loc_list):
        city = None
        district = None
        street = None
        province = None

        if len(loc_list) > 1:
            province = loc_list[1]
        if len(loc_list) == 5:
            street = loc_list[4]
        if loc_list[2][0].isupper():
            city = loc_list[2]
        else:
            city = loc_list[3]
        if len(loc_list) > 3 and city == loc_list[2]:
            district = loc_list[3]

        return city, district, street, province

    def clean_string(self, expr):
        if expr is None:
            return None
        else:
            data = expr.get_text("/*").split("/*")[1].strip()
            if (
                data == "brak informacji"
                or data == "brak"
                or data == "Zapytaj"
                or data == "Zapytaj o cenę"
            ):
                return None
            else:
                return data

    def transform_oto(self, flat):
        flat.price = self.clean_price(flat.price)
        flat.market = self.clean_string(flat.market)
        flat.advertiser = self.clean_string(flat.advertiser)
        flat.year_built = self.clean_integer(flat.year_built)
        flat.estate_type = self.clean_string(flat.estate_type)
        flat.windows = self.clean_string(flat.windows)
        flat.lift = self.clean_string(flat.lift)
        flat.utilities = self.clean_string(flat.utilities)
        flat.security = self.clean_string(flat.security)
        flat.furnishing = self.clean_string(flat.furnishing)
        flat.other_info = self.clean_string(flat.other_info)
        flat.material = self.clean_string(flat.material)
        flat.area = self.clean_float(flat.area)
        flat.legal_status = self.clean_string(flat.legal_status)
        flat.rooms = self.clean_integer(flat.rooms)
        flat.condition = self.clean_string(flat.condition)
        flat.level = self.clean_string(flat.level)
        flat.balcony = self.clean_string(flat.balcony)
        flat.rent = self.clean_integer(flat.rent)
        flat.parking = self.clean_string(flat.parking)
        flat.heating = self.clean_string(flat.heating)
        flat.city, flat.district, flat.street, flat.province = self.localize(
            flat.loc_list
        )

        return flat
