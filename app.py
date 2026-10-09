from flask import Flask, render_template, request
from services.student_service import StudentService

app = Flask(__name__)

# In-memory storage
service = StudentService()


@app.route("/")
def index():
    """Home page - show all students."""
    students = service.get_all_students()
    return render_template("index.html", students=students)


@app.route("/add", methods=["GET", "POST"])
def add_student():
    """Add student page."""
    message = None
    message_type = None  # 'success' or 'error'

    if request.method == "POST":
        student_id = request.form.get("student_id", "").strip()
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        age = request.form.get("age", "").strip()
        course = request.form.get("course", "").strip()

        success, msg = service.add_student(student_id, name, email, age, course)

        if success:
            message = msg
            message_type = "success"
        else:
            message = msg
            message_type = "error"

    return render_template(
        "add_student.html",
        message=message,
        message_type=message_type,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)