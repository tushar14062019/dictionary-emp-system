# **Case Study: Employee Management System using Python Dictionaries**

## **Objective**

Develop a Python-based Employee Management System that stores and manipulates employee records using dictionaries. The system should allow adding, updating, removing, and searching employees while enforcing data validations. Additionally, it should support sorting employees based on different criteria.

---

## **System Requirements**

The system should support the following functionalities:

1. **Add a new employee**
   - Validate that Employee ID is unique.
   - Ensure proper data format for name, age, and department.
2. **Remove an employee**
   - Allow removal only if the Employee ID exists.
3. **Update employee details**
   - Modify name, age, or department while maintaining data integrity.
4. **Search employees**
   - Search by Employee ID or by name (case-insensitive).
5. **Sort employees**
   - Sort by name, age, or department.

---

## **Implementation Details**

### **1. Data Structure**

A Python dictionary will store employee details where:

- The **keys** are unique Employee IDs.
- The **values** are dictionaries containing employee details.

Example structure:

```python
employees = {
   "E101": {"name": "Alice Johnson", "age": 30, "department": "HR"},
   "E102": {"name": "Bob Smith", "age": 25, "department": "IT"}
}
```

---

### **2. Functionalities**

#### **a. Add an Employee**

- Prompt for Employee ID, Name, Age, and Department.
- Ensure Employee ID is unique.
- Validate that Name contains only alphabets.
- Ensure Age is a positive integer.
- Add to the dictionary if all validations pass.

#### **b. Remove an Employee**

- Check if Employee ID exists before deletion.
- Remove the employee from the dictionary.

#### **c. Update Employee Details**

- Allow modification of name, age, or department.
- Validate updated values before applying changes.

#### **d. Search Employees**

- Search by Employee ID.
- Search by Name (case-insensitive).

#### **e. Sort Employees**

- Sort by Name (alphabetical order).
- Sort by Age (ascending order).
- Sort by Department.

---

## **Key Learning Outcomes**

- Using **dictionaries** for structured data storage.
- Performing **CRUD (Create, Read, Update, Delete)** operations.
- Implementing **validations** for data integrity.
- Searching within dictionaries using **case-insensitive search**.
- Sorting dictionaries based on different criteria.

---

## **Next Steps**

- Extend functionality to allow exporting data to a file (CSV/JSON).
- Implement a simple command-line menu for better user interaction.
- Consider integrating with a database for persistence.

---

### **License**
This project is licensed under the MIT License - feel free to modify and distribute.

---

### **Contributing**
If you’d like to contribute, please fork the repository and submit a pull request.

