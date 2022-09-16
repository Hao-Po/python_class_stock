from Source.DBController.DBConnection import DBConnection

necessary_table_to_create = {
    "optional_stock_info":
        """
            CREATE TABLE optional_stock_info
            (
                stock_id VARCHAR PRIMARY KEY,
                stock_name VARCHAR(255)         
            );
        """
}

class DBInitializer:
    def execute(self):
        existing_tables = self.get_existing_tables()
        self.__create_inexist_table(existing_tables)

    def get_existing_tables(self):
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM sqlite_master WHERE type='table'")
            records = cursor.fetchall()

        return [single_row["tbl_name"] for single_row in records]

    def __create_inexist_table(self, existing_tables):
        for necessary_table, table_creating_command in necessary_table_to_create.items():
            if necessary_table not in existing_tables:
                self.create_table_with_specefied_command(table_creating_command)

    def create_table_with_specefied_command(self, command):
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()