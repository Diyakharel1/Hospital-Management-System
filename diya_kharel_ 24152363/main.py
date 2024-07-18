from admin import Admin
from doctor import Doctor
from patient import Patient
from gui import HospitalGUI 
import tkinter as tk

def main():
    # Initializing admin, doctors, and patients
    admin = Admin('admin', '123', 'B1 1AB')
    doctors = [
        Doctor('John', 'Smith', 'Internal Med.'),
        Doctor('Jane', 'Doe', 'Pediatrics'),
        Doctor('Carlos', 'Johnson', 'Cardiology')
    ]
    patients = [
        Patient('Sara', 'Smith', 20, '07012345678', 'B1 234',['flu', 'headache']),
        Patient('Mike', 'Jones', 37, '07555551234', 'L2 2AB',['vomitting', 'fever']),
        Patient('David', 'Smith', 15, '07123456789', 'C1 ABC',['fever'])
    ]
    discharged_patients = []

    # Creating and adding a new patient
    new_patient = Patient('Diya', 'Kharel', 25, '07987654321', 'A1 3CD', ['covid', 'headache'])
    patients.append(new_patient)

    # Initialize Tkinter and create the GUI instance
    root = tk.Tk()
    app = HospitalGUI(root, admin, doctors, patients, discharged_patients)
    root.mainloop()

if __name__ == '__main__':
    main()