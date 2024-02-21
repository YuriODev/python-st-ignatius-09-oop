class CourseCatalog:
    total_courses = 0  # Class variable (immutable)
    courses_by_subject = {}  # Class variable (mutable)

    def __init__(self, course_name: str, instructor: str,
                 students_enrolled: int, duration_weeks: int) -> None:
        self.course_name = course_name
        self.instructor = instructor
        self.students_enrolled = students_enrolled
        self.duration_weeks = duration_weeks
        CourseCatalog.total_courses += 1  # Incrementing the total number of courses

    def add_course(self, subject: str) -> None:
        """Add the course to the specified subject

        Args:
        subject (str): Name of the subject

        """

        if subject not in CourseCatalog.courses_by_subject:
            CourseCatalog.courses_by_subject[subject] = [self.course_name]
        else:
            CourseCatalog.courses_by_subject[subject].append(self.course_name)
        print(f"Course '{self.course_name}' added to the subject '{subject}'.")


# Example usage
course1 = CourseCatalog(course_name="Introduction to Python",
                        instructor="Dr. Jane Smith",
                        students_enrolled=30,
                        duration_weeks=10)
course1.add_course(subject="Computer Science")

course2 = CourseCatalog(course_name="Advanced Data Science",
                        instructor="Dr. John Doe",
                        students_enrolled=25,
                        duration_weeks=12)

course2.add_course(subject="Data Science")

course3 = CourseCatalog(course_name="Web Development Fundamentals",
                        instructor="Dr. Emily Johnson",
                        students_enrolled=20,
                        duration_weeks=8)
course3.add_course(subject="Web Development")

print("Total Number of Courses:", CourseCatalog.total_courses) # 3
print("Courses by Subject:", CourseCatalog.courses_by_subject) # {'Computer Science': ['Introduction to Python'], 'Data Science': ['Advanced Data Science'], 'Web Development': ['Web Development Fundamentals']}
