from employee import Employee

emp1 = Employee(1, "nini", "Zhvania", 19)

emp1.create()

emp = Employee.get_employee_by_id(1)

if emp is not None:
    print("Fetched employee:", emp.__dict__)
else:
    print("No employee found with the specified ID")

emp1.age = 20
emp1.update()
print("Employee age updated")

updated_emp = Employee.get_employee_by_id(emp1.id)
print("Updated employee:", updated_emp.__dict__)

emp1.delete()
print("Employee deleted")

deleted_emp = Employee.get_employee_by_id(1)
print("Deleted employee:", deleted_emp)
