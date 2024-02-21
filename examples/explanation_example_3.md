# Course Catalog Management System

## Code

```python
class CourseCatalog:
    total_courses = 0
    courses_by_subject = {}

    def __init__(self, course_name: str, instructor: str,
                 students_enrolled: int, duration_weeks: int) -> None:
        self.course_name = course_name
        self.instructor = instructor
        self.students_enrolled = students_enrolled
        self.duration_weeks = duration_weeks
        CourseCatalog.total_courses += 1

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
```

The `CourseCatalog` class is designed to manage a catalog of educational courses. It tracks the total number of courses and organizes courses by their associated subjects. This class demonstrates the use of class variables for global tracking and categorization, as well as instance variables for individual course attributes.

## Class Overview

- **Class Variables:**
  - `total_courses`: A class-level counter that keeps track of the total number of courses added to the catalog. It's an immutable integer that increases with each instantiation of a `CourseCatalog` object.
  - `courses_by_subject`: A dictionary that organizes courses by their subjects. The keys are subject names, and the values are lists of course names associated with each subject.

## Constructor Method: `__init__`

- The constructor initializes a `CourseCatalog` instance with four parameters: `course_name`, `instructor`, `students_enrolled`, and `duration_weeks`.
- It increments the `total_courses` class variable, reflecting the addition of a new course to the catalog.

## Instance Method: `add_course`

- This method adds the course to a specific subject category within the `courses_by_subject` dictionary.
- If the subject does not exist in the dictionary, a new key-value pair is created with the subject as the key and a list containing the course name as the value. If the subject exists, the course name is appended to the corresponding list.
- The method showcases how class variables can be modified from within instance methods and the dynamic organization of courses by subject.

## Example Usage and Outputs

- Three instances of `CourseCatalog` are created, each representing a different course with unique attributes.
- **Keyword Arguments:** The constructor uses keyword arguments, allowing for the explicit naming of parameters when creating an instance. This enhances code readability and reduces the likelihood of errors from incorrect argument order.
- The `add_course` method is called for each instance to associate the course with a specific subject. This demonstrates how courses are categorized and the catalog is updated dynamically.
- The total number of courses and the structured catalog of courses by subject are printed, highlighting the global tracking and organization capabilities of the class.

## Conclusion

The `CourseCatalog` class illustrates the principles of object-oriented programming applied to the management of a course catalog. It utilizes class and instance variables effectively to track and organize courses on a global and individual level, respectively. The use of keyword arguments in the constructor method enhances the clarity and maintainability of the code, making the class a robust solution for managing educational courses.

