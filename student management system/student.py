# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 12:53:16 2025

@author: SUBHASHINI
"""

import json
import os
DATA_FILE= "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    else:
        return []
    
#saving data to file after taking inputs from user

def save_data(data):
    with open(DATA_FILE,"w") as f:
        json.dump(data, f, indent=4)
        
        
#adding the features to find out whatever is necessary

def add_student():
    data=load_data()
    try:
        name=input("Please input the student's name:")
        roll=int(input("Please enter student roll number:"))
        marks=float(input("Please enter your marks:"))
    except ValueError:
        print("X, INVALID INPUT, TRY AGAIN!")
        return
    
    #checking for unique roll numbers:
    for student in data:
        if student["roll"] == roll:
            print(" Roll number already exists!")
            return
    new_student = {"name": name, "roll": roll, "marks": marks}
    data.append(new_student)
    save_data(data)
    print("_____/Student added successfully!\n")
    

def list_students():
    data = load_data()
    if not data:
        print("No students found!\n")
        return

    print("\n Student List:")
    for s in data:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")
    print()
    
def show_average():
    data = load_data()
    if not data:
        print("No data available!\n")
        return

    avg = sum(s["marks"] for s in data) / len(data)
    print(f" Average Marks: {avg:.2f}\n")


#DISPLAYING THE MENU TO SHOW THE USERS

def main():
    while True:
        print("===== Student Marks Management System =====")
        print("1. Add Student")
        print("2. List Students")
        print("3. Show Average Marks")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            list_students()
        elif choice == "3":
            show_average()
        elif choice == "4":
            print("Bye! Exiting program.")
            break
        else:
            print("X. Invalid choice. Try again!\n")
            
#MAKING THE ENTIRE PROGRAM RUN

if __name__ == "__main__":
    main()

                