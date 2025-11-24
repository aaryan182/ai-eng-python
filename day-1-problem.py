# Create a python script that has a list of 10 user names , filter those whose name starts with "A", count how many names start with "A"

users = ["Aaryan", "Rohan", "Amit", "Sneha", "Anya", "Rahul", "Aakash", "Meera", "Arjun", "Tina"]

a_users = [u for u in users if u.startswith("A")]

count_a = len(a_users)
