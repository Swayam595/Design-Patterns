import threading
import time

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    @staticmethod
    def get_instance():
        print(f"[{threading.current_thread().name}] Checking if instance exists...")
        if DatabaseConnection._instance is None:
            print(f"[{threading.current_thread().name}] Instance is None, attempting to acquire lock...")
            with DatabaseConnection._lock:
                print(f"[{threading.current_thread().name}] Acquired lock, checking again...")
                if DatabaseConnection._instance is None:
                    print(f"[{threading.current_thread().name}] Instance is None, creating new Singleton instance...")
                    DatabaseConnection._instance = DatabaseConnection()
                else:
                    print(f"[{threading.current_thread().name}] Instance already created by another thread")
        else:
            print(f"[{threading.current_thread().name}] Instance already exists, returning existing instance...")
        return DatabaseConnection._instance
    
    def __init__(self):
        self.connection = None

    def connect(self, host, port, database, user, password):
        self.connection = f"Connected to {host}:{port}/{database} as {user} with password {password}"
        print (self.connection)