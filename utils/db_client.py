import psycopg2
from utils.config import Config
from utils.logger import get_logger


class DBClient:

    def __init__(self):
        self.logger = get_logger(self.__class__.__name__)

        self.logger.info("Connecting to PostgreSQL database")

        self.connection = psycopg2.connect(
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            database=Config.DB_NAME,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD
        )

    def get_order_by_order_number(self, order_number):
        self.logger.info(f"Fetching order by order number: {order_number}")

        query = """
            SELECT 
                id,
                order_number,
                customer_name,
                customer_phone,
                customer_email,
                order_type,
                payment_method,
                payment_status,
                branch_id,
                total,
                total_with_tax
            FROM orders
            WHERE order_number = %s
        """

        with self.connection.cursor() as cursor:
            cursor.execute(query, (order_number,))
            return cursor.fetchone()

    def close(self):
        self.logger.info("Closing database connection")
        self.connection.close()