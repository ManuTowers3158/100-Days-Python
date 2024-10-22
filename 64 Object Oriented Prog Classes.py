# This script defines a basic job class structure and two specific job roles, "doctor" and "teacher", 
# each with their own specialized attributes. The script then demonstrates creating objects from these classes 
# and displaying their details.

# Base class for general job attributes
class job:
    name = None  # Job title
    salary = None  # Salary for the job
    work_hours = None  # Work hours for the job

    # Constructor to initialize the base class with name, salary, and work hours
    def __init__(self, name, salary, work_hours):
        self.name = name
        self.salary = salary
        self.work_hours = work_hours

    # Method to print a summary of the job details
    def Summary(self):
        print(f"Job: {self.name}\nSalary: {self.salary},\nWork Hours: {self.work_hours}")


# Doctor class inheriting from job class
class doctor(job):
    speciality = None  # Doctor's speciality
    years_exp = None  # Years of experience

    # Constructor to initialize the doctor class with speciality and years of experience
    def __init__(self, speciality, years_exp):
        self.name = "Doctor"  # Set default job title
        self.salary = "$300,000"  # Set default salary for doctor
        self.work_hours = "50"  # Set default work hours for doctor
        self.speciality = speciality  # Set speciality
        self.years_exp = years_exp  # Set years of experience

    # Override method to print a summary of the doctor's details
    def Summary(self):
        print(
            f"Job: {self.name}\nSalary: {self.salary},\nWork Hours: {self.work_hours}\nSpeciality: {self.speciality}\nYears of Experience: {self.years_exp}")


# Teacher class inheriting from job class
class teacher(job):
    subject = None  # Subject the teacher teaches
    position = None  # Position or title of the teacher

    # Constructor to initialize the teacher class with subject and position
    def __init__(self, subject, position):
        self.name = "Teacher"  # Set default job title
        self.salary = "$80,000"  # Set default salary for teacher
        self.work_hours = "30"  # Set default work hours for teacher
        self.subject = subject  # Set subject
        self.position = position  # Set position

    # Override method to print a summary of the teacher's details
    def Summary(self):
        print(
            f"Job: {self.name}\nSalary: {self.salary},\nWork Hours: {self.work_hours}\nSubject: {self.subject}\nPosition: {self.position}")


# Create an Engineer object using the base job class
Engineer = job("Engineer", "$180,000", "48")
print(Engineer.salary)  # Print the engineer's salary
job.Summary(Engineer)  # Call the base class method to display the job summary

print()

# Create a Surgeon object using the doctor subclass
surgeon = doctor("Surgeon", "10")  # Speciality is "Surgeon" with 10 years of experience
doctor.Summary(surgeon)  # Call the subclass method to display the doctor's details

print()

# Create a HeadMaster object using the teacher subclass
HeadMaster = teacher("Head Master",
                     "Advanced Robotics")  # Subject is "Head Master" with position in "Advanced Robotics"
teacher.Summary(HeadMaster)  # Call the subclass method to display the teacher's details
