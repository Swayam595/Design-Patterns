from database_connection import DatabaseConnection

class Client:
    def __init__(self, name, email, phone):
        self.__name = name
        self.__email = email
        self.__password = phone

    def connect_to_database(self):
        db = DatabaseConnection.get_instance()
        db.connect("localhost", 8080, "mydatabase", self.__email, self.__password)

if __name__ == "__main__":
    client1 = Client("John Doe", "john.doe@example.com", "1234567890")
    client1.connect_to_database()

    client2 = Client("Jane Doe", "jane.doe@example.com", "1234567890")
    client2.connect_to_database()