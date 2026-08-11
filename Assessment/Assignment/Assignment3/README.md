# Python Data Structures & Customer Analysis

## 📌 Project Overview

This project is a beginner-level Python business analysis exercise based on a simple customer support scenario.

The objective of this project was to understand how different Python data structures can be used to store, manage, update, and analyze business data.

As part of the exercise, I worked with **strings, lists, tuples, sets, and dictionaries** and applied them to practical customer-related tasks such as customer management, city analysis, satisfaction rating analysis, summary reporting, and customer search.

---

## 🎯 Business Scenario

A retail/customer support company wants to maintain basic customer information and generate simple business insights using Python.

The analysis includes:

* Managing customer records
* Updating customer information
* Identifying unique cities
* Finding the highest customer satisfaction rating
* Generating a customer summary report
* Searching for a customer using Customer ID

The purpose was to practice Python fundamentals through a simple business use case rather than only working with theoretical examples.

---

## 🛠️ Concepts Used

* Python
* Strings
* Lists
* Tuples
* Sets
* Dictionaries
* `for` loops
* `if` conditions
* `input()`
* Built-in functions such as `len()` and `max()`
* Dictionary methods such as `keys()` and `values()`
* List methods such as `append()`
* Set operations for unique values

---

## 📊 Data Structures Used

### 1. Lists

Lists were used to store collections of customer records.

```python
customers = [
    {
        "Customer_ID": "C101",
        "Name": "John",
        "City": "Chennai",
        "Satisfaction_Rating": 4.5
    },
    {
        "Customer_ID": "C102",
        "Name": "Mary",
        "City": "Coimbatore",
        "Satisfaction_Rating": 4.8
    },
    {
        "Customer_ID": "C103",
        "Name": "David",
        "City": "Madurai",
        "Satisfaction_Rating": 4.2
    }
]
```

I practiced accessing individual records using list indexing and working with dictionaries inside a list.

---

### 2. Tuples

Tuples were used to store fixed company information.

```python
company = ("ABC Support Services", "Coimbatore", 2015)
```

The tuple stores:

* Company Name
* Location
* Established Year

This helped me understand when fixed information can be stored using a tuple.

---

### 3. Sets

Sets were used to identify unique customer cities.

```python
cities = []

for customer in customers:
    cities.append(customer["City"])

unique_cities = set(cities)
```

This helped me understand how duplicate values can be removed when only unique information is required.

---

### 4. Dictionaries

Dictionaries were used to store structured customer information using key-value pairs.

Example:

```python
{
    "Customer_ID": "C101",
    "Name": "John",
    "City": "Chennai",
    "Satisfaction_Rating": 4.5
}
```

I practiced:

* Accessing values using keys
* Updating values
* Adding new fields
* Removing fields
* Displaying keys and values

---

## 🔄 Customer Data Operations

### Update Customer Information

Customer satisfaction rating was updated using Customer ID.

```python
for customer in customers:
    if customer["Customer_ID"] == "C102":
        customer["Satisfaction_Rating"] = 4.8
```

### Add a New Field

```python
customers[0]["Membership"] = "Gold"
customers[1]["Membership"] = "Silver"
customers[2]["Membership"] = "Gold"
```

### Remove a Field

```python
for customer in customers:
    del customer["Membership"]
```

### Display Keys and Values

```python
for customer in customers:
    print("Keys:", customer.keys())
    print("Values:", customer.values())
```

---

## 📈 Business Analysis

The customer data was used to answer simple business questions.

### Total Customers

```python
len(customers)
```

### Unique Cities

```python
unique_cities = set(cities)
```

### Highest Satisfaction Rating

```python
highest_rating = max(
    customer["Satisfaction_Rating"]
    for customer in customers
)

for customer in customers:
    if customer["Satisfaction_Rating"] == highest_rating:
        print(customer["Name"], "-", highest_rating)
```

Example output:

```text
Mary - 4.8
```

---

## 📋 Customer Summary Report

A simple summary report was generated using the analyzed customer information.

Example:

```text
Customer Summary Report

Total Customers: 3
Unique Cities: 3

Cities:
Chennai
Coimbatore
Madurai

Highest Satisfaction Rating:
Mary - 4.8

Company:
ABC Support Services
Coimbatore
Established: 2015
```

---

## 🔎 Customer Search Feature

As a bonus task, I created a simple customer search feature where the user can enter a Customer ID and retrieve the corresponding customer details.

```python
customer_id = input("Enter Customer ID: ")

found = False

for customer in customers:
    if customer["Customer_ID"] == customer_id:
        print(customer)
        found = True

if found == False:
    print("Customer not found")
```

Example:

```text
Enter Customer ID: C102

{'Customer_ID': 'C102',
 'Name': 'Mary',
 'City': 'Coimbatore',
 'Satisfaction_Rating': 4.8}
```

If the entered ID does not exist:

```text
Customer not found
```

---

## 📚 What I Learned

Through this project, I learned how basic Python data structures can be applied to a practical business problem.

### Key Learning

* How to manipulate strings using built-in methods.
* How to store and manage collections using lists.
* How to use tuples for fixed information.
* How to use sets to identify unique values.
* How to use dictionaries for structured business data.
* How to combine lists and dictionaries to represent customer records.
* How to use loops and conditions to process business data.
* How to use built-in functions such as `len()` and `max()`.
* How to perform basic data analysis using Python.
* How to create a simple business summary report.
* How to build a basic customer search feature.

Most importantly, this exercise helped me understand how Python fundamentals can be connected to **real-world data analysis scenarios**.

---

## 📁 Project Structure

```text
Python-Data-Structures-Customer-Analysis/
│
├── Customer_Analysis.ipynb
├── README.md
└── screenshots/
    └── customer_summary_output.png
```

---

## 📸 Output Screenshot

The output screenshot shows the customer summary report and the results of the basic business analysis.

 <img width="1137" height="428" alt="image" src="https://github.com/user-attachments/assets/dbe706a8-fe39-4d2c-a686-3de8c9c65f05" />

---

## 🚀 Future Improvements

This project can be extended further by:

* Adding more customer records
* Reading customer data from CSV or Excel files
* Using Pandas for larger datasets
* Adding more business metrics
* Creating interactive reports
* Adding data validation for user input
* Building a simple customer dashboard

---

## 👩‍💻 Project Takeaway

This project gave me hands-on practice with Python data structures and helped me move from learning individual Python concepts to applying them together in a simple business scenario.

It also gave me a better understanding of how basic programming logic can be used for **data preparation, analysis, and reporting**.
