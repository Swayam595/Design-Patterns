class Student:
    """Student class."""

    def __init__(self, builder, _is_called_by_builder = False):
        """Initialize a Student instance using the Builder."""
        if not _is_called_by_builder:
            raise ValueError("Student cannot be created directly using the constructor")
        self._name = builder.get_name()
        self._age = builder.get_age()
        self._gender = builder.get_gender()
        self._address = builder.get_address()
        self._psp = builder.get_psp()

    def __str__(self):
        """Return a string representation of the Student."""
        return f"Student(name={self._name}, age={self._age}, gender={self._gender}, address={self._address}, psp={self._psp})"

    @staticmethod
    def get_builder():
        """Return a new Builder instance for Student."""
        return Student.Builder()

    class Builder:
        """Builder class for Student."""

        def __init__(self):
            """Initialize the Builder with default None values."""
            self._name = None
            self._age = None
            self._gender = None
            self._address = None
            self._psp = None

        def set_name(self, name):
            """Set the student's name."""
            self._name = name
            return self

        def set_age(self, age):
            """Set the student's age."""
            self._age = age
            return self

        def set_gender(self, gender):  
            """Set the student's gender."""
            self._gender = gender
            return self

        def set_address(self, address):
            """Set the student's address."""
            self._address = address
            return self

        def set_psp(self, psp):
            """Set the student's PSP (Percentile Score Performance)."""
            self._psp = psp
            return self

        def get_name(self):
            """Get the student's name."""
            return self._name

        def get_age(self):
            """Get the student's age."""
            return self._age

        def get_gender(self):   
            """Get the student's gender."""
            return self._gender

        def get_address(self):
            """Get the student's address."""
            return self._address

        def get_psp(self):
            """Get the student's PSP."""
            return self._psp

        def validate(self):
            """Validate the student's fields before building."""
            if self._age is None or self._psp is None:
                return False
            if self._age > 24 and self._psp < 70:
                return False
            if self._age < 18:
                return False
            return True

        def build(self):
            """Build and return a Student object if parameters are valid."""
            if not self.validate():
                raise ValueError("Invalid student: Wrong parameters for the student were provided")
            return Student(self, _is_called_by_builder = True)
