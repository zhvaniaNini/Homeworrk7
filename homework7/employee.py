from db import c


class Employee:

    def __init__(self, id, first_name, last_name, age):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def get_employee_by_id(cls, id):
        result = c.execute("SELECT * FROM employee WHERE id = ?", (id,))
        value = result.fetchone()
        if value is None:
            return None
        return Employee(value[0], value[1], value[2], value[3])

    @classmethod
    def get_list_with_name(cls, name):
        result = c.execute("SELECT * FROM employee WHERE first_name = ?", (name,))
        values = result.fetchall()
        employees = []
        for value in values:
            employees.append(Employee(value["id"], value["first_name"], value["last_name"], value["age"]))
        return employees

    @classmethod
    def get_list_with_name_and_surname(cls, name, surname):
        result = c.execute("SELECT * FROM employee WHERE first_name = ? AND last_name = ?", (name, surname))
        values = result.fetchall()
        employees = []
        for value in values:
            employees.append(Employee(value["id"], value["first_name"], value["last_name"], value["age"]))
        return employees

    @classmethod
    def get_list_with_name_surname_age(cls, name, surname, age):
        result = c.execute("SELECT * FROM employee WHERE first_name = ? AND last_name = ? AND age = ?",
                           (name, surname, age))
        values = result.fetchall()
        employees = []
        for value in values:
            employees.append(Employee(value["id"], value["first_name"], value["last_name"], value["age"]))
        return employees

    def update(self):
        c.execute("UPDATE employee SET first_name = ?, last_name = ?, age = ? WHERE id = ?",
                  (self.first_name, self.last_name, self.age, self.id))

    def create(self):
        c.execute("INSERT INTO employee (first_name, last_name, age) VALUES (?, ?, ?)",
                  (self.first_name, self.last_name, self.age))
        self.id = c.lastrowid

    def delete(self):
        if self.id is not None:
            c.execute("DELETE FROM employee WHERE id = ?", (self.id,))
        else:
            print("Cannot delete: Employee object has not been saved to the database")

    def __gt__(self, other):
        return self.age > other.age

    def __repr__(self):
        return "<Employee {}>".format(self.first_name)
