import mysql.connector
config = {
    "user": "sonpro",
    "password": 'Ratiendi89',
    "host": "localhost",
    "port": 3306,
    "database": "FutureLove4",
    "auth_plugin" : "mysql_native_password",
}

def retrieve_data_from_saved_sukien_2_image():
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            print("Connected to MySQL database")
            cursor = connection.cursor()

            # Thực hiện câu lệnh SELECT để truy xuất dữ liệu
            query = "SELECT * FROM saved_sukien_2_image"
            cursor.execute(query)

            # Lấy tất cả các bản ghi từ kết quả của câu lệnh SELECT
            records = cursor.fetchall()

            # In ra các bản ghi
            for record in records:
                print(record)

            return records

    except mysql.connector.Error as error:
        print(f"Failed to connect to MySQL database: {error}")

    finally:
        if "connection" in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")

# Gọi hàm để truy xuất dữ liệu
retrieve_data_from_saved_sukien_2_image()
