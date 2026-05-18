import psycopg2
from utils.config import Config


class DBClient:

    def __init__(self):
        self.connection = psycopg2.connect(
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            database=Config.DB_NAME,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD
        )

    def get_order_by_order_number(self, order_number):
        cursor = self.connection.cursor()

        query = """
            SELECT id,
                   order_number,
                   customer_name,
                   payment_method,
                   payment_status,
                   order_type
            FROM orders
            WHERE order_number = %s
        """

        cursor.execute(query, (order_number,))
        result = cursor.fetchone()

        cursor.close()

        return result

    def close(self):
        self.connection.close()