
class MySqliteRequest():
    def __init__(self):
        pass

    def _from(self, table_name: str) -> object:
        pass

    def select(self, column_names: list or str) -> object:
        pass

    def where(self, column_name: str, criteria: any) -> object:
        pass

    def join(self, column_on_db_a: str, filename_db_b: str, column_on_db_b: str):
        pass

    def order(self, order: str, column_name: str) -> object:
        pass

    def insert(self, table_name: str) -> object:
        pass

    def values(self, data) -> object:
        pass

    def update(self, table_name: str) -> object:
        pass

    def set(self, data) -> object:
        pass

    def delete(self) -> object:
        pass

    def run(self):
        pass