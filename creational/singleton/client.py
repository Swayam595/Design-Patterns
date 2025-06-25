"""Module to create a client and connect to the database using the singleton instance."""
import threading
from database_connection import DatabaseConnection

class Client:
    """Client class."""
    def __init__(self, name, email, phone):
        """Initialize the Client with the given parameters."""
        self.__name = name
        self.__email = email
        self.__password = phone
        print(f"Client {self.__name} connecting to the database...")

    def connect_to_database(self):
        """Connect to the database using the singleton instance."""
        db = DatabaseConnection.get_instance()
        db.connect("localhost", 8080, "mydatabase", self.__email, self.__password)

def create_client(name, email, password):   
    """Create a Client object and connect to the database."""
    client = Client(name, email, password)
    client.connect_to_database()
    print (f"[{threading.current_thread().name}] Client created with instance ID: {id(client)}")

### This method will always raise an exception because the database connection 
### constructor will throw an exception when an object is created using the constructor
def create_new_database_connection_connection():
    """Create a new database connection using the constructor."""
    try:
        db = DatabaseConnection()
        print(f"[{threading.current_thread().name}] Database connection created "
              f"with instance ID: {id(db)}")
    except ValueError as e:
        print(f"[{threading.current_thread().name}] Error creating new database connection: {e}")

if __name__ == "__main__":
    thread1 = threading.Thread(
        target=create_client, 
        args=("John Doe", "john.doe@example.com", "1234567890"), 
        name="Thread 1"
    )

    thread2 = threading.Thread(
        target=create_client, 
        args=("Jane Doe", "jane.doe@example.com", "1234567890"), 
        name="Thread 2"
    )

    thread3 = threading.Thread(target=create_new_database_connection_connection, name="Thread 3")

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()
