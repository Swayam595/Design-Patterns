import threading

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    @staticmethod
    def get_instance():
        if DatabaseConnection._instance is None:
            with DatabaseConnection._lock:
                if DatabaseConnection._instance is None:
                    DatabaseConnection._instance = DatabaseConnection()
        return DatabaseConnection._instance
    
    def __init__(self):
        self.connection = None

    def connect(self, host, port, database, user, password):
        self.connection = f"Connected to {host}:{port}/{database} as {user} with password {password}"
        print (self.connection)