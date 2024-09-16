# 📘 Object-Oriented Programming in Python

Welcome to the first module of our Python course at St. Ignatius College, focusing on Simple Data Types. This module is designed to lay a solid foundation for understanding how Python stores, manipulates, and utilizes data.

# Navigation 🧭

This module is part of the larger Python programming course offered by St. Ignatius College, designed to take you from basic to advanced programming concepts in a step-by-step manner. 

[Course Repository: Comprehensive Python Course](https://github.com/YuriODev/St-Ignatius-Python-Course)

⬅️ [Previous Topic: Files](https://github.com/YuriODev/python-yuriodev-08-files-in-python/blob/main/README.md)

➡️ [Next Topic: Modules and Packages](https://github.com/YuriODev/python-yuriodev-10-modules-and-packages/blob/main/README.md)

# Course Overview 🎓

This Python course covers a wide range of topics, designed to provide you with a solid foundation in programming, from simple data types to advanced concepts like Object-Oriented Programming and data structures. Each module is carefully crafted to build upon the previous one, ensuring a comprehensive understanding of Python programming.

## Modules Covered:
- [Variables and Data Types 📊](https://github.com/YuriODev/python-yuriodev-01-simple-data-types/blob/main/README.md) 
- [Conditional Statements 🔀](https://github.com/YuriODev/python-yuriodev-02-simple-conditional-statements/blob/main/README.md)
- [Iterations and Loops ➿](https://github.com/YuriODev/python-yuriodev-03-iterations-and-loops/blob/main/README.md)
- [String Manipulation 🧵](https://github.com/YuriODev/python-yuriodev-04-string-manipulation/blob/main/README.md)
- [Lists and Tuples 📝](https://github.com/YuriODev/python-yuriodev-05-lists-in-python/blob/main/README.md)
- [Dictionaries 🗂](https://github.com/YuriODev/python-yuriodev-06-mastering-dictionaries/blob/main/README.md)
- [Functions 🛠](https://github.com/YuriODev/python-yuriodev-07-functions-in-python/blob/main/README.md)
- [Files 🗄](https://github.com/YuriODev/python-yuriodev-08-files-in-python/blob/main/README.md)
- **Object-Oriented Programming (OOP) (Current Module)**
- [Modules and Packages 📦](https://github.com/YuriODev/python-yuriodev-10-modules-and-packages/blob/main/README.md)
- [Unit Testing ✅](https://github.com/YuriODev/python-yuriodev-11-unit-testing/blob/main/README.md)

## 📂 Repository Structure

- [Theory](./theory): This folder contains all the theoretical materials related to simple data types in Python.
- [Examples](./examples): Here you can find example problems and their solutions to understand the practical implementation of the concepts covered.
- [Exercises](./exercises): Here you can find exercises to practice your understanding of the topics covered.
- [Solutions](./solutions): This folder contains solutions to the exercises. It's recommended to try solving the exercises yourself before checking the solutions.

## 📝 Overview

In this module, we'll dive deep into the basics of Python programming, starting with objects and variables, moving through numbers and strings, and learning how to interact with users through keyboard input. Each section is crafted to enhance your understanding and skills in handling data in Python.

## 🧩 Topics Covered

### 1. Introduction to Object-Oriented Programming (OOP) 🌟
   - Explore the definition and significance of OOP in modern programming.
   - Compare OOP with procedural programming to highlight advantages.
   - Introduce core OOP concepts: Classes, Objects, Methods, Attributes.

### 2. Benefits of Object-Oriented Programming 🚀
   - Discuss modularity, highlighting how OOP facilitates modular code development.
   - Cover reusability, demonstrating how OOP principles encourage code reuse.
   - Explain code readability and maintainability improvements through OOP.
   - Introduce key OOP features: Encapsulation, Inheritance, Polymorphism.

### 3. Classes and Objects 🛠
   - **Class Definition**
      - Explain the structure and syntax for defining classes in Python.
      - Discuss the purpose and usage of the `__init__` constructor method.
      - Introduce the concept of a `FootballPlayer` class with attributes like `name` and `position`.
   - **Object Instantiation**
      - Guide on creating instances from a class (object instantiation).
      - Demonstrate accessing attributes and methods on class instances.
      - Provide an example of creating and interacting with a `FootballPlayer` object.

### 4. Attributes and Methods 🔑
   - **Instance Variables**
      - Detail instance variables and their role in defining object state.
   - **Class Variables**
      - Explain class variables and how they are shared across class instances.
      - Use a class variable in the `FootballPlayer` class to demonstrate sharing data.
   - **Methods in Depth**
      - Elaborate on creating and using instance, class, and static methods.
      - Highlight the importance of the `self` parameter in instance methods.
      - Extend the `FootballPlayer` class with methods like `score_goal` to showcase method usage.

### 5. Encapsulation 🛡
   - **Understanding Encapsulation**
      - Discuss the concept of encapsulating data within an object.
      - Explain the distinction between public, protected and private attributes.
   - **Implementing Encapsulation**
      - Introduce property decorators for creating getter and setter methods.
      - Apply encapsulation in the `FootballPlayer` class to manage `age` attribute access securely.

### 6. Getters and Setters 🔄
   - **Using Getters and Setters**
      - Discuss why getters and setters are important for data encapsulation and validation.
      - Implement getters and setters in the `FootballPlayer` class to control access to private attributes like `__salary`.

### 7. Inheritance (Preview) 🌱
   - Provide a brief overview of inheritance as an introduction to the next notebook.
   - Highlight the concept of deriving new classes from existing ones to extend or modify functionality.

### 8. Deep Dive into Inheritance 🌱
  - **The Power of Inheritance**: Explore the concept of inheritance in OOP, enabling new classes to take on properties and methods of existing classes.
    - Example: Extending a `FootballPlayer` class to a more specific `Goalkeeper` class.
  - **Customizing with Method Overriding**: Learn how subclasses can override methods of their superclass to perform different or additional actions.
    - Example: Overriding the `save_goal` method in the `Goalkeeper` class.
  - **Advanced Inheritance Patterns**: Discuss scenarios where multiple inheritance might be used and how Python resolves method lookup.
    - Example: Creating a `PlayerCoach` class that inherits from both `Player` and `Coach` classes.
  - **Utilizing the `super()` Function**: Demystify the `super()` function for accessing superclass methods from a subclass.
    - Example: Using `super()` in the `Goalkeeper` class to extend the `__init__` method.

### 9. Exploring Polymorphism 🔁
  - **Understanding Polymorphism**: Introduce polymorphism as a way to use a unified interface for objects of different classes.
    - Example: A function that accepts any object that has a `play` method, whether it's a `FootballPlayer` or a `Musician`.
  - **Implementing Polymorphism**: Show how Python's dynamic nature supports polymorphism without the need for complex type hierarchies.
    - Example: Writing a generic `team_performance` function that can apply to objects of both the `FootballPlayer` and `Coach` classes.
  - **Duck Typing and Python**: Illustrate the concept of duck typing in Python and how it relates to polymorphism.
    - Example: Demonstrating duck typing with different objects that implement a common method differently.

### 10. Mastering Magic Methods and Operator Overloading ✨
  - **Introduction to Magic Methods**: Explain magic methods and how they allow customization of Python's built-in behavior for custom classes.
    - Example: Implementing `__str__` and `__repr__` for the `FootballPlayer` class for better string representation.
  - **Operator Overloading Fundamentals**: Cover how to overload standard operators for custom objects using magic methods.
    - Example: Overloading the `+` operator to combine the goals of two `FootballPlayer` instances.
  - **Comprehensive List of Magic Methods**: Provide an overview of various magic methods for comparison, arithmetic operations, and container behaviors.
    - Example: Using `__add__`, `__lt__` (less than), `__eq__` (equal to), and `__getitem__` for a class representing a team.

### 11. Abstract Base Classes (ABCs) and Interface Definition 🛡️
  - **Why Use ABCs?**: Understand the role of abstract base classes in defining interfaces and enforcing subclass implementation.
    - Example: Defining an `Athlete` ABC with an abstract `train` method.
  - **Creating and Using ABCs**: Learn to use the `abc` module to create abstract classes and abstract methods.
    - Example: Implementing an `Athlete` class that cannot be instantiated and requires subclasses to implement the `train` method.

### 12. Multiple Inheritance and Mixins 🔄
  - **Understanding Multiple Inheritance**: Navigate the complexities and benefits of inheriting from more than one base class.
    - Example: Creating a `StudentAthlete` class that inherits from both `Student` and `Athlete` classes.
  - **Leveraging Mixins for Composability**: Utilize mixins to add reusable functionalities to classes.
    - Example: Introducing a `TrainingMixin` that provides additional training methods to any class.

### 13. Decorators in OOP 🎨
  - **Enhancing Methods with Decorators**: Use decorators to add new functionalities to methods without modifying their original structure.
    - Example: Applying a `@performance_timer` decorator to time methods in the `Athlete` class.
  - **Creating Custom Decorators**: Dive into writing your own decorators for methods in OOP contexts.
    - Example: Writing a `@debug` decorator to log method calls and arguments.

### 14. Advanced Use Cases and Techniques 🚀
  - **Operator Overloading for Custom Behaviors**: Explore further examples of magic methods for custom object behavior.
    - Example: Implementing `__call__` in the `Coach` class to make objects callable.
  - **Using Context Managers in OOP**: Implement context managers within classes for resource management.
    - Example: Creating a `GameSession` context manager to manage game state.

### 15. Best Practices and Common Design Patterns 🏅
  - **OOP Best Practices**: Summarize key practices for writing effective and clean OOP code.
  - **Exploring Design Patterns**: Introduction to common OOP design patterns like Singleton, Factory, Strategy, and Observer.
    - Example: Implementing the Singleton pattern in a `GameManager` class.
  - **Real-World Applications of Design Patterns**: Discuss how these patterns are applied in real-world scenarios and projects.

### 16. Conclusion and Further Learning 📚
  - **Wrapping Up**: Reflect on the journey through OOP with Python and how these concepts apply to real-world software development.
  - **Beyond the Basics**: Recommendations for further exploration in OOP, including resources, projects, and advanced topics not covered in this series.



# Learning Path 🛣️

1. **Fundamentals of Object-Oriented Programming (OOP)**
   - Notebook 1: Introduction to OOP
   - Notebook 2: Inheritance and Polymorphism
   - Notebook 3: Advanced OOP Concepts


# Exercises and Examples 🏋️‍♂️

Each section is accompanied by practical exercises and examples, enabling you to apply the concepts you've learned. Remember, practice is key to mastering programming!


## 🙋‍♂️ Asking for Help

Encountering difficulties is a natural part of the learning journey. Our team encourages all students to ask questions, seek help, and engage deeply with the course material. We're here to support you every step of the way.

## 🛠 Additional Resources

To further enhance your understanding of Python's simple data types and get more hands-on practice, explore the following resources:

- [Python Official Documentation on Strings](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str): Dive deep into Python's official documentation for a comprehensive understanding of string operations and methods.
- [Real Python on Python String Formatting](https://realpython.com/python-f-strings/): An excellent tutorial on modern string formatting techniques in Python, including the powerful f-strings.
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/2e/chapter6/): Learn practical applications of Python strings in automating everyday tasks.
- [W3Schools Python Tutorial](https://www.w3schools.com/python/): Offers a wide range of Python tutorials and exercises, from basic to advanced topics.
- [Programiz Python Programming](https://www.programiz.com/python-programming): A resource for beginners and intermediate learners with tutorials, examples, and editor to write and test Python code.

We encourage you to explore beyond the exercises provided, delve into additional problems, and experiment with code. Our department is committed to fostering a supportive learning environment and is excited to see your progress.

Happy Coding! 💻

## License

This project is licensed under a custom license. Please note the following important restrictions:

- The Software shall not be used for educational purposes in any formal educational institutions such as schools, colleges, or universities without the explicit permission of the copyright holder.
- The Software is provided for personal, non-commercial use only.
- Forking the repository is allowed for personal use and non-commercial purposes only. Any forks or derivatives of this repository must include this license and maintain the same restrictions.

For full details, please refer to the [LICENSE](./LICENSE) file.
