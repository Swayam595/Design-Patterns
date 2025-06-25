"""Module to create a client and create a student using the builder pattern."""
import threading
from student import Student

class Client:
    """Client class."""
    __lock = threading.Lock()
    def __init__(self, name, age, gender, address, psp):
        """Initialize the Client with the given parameters."""
        self._name = name
        self._age = age
        self._gender = gender
        self._address = address
        self._psp = psp

    def create_student(self):
        """Create a Student object using the Builder."""
        with Client.__lock:
            student = (Student.get_builder()
                    .set_name(self._name)
                    .set_age(self._age)
                    .set_gender(self._gender)
                    .set_address(self._address)
                    .set_psp(self._psp)
                    .build())
            print(f"[{threading.current_thread().name}] Student created with instance ID: {id(student)}")
            print(student)
            print("\n\n")
            return student

def create_student(name, age, gender, address, psp):
    """Create a Student object using the Client."""
    client = Client(name, age, gender, address, psp)
    return client.create_student()

if __name__ == "__main__":
    thread1 = threading.Thread(target=create_student, args=("John Doe", 20, "Male", "123 Main St, Anytown, USA", 85), name="Thread 1")
    thread2 = threading.Thread(target=create_student, args=("Jane Doe", 21, "Female", "456 Main St, Anytown, USA", 80), name="Thread 2")
    thread3 = threading.Thread(target=create_student, args=("Jim Beam", 22, "Male", "789 Main St, Anytown, USA", 75), name="Thread 3")

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()
