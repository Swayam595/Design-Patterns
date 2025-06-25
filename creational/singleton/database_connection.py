"""Module to create a singleton instance of the DatabaseConnection class."""
import threading

class DatabaseConnection:
    """DatabaseConnection class."""
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        """Initialize the DatabaseConnection instance."""
        if DatabaseConnection._instance is not None:
            raise ValueError("Use get_instance() to get the singleton instance.")
        self.connection = None


    @staticmethod
    def get_instance():
        """Get the singleton instance of the DatabaseConnection class."""
        print(f"[{threading.current_thread().name}] Checking if instance exists...")
        if DatabaseConnection._instance is None:
            print(f"[{threading.current_thread().name}] Instance is None, "
                  "attempting to acquire lock...")
            with DatabaseConnection._lock:
                print(f"[{threading.current_thread().name}] Acquired lock, checking again...")
                if DatabaseConnection._instance is None:
                    print(f"[{threading.current_thread().name}] Instance is None, "
                          "creating new Singleton instance...")
                    DatabaseConnection._instance = DatabaseConnection()
                else:
                    print(f"[{threading.current_thread().name}] Instance already "
                          "created by another thread")
        else:
            print(f"[{threading.current_thread().name}] Instance already exists, "
                  "returning existing instance...")
        return DatabaseConnection._instance

    def connect(self, host, port, database, user, password):
        """Connect to the database."""
        self.connection = (f"Connected to {host}:{port}/{database} "
                           f"as {user} with password {password}")
        print (self.connection)
