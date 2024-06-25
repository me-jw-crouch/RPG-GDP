from datetime import datetime, timedelta

class DatabaseTable:
    def __init__(self):
        self.rows = {}
        self.nextUID = 0

    def __getitem__(self, item):
        return self.rows.get(item)

    def insert_row(self, **attributes):
        self.rows[self.nextUID] = attributes
        self.nextUID += 1

    def read_row(self, key):
        return self.rows.get(key)

    def update_row(self, key, **attributes):
        if key in self.rows:
            self.rows[key].update(attributes)

    def delete_row(self, key):
        if key in self.rows:
            del self.rows[key]

    def find_all_rows_by_attribute(self, **criteria):
        results = []

        for key, attributes in self.rows.items():
            if all(attributes.get(k) == v for k, v in criteria.items()):
                results.append((key, attributes))

        return results
