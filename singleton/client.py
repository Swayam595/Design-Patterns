from database_connection import DatabaseConnection
import threading

class Client:
    def __init__(self, name, email, phone):
        self.__name = name
        self.__email = email
        self.__password = phone

    def connect_to_database(self):
        db = DatabaseConnection.get_instance()
        db.connect("localhost", 8080, "mydatabase", self.__email, self.__password)

def create_client(name, email, password):
    client = Client(name, email, password)
    client.connect_to_database()
    print (f"[{threading.current_thread().name}] Client created with instance ID: {id(client)}")

if __name__ == "__main__":
    thread1 = threading.Thread(target=create_client, args=("John Doe", "john.doe@example.com", "1234567890"), name="Thread 1")
    thread2 = threading.Thread(target=create_client, args=("Jane Doe", "jane.doe@example.com", "1234567890"), name="Thread 2")

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()