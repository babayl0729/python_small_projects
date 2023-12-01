# This application is program to 
# output the course, advisor,
# and students' information
# in discreet math course.
# Not only it will out the full name
# but also the students' major-minor
# and the what semester of the year
# they are currently in.

# To accomplish this small project:
# I used nested dictionary and list to
# properly listed the information of the students.

# Extract course and advisor name:
# To extract the course and advisor's name I used
# a print to return its name and to output it to
# the console.

# Extract students' information:
# I used for loop to iterate each students
# information from the dictionary.

student_list = {
    'course': 'Discreet Math',
    'advisor': 'Dr. Isabella Babay',
    'student': [
        {'full_name': 'Jaiden Smith', 'major-minor':['electrical engnr', 'math'], 'semester': 1},
         {'full_name': 'Zander Trumata', 'major-minor':['physics', 'math'], 'semester': 1},
          {'full_name': 'William Wilson', 'major-minor':['comp sci', 'systems tech'], 'semester': 1}
    ]
}


print(f"Welcome to {student_list['course']} course!")
print(f"Advisor: {student_list['advisor']}\n")

print("Student Information:")
for x,y in student_list["student"][0].items():
    print(f"{x}: {y}")

print("\n")
for x,y in student_list["student"][1].items():
    print(f"{x}: {y}")

print("\n")
for x,y in student_list["student"][2].items():
    print(f"{x}: {y}")