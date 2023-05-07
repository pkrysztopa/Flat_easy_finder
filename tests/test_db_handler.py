import unittest
from src.tracking.db_handler import DBHandler
from src.tracking.flat import Flat


class TestDBHandler(unittest.TestCase):
    def setUp(self):
        self.db_handler = DBHandler(":memory:")

    def tearDown(self):
        self.db_handler.con.close()

    def test_create_table(self):
        self.db_handler.create_table()
        self.db_handler.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Houses'")
        result = self.db_handler.cursor.fetchone()
        assert result[0] == "Houses"

    def test_save_to_db(self):
        self.db_handler.create_table()
        flat = Flat()
        flat.price = 100000
        flat.area = 50
        flat.province = 'mazowieckie'
        self.db_handler.save_to_db(flat)
        self.db_handler.con.commit()
        result = self.db_handler.cursor.execute("SELECT * FROM Houses").fetchone()
        assert result[1] == 100000
        assert result[2] == 50
        assert result[3] == 'mazowieckie'

    def test_fetch_data(self):
        self.db_handler.create_table()
        flat_1 = Flat()
        flat_1.price = 100000
        flat_1.area = 50
        flat_1.province = 'mazowieckie'
        self.db_handler.save_to_db(flat_1)
        self.db_handler.con.commit()
        self.db_handler.create_table()
        flat_2 = Flat()
        flat_2.price = 200000
        flat_2.area = 100
        flat_2.province = 'podlaskie'
        self.db_handler.save_to_db(flat_2)
        self.db_handler.con.commit()
        self.db_handler.create_table()
        flat_3 = Flat()
        flat_3.price = 660000
        flat_3.area = 42
        flat_3.province = 'małopolskie'
        self.db_handler.save_to_db(flat_3)
        self.db_handler.con.commit()
        results = self.db_handler.fetch_data()
        assert results == [(1, 100000, 50, 'mazowieckie', None, None, None, None, None, None, None, None, None, None,
                            None, None, None, None, None, None, None, None, None, None, None, None, None),
                           (2, 200000, 100, 'podlaskie', None, None, None, None, None, None, None, None, None, None,
                            None, None, None, None, None, None, None, None, None, None, None, None, None),
                           (3, 660000, 42, 'małopolskie', None, None, None, None, None, None, None, None, None, None,
                            None, None, None, None, None, None, None, None, None, None, None, None, None)]
        results = self.db_handler.fetch_data(columns = ['Cena', 'Powierzchnia'], col_asc='Cena', sort_order='DESC')
        print(results)
        assert results == [(660000, 42), (200000, 100), (100000, 50)]


