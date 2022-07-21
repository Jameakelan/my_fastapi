class Query:

    fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

    def read_item(self,skip: int = 0, limit: int = 10):
        return self.fake_items_db[skip : skip + limit]