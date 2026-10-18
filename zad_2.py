#- Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas tworzenia instancji klasy za pośrednictwem konstruktora.
#    - Stworzyć 2 biblioteki (2 instancje klasy), 5 książek, 3 pracowników, 3 studentów, oraz 2 zamówienia.
#    - Wyświetlić oba zamówienia (`print`)
class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if not self.marks:
            return False
        average = sum(self.marks) / len(self.marks)
        return average > 50

class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library in {self.city}, {self.street}, {self.zip_code}, Open hours: {self.open_hours}, Phone: {self.phone}"

class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str, birth_date: str, city: str, street: str, zip_code: str, phone: str):
            self.first_name = first_name
            self.last_name = last_name
            self.hire_date = hire_date
            self.birth_date = birth_date
            self.city = city
            self.street = street
            self.zip_code = zip_code
            self.phone = phone

    def __str__(self):
            return f"Employee: {self.first_name} {self.last_name}, Hired on: {self.hire_date}, Born on: {self.birth_date}, Address: {self.city}, {self.street}, {self.zip_code}, Phone: {self.phone}"
        
class Book:
    def __init__(self, library: Library, publication_date: str, author_name: str, author_surname: str, number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book by {self.author_name} {self.author_surname}, Published on: {self.publication_date}, Pages: {self.number_of_pages}, Library: {self.library}"

class Order:
    def __init__(self, employee: Employee, student: Student, books: list, order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = ', '.join(str(book) for book in self.books)
        return f"Order placed by {self.student.name} on {self.order_date}, Processed by: {self.employee.first_name} {self.employee.last_name}, Books: [{books_str}]"

library1 = Library("New York", "5th Avenue", "10001", "9 AM - 5 PM", "123-456-7890")    
library2 = Library("Los Angeles", "Sunset Boulevard", "90001", "10 AM - 6 PM", "987-654-3210")
book1 = Book(library1, "2020-01-01", "John", "Doe", 300)
book2 = Book(library1, "2019-05-15", "Jane", "Smith", 250)
book3 = Book(library2, "2021-07-20", "Alice", "Johnson", 400)
book4 = Book(library2, "2018-03-10", "Bob", "Brown", 150)
book5 = Book(library1, "2022-11-05", "Charlie", "Davis", 350)
employee1 = Employee("Emily", "Clark", "2020-02-01", "1990-06-15", "New York", "5th Avenue", "10001", "123-456-7890")
employee2 = Employee("Michael", "Johnson", "2019-08-15", "1985-12-20", "Los Angeles", "Sunset Boulevard", "90001", "987-654-3210")
employee3 = Employee("Sarah", "Williams", "2021-05-10", "1992-03-25", "Chicago", "Michigan Avenue", "60601", "555-123-4567")
student1 = Student("Alice", [60, 70, 80])
student2 = Student("Bob", [40, 30, 20])
student3 = Student("Charlie", [90, 85, 95])
order1 = Order(employee1, student1, [book1, book2], "2023-09-01")
order2 = Order(employee2, student2, [book3, book4, book5], "2023-09-02")
print(order1)
print(order2)   