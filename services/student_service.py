import re
from models.student import Student


class StudentService:
    """Service class - handles student operations with validation."""

    def __init__(self):
        self.students = []  # in-memory storage

    # ---------- Validation helpers ----------
    def _is_valid_email(self, email):
        """Simple email format check."""
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email) is not None

    def _find_by_id(self, student_id):
        """Find a student by ID."""
        for s in self.students:
            if s.id == student_id:
                return s
        return None

    def _find_by_email(self, email):
        """Find a student by email."""
        for s in self.students:
            if s.email.lower() == email.lower():
                return s
        return None

    def _validate(self, student_id, name, email, age, course):
        """Validate input fields. Returns list of errors."""
        errors = []

        # ID
        if not student_id or not student_id.strip():
            errors.append("Student ID is required.")
        elif self._find_by_id(student_id.strip()):
            errors.append(f"Student ID '{student_id}' already exists.")

        # Name
        if not name or not name.strip():
            errors.append("Name is required.")
        elif len(name.strip()) < 2:
            errors.append("Name must be at least 2 characters.")
        elif not re.match(r"^[A-Za-z\s]+$", name.strip()):
            errors.append("Name can only contain letters and spaces.")

        # Email
        if not email or not email.strip():
            errors.append("Email is required.")
        elif not self._is_valid_email(email.strip()):
            errors.append("Email format is invalid.")
        elif self._find_by_email(email.strip()):
            errors.append(f"Email '{email}' already exists.")

        # Age
        try:
            age_int = int(age)
            if age_int < 16 or age_int > 100:
                errors.append("Age must be between 16 and 100.")
        except (ValueError, TypeError):
            errors.append("Age must be a valid number.")

        # Course
        if not course or not course.strip():
            errors.append("Course is required.")

        return errors

    # ---------- Main operations ----------
    def add_student(self, student_id, name, email, age, course):
        """
        Add a new student after validation.
        Returns (success: bool, message: str)
        """
        errors = self._validate(student_id, name, email, age, course)

        if errors:
            return False, " | ".join(errors)

        new_student = Student(
            student_id.strip(),
            name.strip(),
            email.strip(),
            int(age),
            course.strip(),
        )
        self.students.append(new_student)
        return True, f"Student added successfully. ID: {new_student.id}"

    def get_all_students(self):
        """Return all students."""
        return self.students

    def search_by_name(self, keyword):
        """
        Search students by name (case-insensitive partial match).
        Returns (success: bool, results: list, message: str)
        """
        # Empty input check
        if not keyword or not keyword.strip():
            return False, [], "Search keyword is required."

        keyword_lower = keyword.strip().lower()

        # Partial match, case-insensitive
        results = [
            s for s in self.students
            if keyword_lower in s.name.lower()
        ]

        if not results:
            return False, [], f"No students found matching '{keyword.strip()}'."

        return True, results, f"Found {len(results)} student(s) matching '{keyword.strip()}'."