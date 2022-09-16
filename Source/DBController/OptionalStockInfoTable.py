from Source.DBController.DBConnection import DBConnection
from Source.DBController.DBInitializer import DBInitializer

class OptionalStockInfoTable:
    DBConnection.db_file_path = "optional_stock.db"
    DBInitializer().execute()

    def insert_new_stock(self, stock_id, stock_name):
        command = "INSERT INTO optional_stock_info (stock_id, stock_name) VALUES ('{}','{}');".format(stock_id, stock_name)
            
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def delete_stock(self, stock_id):
        command = "DELETE FROM optional_stock_info WHERE stock_id='{}';".format(stock_id)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def database_info(self):
        get_optional_stock_info = "SELECT * FROM optional_stock_info"

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(get_optional_stock_info)
            fetch_optional_stock_list = cursor.fetchall()
            try:
                stock_id_name = dict()
                for stock in fetch_optional_stock_list:   
                    stock_id_name.update({str(stock['stock_id']) : stock['stock_name']})
                    
            except Exception as ex:
                print(ex)
                
        return  [stock_id_name]