Student_Name = ["Sujoy", "Subha", "Sumit", "Souvik"]

for name in Student_Name:
    print(name, end="-")

# Add a new student
Student_Name.append("Subhadip")
print("\n", Student_Name)

# Check if specific students are in the list
if "Subhadip" in Student_Name:
    print("Subhadip in college")
if "Souvik" in Student_Name:
    print("Souvik in college")
else:
    print("Student not in college")
