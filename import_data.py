import mysql.connector
import csv
from mysql.connector import Error
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def connect_to_db(host, user, password, database):
    """Підключення до MySQL бази даних"""
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            use_pure=True
        )
        logger.info(f"Successfully connected to database: {database}")
        return connection
    except Error as e:
        logger.error(f"Error connecting to MySQL: {e}")
        return None

def create_table(connection):
    """Створення таблиці infectious_cases"""
    if connection is None:
        logger.error("No database connection.")
        return

    cursor = connection.cursor()
    
    # Спочатку видаляємо таблицю якщо вона існує
    drop_table_query = "DROP TABLE IF EXISTS infectious_cases"
    
    # Створюємо нову таблицю
    create_table_query = """
    CREATE TABLE IF NOT EXISTS infectious_cases (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Entity TEXT,
        Code TEXT,
        Year INT,
        Number_yaws DOUBLE,
        polio_cases DOUBLE,
        cases_guinea_worm DOUBLE,
        Number_rabies DOUBLE,
        Number_malaria DOUBLE,
        Number_hiv DOUBLE,
        Number_tuberculosis DOUBLE,
        Number_smallpox DOUBLE,
        Number_cholera_cases DOUBLE
    )
    """
    
    try:
        cursor.execute(drop_table_query)
        cursor.execute(create_table_query)
        connection.commit()
        logger.info("Table created successfully.")
    except Error as e:
        logger.error(f"Error creating table: {e}")
        connection.rollback()
    finally:
        cursor.close()

def read_csv_file(file_path):
    """Читання та обробка CSV файлу"""
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            for row_num, row in enumerate(csv_reader, start=1):
                processed_row = {}
                try:
                    # Обробляємо текстові поля
                    processed_row['Entity'] = row['Entity']
                    processed_row['Code'] = row['Code']
                    
                    # Обробляємо числові поля
                    for key, value in row.items():
                        if key in ['Entity', 'Code']:
                            continue
                        
                        if value == '' or value is None:
                            processed_row[key] = None
                        else:
                            try:
                                processed_row[key] = float(value)
                            except ValueError:
                                logger.warning(f"Cannot convert '{value}' to float for column '{key}' in row {row_num}")
                                processed_row[key] = None
                    
                    data.append(processed_row)
                    
                except Exception as e:
                    logger.error(f"Error processing row {row_num}: {e}")
                    continue
                    
        logger.info(f"Successfully read {len(data)} rows from CSV file")
        return data
        
    except FileNotFoundError:
        logger.error(f"CSV file not found: {file_path}")
        return []
    except Exception as e:
        logger.error(f"Error reading CSV file: {e}")
        return []

def insert_data(connection, data):
    """Вставка даних в таблицю"""
    if connection is None:
        logger.error("No database connection.")
        return
    
    if not data:
        logger.error("No data to insert.")
        return

    cursor = connection.cursor()
    
    insert_query = """
    INSERT INTO infectious_cases (
        Entity, Code, Year, Number_yaws, polio_cases, cases_guinea_worm, 
        Number_rabies, Number_malaria, Number_hiv, Number_tuberculosis, 
        Number_smallpox, Number_cholera_cases
    ) VALUES (
        %(Entity)s, %(Code)s, %(Year)s, %(Number_yaws)s, %(polio_cases)s, 
        %(cases_guinea_worm)s, %(Number_rabies)s, %(Number_malaria)s, 
        %(Number_hiv)s, %(Number_tuberculosis)s, %(Number_smallpox)s, 
        %(Number_cholera_cases)s
    )
    """
    
    try:
        cursor.executemany(insert_query, data)
        connection.commit()
        logger.info(f"Successfully inserted {cursor.rowcount} rows.")
    except Error as e:
        logger.error(f"Error inserting data: {e}")
        connection.rollback()
    finally:
        cursor.close()

def main():
    # ЗМІНІТЬ ЦІ НАЛАШТУВАННЯ НА ВАШІ!
    host = '127.0.0.1'  # або 'localhost'
    user = 'root'       # ваш MySQL користувач
    password = '1234'  # ваш MySQL пароль
    database = 'pandemic'  # назва бази даних
    csv_file_path = 'infectious_cases.csv'  # шлях до CSV файлу
    
    # Підключення до бази даних
    connection = connect_to_db(host, user, password, database)
    
    if connection:
        try:
            # Створення таблиці
            create_table(connection)
            
            # Читання CSV файлу
            data = read_csv_file(csv_file_path)
            
            # Вставка даних
            if data:
                insert_data(connection, data)
                logger.info("Data import completed successfully!")
            else:
                logger.error("No data to import.")
                
        except Exception as e:
            logger.error(f"Error in main process: {e}")
        finally:
            connection.close()
            logger.info("Database connection closed.")
    else:
        logger.error("Failed to connect to database. Please check your connection settings.")

if __name__ == "__main__":
    main()