import sys
if len(sys.argv) == 3:
    script_name = sys.arvg[0]
    name = sys.arvg[1]
    rollno = sys.arvg[2]
    print("User provided input values:")
else:
    script_name = sys.arvg[0]
    name = "pratibha"
    rllno = "055"
    print("No input given - using default values:")
    
print("Script Name:",script_name)
print("Student Name:",name)
print("Roll Number:",rollno)
