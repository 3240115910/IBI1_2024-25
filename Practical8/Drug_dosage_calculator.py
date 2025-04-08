#create	a new Python class named patients
#use two functions to record and print the information of the patient
class patients:
    def __init__(x, name, age, date_of_latest_admission, medical_history):
        x.name = name
        x.age = age
        x.date_of_latest_admission = date_of_latest_admission
        x.medical_history = medical_history
    def print(x):
        print(f"Name: {x.name}, Age: {x.age}, Date of Latest Admission: {x.date_of_latest_admission}, Medical History: {x.medical_history}")
# an example about myself
patient = patients("Jiarui", 18, "2023-10-01", "Flu in 2020")
patient.print()