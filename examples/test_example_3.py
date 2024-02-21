import unittest
from example_3 import CourseCatalog  # Adjust this import as necessary


class TestCourseCatalog(unittest.TestCase):

    def setUp(self):
        """Reset class variables before each test."""
        CourseCatalog.total_courses = 0
        CourseCatalog.courses_by_subject = {}

    def test_total_courses_increment(self):
        """Test that the total courses count increments correctly."""
        CourseCatalog(course_name="Introduction to Python", instructor="Dr. Jane Smith", students_enrolled=30, duration_weeks=10)
        CourseCatalog(course_name="Advanced Data Science", instructor="Dr. John Doe", students_enrolled=25, duration_weeks=12)
        CourseCatalog(course_name="Web Development Fundamentals", instructor="Dr. Emily Johnson", students_enrolled=20, duration_weeks=8)
        self.assertEqual(CourseCatalog.total_courses, 3)

    def test_courses_by_subject_updates_correctly(self):
        """Test that courses are correctly added to subjects."""
        course1 = CourseCatalog(course_name="Introduction to Python", instructor="Dr. Jane Smith", students_enrolled=30, duration_weeks=10)
        course1.add_course(subject="Computer Science")
        course2 = CourseCatalog(course_name="Advanced Data Science", instructor="Dr. John Doe", students_enrolled=25, duration_weeks=12)
        course2.add_course(subject="Data Science")
        course3 = CourseCatalog(course_name="Web Development Fundamentals", instructor="Dr. Emily Johnson", students_enrolled=20, duration_weeks=8)
        course3.add_course(subject="Web Development")
        expected_courses_by_subject = {
            'Computer Science': ['Introduction to Python'],
            'Data Science': ['Advanced Data Science'],
            'Web Development': ['Web Development Fundamentals']
        }
        self.assertEqual(CourseCatalog.courses_by_subject, expected_courses_by_subject)


if __name__ == '__main__':
    unittest.main()
