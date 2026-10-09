class Student:
    """Student model - represents a student in the system."""

    def __init__(self, student_id, name, email, age, course):
        self.id = student_id
        self.name = name
        self.email = email
        self.age = age
        self.course = course

    def to_dict(self):
        """Convert student to dictionary (useful for storage/printing)."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "course": self.course,
        }

    def __str__(self):
        return f"[{self.id}] {self.name} | {self.email} | Age: {self.age} | Course: {self.course}"