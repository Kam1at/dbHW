import csv
import psycopg2


class Homework:
    _password = input('Введите пароль: ')
    file_name = str
    table_name = str

    def add_data(self):
        connect = psycopg2.connect(
            host='localhost',
            database='north',
            user='postgres',
            password=self._password
        )
        with connect as conn:
            with conn.cursor() as cur:
                with open(self.file_name) as file:
                    reader = csv.reader(file)
                    next(file)                         # Пропуск первой строки .csv файла
                    for row in reader:
                        cur.execute(f'INSERT INTO {self.table_name} VALUES ({"%s, "* (len(row) - 1) + "%s"})', tuple(row))
        conn.close()

    def customers(self):
        self.file_name = 'customers_data.csv'
        self.table_name = 'customers'
        return self.add_data()

    def employee(self):
        self.file_name = 'employees_data.csv'
        self.table_name = 'employees'
        return self.add_data()

    def orders(self):
        self.file_name = 'orders_data.csv'
        self.table_name = 'orders'


if __name__ == '__main__':
    run = Homework()
    run.customers()
    run.employee()
    run.orders()