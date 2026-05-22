import psycopg2
from psycopg2 import sql
from utils.config import Config
from utils.logger import get_logger


class DBClient:

    def __init__(self):
        self.logger = get_logger(self.__class__.__name__)
        self.schema = Config.DB_SCHEMA

        self.logger.info(
            f"Connecting to PostgreSQL database with schema: {self.schema}"
        )

        self.connection = psycopg2.connect(
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            database=Config.DB_NAME,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD
        )

    def get_order_by_order_number(self, order_number):
        self.logger.info(
            f"Fetching order by order number from schema {self.schema}: {order_number}"
        )

        query = sql.SQL("""
                        SELECT
                            {id_col}, {order_number_col}, {customer_name_col}, {customer_phone_col}, {customer_email_col}, {order_type_col}, {payment_method_col}, {payment_status_col}, {branch_id_col}, {total_col}, {total_with_tax_col}
                        FROM {schema}.{table}
                        WHERE {order_number_col} = %s
                        """).format(
            schema=sql.Identifier(self.schema),
            table=sql.Identifier("orders"),
            id_col=sql.Identifier("id"),
            order_number_col=sql.Identifier("orderNumber"),
            customer_name_col=sql.Identifier("customerName"),
            customer_phone_col=sql.Identifier("customerPhone"),
            customer_email_col=sql.Identifier("customerEmail"),
            order_type_col=sql.Identifier("orderType"),
            payment_method_col=sql.Identifier("paymentMethod"),
            payment_status_col=sql.Identifier("paymentStatus"),
            branch_id_col=sql.Identifier("branchId"),
            total_col=sql.Identifier("total"),
            total_with_tax_col=sql.Identifier("totalWithTax"),
        )

        with self.connection.cursor() as cursor:
            cursor.execute(query, (order_number,))
            return cursor.fetchone()

    def close(self):
        self.logger.info("Closing database connection")
        self.connection.close()