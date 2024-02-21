# Exercises 🏋️‍♂️

## Topics Covered:
- Defining and Instantiating Classes
- Working with Class and Instance Variables
- Implementing Instance Methods with Detailed Arguments Description

---

## Exercise 1: Library Management System

**Objective:** Develop a class `Book` for a library system to manage book checkouts.

### Specifications:
- **Class Variables:**
  - `total_books`: Tracks the total number of books in the library.
- **Instance Variables:**
  - `title` (str): The title of the book.
  - `author` (str): The author of the book.
  - `is_checked_out` (bool): True if the book is checked out, False otherwise.
- **Methods:**
  - `check_out() -> None`: Sets `is_checked_out` to True. Prints a message indicating the book has been checked out.
  - `check_in() -> None`: Sets `is_checked_out` to False. Prints a message indicating the book has been returned.

### Example Usage:

| Task                      | Inputs                                    | Expected Outputs                                  |
|---------------------------|-------------------------------------------|---------------------------------------------------|
| Instantiate a book object | `Book("The Hobbit", "J.R.R. Tolkien")`    | "Book 'The Hobbit' by J.R.R. Tolkien added."      |
| Check out the book        | `book.check_out()`                        | "'The Hobbit' has been checked out."              |
| Check in the book         | `book.check_in()`                         | "'The Hobbit' has been returned to the library."  |

---

## Exercise 2: Simple Bank Account

**Objective:** Create a class `BankAccount` to represent a user's bank account, allowing deposits and withdrawals.

### Specifications:
- **Instance Variables:**
  - `account_holder` (str): The name of the account holder.
  - `balance` (float): The current balance in the account.
- **Methods:**
  - `deposit(amount: float) -> None`: Adds `amount` to `balance`. Prints the new balance.
  - `withdraw(amount: float) -> None`: Subtracts `amount` from `balance` if funds are sufficient. Prints the new balance or an error message.

### Example Usage:

| Task                      | Inputs                                         | Expected Outputs                                         |
|---------------------------|------------------------------------------------|----------------------------------------------------------|
| Instantiate account       | `BankAccount("John Doe", 1000)`                | "Account for John Doe opened with balance $1000."        |
| Deposit money             | `account.deposit(500)`                         | "Deposited $500. New balance: $1500."                    |
| Withdraw money            | `account.withdraw(200)`                        | "Withdrew $200. New balance: $1300."                     |

---

## Exercise 3: Classroom Roster

**Objective:** Design a class `Classroom` to manage student enrollments and withdrawals.

### Specifications:
- **Instance Variables:**
  - `course_name` (str): The name of the course.
  - `roster` (list of str): A list of enrolled student names.
- **Methods:**
  - `add_student(name: str) -> None`: Adds `name` to `roster`. Prints the updated roster.
  - `remove_student(name: str) -> None`: Removes `name` from `roster` if present. Prints the updated roster or an error message.

### Example Usage:

| Task                      | Inputs                                            | Expected Outputs                                          |
|---------------------------|---------------------------------------------------|-----------------------------------------------------------|
| Instantiate classroom     | `Classroom("Biology 101")`                        | "Biology 101 classroom created."                          |
| Add student               | `classroom.add_student("Alice")`                  | "Alice added to the roster. Current roster: Alice."       |
| Remove student            | `classroom.remove_student("Alice")`               | "Alice removed from the roster. Current roster: ."        |

---

## Exercise 4: Pet Adoption System

**Objective:** Implement a class `Pet` to manage a pet adoption system.

### Specifications:
- **Class Variables:**
  - `total_pets`: Tracks the total number of pets available for adoption.
- **Instance Variables:**
  - `name` (str): The name of the pet.
  - `species` (str): The species of the pet (e.g., "Dog", "Cat").
  - `age` (int): The age of the pet in years.
  - `adopted` (bool): True if the pet is adopted, False otherwise.
- **Methods:**
  - `adopt() -> None`: Marks the pet as adopted by setting `adopted` to True. Prints a message indicating the pet has been adopted.
  - `return_pet() -> None`: Marks the pet as available for adoption by setting `adopted` to False. Prints a message indicating the pet has been returned.

### Example Usage:

| Task                        | Inputs                                | Expected Outputs                                      |
|-----------------------------|---------------------------------------|-------------------------------------------------------|
| Instantiate a pet object    | `Pet("Buddy", "Dog", 3)`              | "Pet 'Buddy' the Dog, aged 3, added to adoption list."|
| Adopt the pet               | `buddy.adopt()`                       | "'Buddy' has been adopted."                           |
| Return the pet              | `buddy.return_pet()`                  | "'Buddy' is now available for adoption again."        |

---

## Exercise 5: Grocery Store Inventory

**Objective:** Create a class `Item` to manage an inventory system for a grocery store.

### Specifications:
- **Class Variables:**
  - `inventory_count`: Tracks the total number of items in inventory.
- **Instance Variables:**
  - `product_name` (str): The name of the product.
  - `quantity` (int): The quantity of the product in stock.
  - `price` (float): The price of the product per unit.
- **Methods:**
  - `restock(quantity: int) -> None`: Adds `quantity` to the current stock. Prints the updated quantity.
  - `sell(quantity: int) -> None`: Subtracts `quantity` from the stock if available. Prints the updated quantity or an error message if insufficient stock.

### Example Usage:

| Task                        | Inputs                                        | Expected Outputs                                        |
|-----------------------------|-----------------------------------------------|---------------------------------------------------------|
| Instantiate an item object  | `Item("Milk", 50, 1.99)`                      | "Item 'Milk' with 50 units at $1.99 each added."        |
| Restock the item            | `milk.restock(100)`                           | "Restocked 'Milk'. New quantity: 150."                  |
| Sell the item               | `milk.sell(75)`                               | "Sold 75 units of 'Milk'. Quantity left: 75."           |



## Exercise 6: Event Planner

**Objective:** Develop an `Event` class to organize details and track attendees for events.

### Class Specifications:

- **Instance Variables:**
  - `name` (str): Name of the event.
  - `date` (str): Date of the event.
  - `attendees` (list): A list storing the names of event attendees.

- **Methods:**
  - `__init__(self, name: str, date: str)`: Constructor to initialize an event with a name, date, and an empty list for attendees.
  - `add_attendee(self, attendee_name: str)`: Adds a new attendee by name to the event.
  - `remove_attendee(self, attendee_name: str)`: Removes an attendee by name from the event, if they are listed.
  - `display_event_details(self)`: Outputs the event's details, including name, date, and a list of attendees.

### Tasks and Expected Inputs/Outputs:

| Task                  | Input Example                              | Expected Output                                                         |
|-----------------------|--------------------------------------------|-------------------------------------------------------------------------|
| **Add Event**         | `event = Event("Tech Conference", "2023-07-24")` | *No direct output, initializes an Event object*                           |
| **Add Attendee**      | `event.add_attendee("Alice")`              | *No direct output, but updates attendees list*                           |
| **Remove Attendee**   | `event.remove_attendee("Alice")`           | *No direct output, but updates attendees list if Alice was listed*       |
| **Display Event**     | `event.display_event_details()`            | "Event: Tech Conference, Date: 2023-07-24, Attendees: Alice, Bob" |

### Implementation Details:

- Ensure the `attendees` list is properly updated with each method call affecting it.
- The `display_event_details` method should neatly format and print all details of the event, including listing all attendees by name.

This corrected version aims to align class specifications with expected inputs/outputs and clarify the tasks involved in implementing the `Event` class.
