from .student import Student

class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation=False):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation

    def summary(self):
        student_summary = super().summary()
        transportation_summary = self.display_transportation_message(student_summary)
        return f"{student_summary} {transportation_summary}"

    def display_transportation_message(self, student_summary):
        transportation_summary = "Transportation status: True" if self.gets_transportation else "Transportation status: False"
        return f"{student_summary} {transportation_summary}"