import tkinter as tk
from tkinter import messagebox
from admin import Admin
from doctor import Doctor
from patient import Patient

class HospitalGUI:
    def __init__(self, master, admin, doctors, patients, discharged_patients):
        self.master = master
        self.admin = admin
        self.doctors = doctors
        self.patients = patients
        self.discharged_patients = discharged_patients

        self.master.title("Hospital Management System")
        self.master.configure(bg='Lavender')  
        self.master.geometry("200x150")  
        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()
        tk.Label(self.master, text="Admin Login",font=("Helvetica", 16, "bold")).pack(pady=5)
        tk.Label(self.master, text="Username:").pack()
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack()
        tk.Label(self.master, text="Password:").pack()
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()
        login_button = tk.Button(self.master, text="Login", command=self.login)
        login_button.configure(bg='LightSkyBlue')
        login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.admin.login(username, password):
            self.create_main_dashboard()
        else:
            messagebox.showerror("Error", "Invalid login credentials")

    def create_main_dashboard(self):
        self.clear_screen()
        button_bg = 'LightBlue'  
        self.master.configure(bg='SkyBlue') 
        self.master.geometry("500x400")  

        tk.Label(self.master, text="Main Menu",font=("Helvetica", 16, "bold")).pack()
        tk.Button(self.master, text="Manage Doctors", command=self.manage_doctors, bg=button_bg).pack(pady=5)
        tk.Button(self.master, text="View Patients", command=self.view_patients, bg=button_bg).pack(pady=5)
        tk.Button(self.master, text="Discharge Patient", command=self.discharge_patient, bg=button_bg).pack(pady=5)
        tk.Button(self.master, text="View Discharged Patients", command=self.view_discharged_patients, bg=button_bg).pack(pady=5)
        tk.Button(self.master, text="Assign Doctor to Patient", command=self.assign_doctor_to_patient, bg=button_bg).pack(pady=5)
        tk.Button(self.master, text="Update Admin Details", command=self.update_admin_details, bg=button_bg).pack(pady=5)
        tk.Button(self.master, text="Get Management Report", command=self.get_management_report, bg=button_bg).pack(pady=5)
        tk.Button(self.master, text="View Patients from Same Family", command=self.view_patients_from_same_family, bg=button_bg).pack(pady=5)
        tk.Button(self.master, text="Relocate Doctor of Patients", command=self.relocate_doctor, bg=button_bg).pack(pady=5)
        tk.Button(self.master, text="Quit", command=self.quit, bg='red').pack(pady=5)

    def manage_doctors(self):
        self.clear_screen()
        button_bg = 'LightPink' 
        self.master.configure(bg='LightCoral') 
        self.master.geometry("400x300") 

        tk.Label(self.master, text="Choose From the Operation Below",font=("Helvetica", 16, "bold")).pack() 
        tk.Button(self.master, text="Register Doctor", command=self.register_doctor, bg=button_bg).pack(pady=5)
        tk.Button(self.master, text="View Doctors", command=self.view_doctors, bg=button_bg).pack(pady=5)
        tk.Button(self.master, text="Update Doctor", command=self.update_doctor, bg=button_bg).pack(pady=5)
        tk.Button(self.master, text="Delete Doctor", command=self.delete_doctor, bg=button_bg).pack(pady=5)
        tk.Button(self.master, text="Back to Main Menu", command=self.create_main_dashboard, bg='LightBlue').pack(pady=5)

    def register_doctor(self):
        self.clear_screen()
        self.master.configure(bg='LightPink') 
        tk.Label(self.master, text="Enter Doctor Detail",font=("Helvetica", 16, "bold")).pack() 
        tk.Label(self.master, text="First Name:").pack()
        self.first_name_entry = tk.Entry(self.master)
        self.first_name_entry.pack()
        tk.Label(self.master, text="Surname:").pack()
        self.surname_entry = tk.Entry(self.master)
        self.surname_entry.pack()
        tk.Label(self.master, text="Speciality:").pack()
        self.speciality_entry = tk.Entry(self.master)
        self.speciality_entry.pack()
        tk.Button(self.master, text="Register", command=self.add_doctor, bg='LightBlue').pack(pady=5)
        tk.Button(self.master, text="Back to Manage Doctors", command=self.manage_doctors, bg='LightBlue').pack(pady=5)

    def add_doctor(self):
        first_name = self.first_name_entry.get()
        surname = self.surname_entry.get()
        speciality = self.speciality_entry.get()
        if any(doc.get_first_name() == first_name and doc.get_surname() == surname for doc in self.doctors):
            messagebox.showerror("Error", "Doctor already exists.")
        else:
            self.doctors.append(Doctor(first_name, surname, speciality))
            messagebox.showinfo("Success", "Doctor registered.")
            self.manage_doctors()

    def view_doctors(self):
        self.clear_screen()
        self.master.configure(bg='LightPink')
        tk.Label(self.master, text="Admin Login",font=("Helvetica", 16, "bold")).pack()  
        for doctor in self.doctors:
            tk.Label(self.master, text=str(doctor)).pack()
        tk.Button(self.master, text="Back to Manage Doctors", command=self.manage_doctors, bg='LightBlue').pack(pady=5)

    def update_doctor(self):
        self.clear_screen()
        self.master.configure(bg='LightPink')  
        tk.Label(self.master, text="Choose Doctor To Update",font=("Helvetica", 16, "bold")).pack()
        tk.Label(self.master, text="Enter Doctor ID:").pack()
        self.doctor_id_entry = tk.Entry(self.master)
        self.doctor_id_entry.pack()
        tk.Button(self.master, text="Update", command=self.update_doctor_details, bg='LightBlue').pack(pady=5)
        tk.Button(self.master, text="Back to Manage Doctors", command=self.manage_doctors, bg='LightBlue').pack(pady=5)

    def update_doctor_details(self):
        doctor_id = int(self.doctor_id_entry.get()) - 1
        if 0 <= doctor_id < len(self.doctors):
            doctor = self.doctors[doctor_id]
            self.clear_screen()
            self.master.configure(bg='LightPink')  
            tk.Label(self.master, text="Update First Name:").pack()
            self.update_first_name_entry = tk.Entry(self.master)
            self.update_first_name_entry.insert(0, doctor.get_first_name())
            self.update_first_name_entry.pack()
            tk.Label(self.master, text="Update Surname:").pack()
            self.update_surname_entry = tk.Entry(self.master)
            self.update_surname_entry.insert(0, doctor.get_surname())
            self.update_surname_entry.pack()
            tk.Label(self.master, text="Update Speciality:").pack()
            self.update_speciality_entry = tk.Entry(self.master)
            self.update_speciality_entry.insert(0, doctor.get_speciality())
            self.update_speciality_entry.pack()
            tk.Button(self.master, text="Save", command=lambda: self.save_doctor_updates(doctor), bg='LightBlue').pack(pady=5)
            tk.Button(self.master, text="Back to Manage Doctors", command=self.manage_doctors, bg='LightBlue').pack(pady=5)
        else:
            messagebox.showerror("Error", "Doctor ID not found.")

    def save_doctor_updates(self, doctor):
        doctor.set_first_name(self.update_first_name_entry.get())
        doctor.set_surname(self.update_surname_entry.get())
        doctor.set_speciality(self.update_speciality_entry.get())
        messagebox.showinfo("Success", "Doctor details updated.")
        self.manage_doctors()

    def delete_doctor(self):
        self.clear_screen()
        self.master.configure(bg='LightPink')  
        tk.Label(self.master, text="Choose Doctor To Delete",font=("Helvetica", 16, "bold")).pack()
        tk.Label(self.master, text="Enter Doctor ID:").pack()
        self.delete_doctor_id_entry = tk.Entry(self.master)
        self.delete_doctor_id_entry.pack()
        tk.Button(self.master, text="Delete", command=self.remove_doctor, bg='LightBlue').pack(pady=5)
        tk.Button(self.master, text="Back to Manage Doctors", command=self.manage_doctors, bg='LightBlue').pack(pady=5)

    def remove_doctor(self):
        doctor_id = int(self.delete_doctor_id_entry.get()) - 1
        if 0 <= doctor_id < len(self.doctors):
            self.doctors.pop(doctor_id)
            messagebox.showinfo("Success", "Doctor deleted.")
        else:
            messagebox.showerror("Error", "Doctor ID not found.")
        self.manage_doctors()

    def view_patients(self):
        self.clear_screen()
        self.master.configure(bg='LightGreen')  
        for patient in self.patients:
            tk.Label(self.master, text=str(patient)).pack()
        tk.Button(self.master, text="Back to Main Menu", command=self.create_main_dashboard, bg='LightBlue').pack(pady=5)

    def discharge_patient(self):
        self.clear_screen()
        tk.Label(self.master, text="Enter Patient ID:").pack()
        self.discharge_patient_id_entry = tk.Entry(self.master)
        self.discharge_patient_id_entry.pack()
        tk.Button(self.master, text="Discharge", command=self.discharge_selected_patient).pack()
        mainmenu_button = tk.Button(self.master, text="Back to Main Menu", command=self.create_main_dashboard)
        mainmenu_button.configure(bg='LightSkyBlue')
        mainmenu_button.pack()

    def discharge_selected_patient(self):
        patient_id = int(self.discharge_patient_id_entry.get()) - 1
        if 0 <= patient_id < len(self.patients):
            self.discharged_patients.append(self.patients.pop(patient_id))
            messagebox.showinfo("Success", "Patient discharged.")
        else:
            messagebox.showerror("Error", "Patient ID not found.")
        self.create_main_dashboard()

    def view_discharged_patients(self):
        self.clear_screen()
        for patient in self.discharged_patients:
            tk.Label(self.master, text=str(patient)).pack()
        mainmenu_button = tk.Button(self.master, text="Back to Main Menu", command=self.create_main_dashboard)
        mainmenu_button.configure(bg='LightSkyBlue')
        mainmenu_button.pack()

    def assign_doctor_to_patient(self):
        self.clear_screen()
        tk.Label(self.master, text="Enter Patient ID:").pack()
        self.patient_id_entry = tk.Entry(self.master)
        self.patient_id_entry.pack()
        tk.Label(self.master, text="Enter Doctor ID:").pack()
        self.doctor_id_entry = tk.Entry(self.master)
        self.doctor_id_entry.pack()
        tk.Button(self.master, text="Assign", command=self.assign_doctor).pack()
        mainmenu_button = tk.Button(self.master, text="Back to Main Menu", command=self.create_main_dashboard)
        mainmenu_button.configure(bg='LightSkyBlue')
        mainmenu_button.pack()

    def assign_doctor(self):
        patient_id = int(self.patient_id_entry.get()) - 1
        doctor_id = int(self.doctor_id_entry.get()) - 1
        if 0 <= patient_id < len(self.patients) and 0 <= doctor_id < len(self.doctors):
            self.patients[patient_id].link(self.doctors[doctor_id].full_name())
            self.doctors[doctor_id].add_patient(self.patients[patient_id])
            messagebox.showinfo("Success", "Doctor assigned to patient.")
        else:
            messagebox.showerror("Error", "Invalid Patient or Doctor ID.")
        self.create_main_dashboard()

    def update_admin_details(self):
        self.clear_screen()
        tk.Label(self.master, text="Update Username:").pack()
        self.update_username_entry = tk.Entry(self.master)
        self.update_username_entry.insert(0, self.admin._Admin__username)
        self.update_username_entry.pack()
        tk.Label(self.master, text="Update Password:").pack()
        self.update_password_entry = tk.Entry(self.master, show="*")
        self.update_password_entry.insert(0, self.admin._Admin__password)
        self.update_password_entry.pack()
        tk.Label(self.master, text="Update Address:").pack()
        self.update_address_entry = tk.Entry(self.master)
        self.update_address_entry.insert(0, self.admin._Admin__address)
        self.update_address_entry.pack()
        tk.Button(self.master, text="Save", command=self.save_admin_updates).pack()
        mainmenu_button = tk.Button(self.master, text="Back to Main Menu", command=self.create_main_dashboard)
        mainmenu_button.configure(bg='LightSkyBlue')
        mainmenu_button.pack()

    def save_admin_updates(self):
        self.admin._Admin__username = self.update_username_entry.get()
        self.admin._Admin__password = self.update_password_entry.get()
        self.admin._Admin__address = self.update_address_entry.get()
        messagebox.showinfo("Success", "Admin details updated.")
        self.create_main_dashboard()

    def get_management_report(self):
        self.clear_screen()
        tk.Label(self.master, text="-----Management Reports-----",font=("Helvetica", 16, "bold")).pack(pady=5)
        tk.Label(self.master, text="Choose from operation:",font=("Helvetica", 13, "bold")).pack(pady=5)
        tk.Button(self.master, text="1 - Total number of doctors in the system", command=lambda: self.display_management_report(1)).pack()
        tk.Button(self.master, text="2 - Total number of patients per doctor", command=lambda: self.display_management_report(2)).pack()
        tk.Button(self.master, text="3 - Total number of appointments per month per doctor", command=lambda: self.display_management_report(3)).pack()
        tk.Button(self.master, text="4 - Total number of patients based on the illness type.", command=lambda: self.display_management_report(4)).pack()
        mainmenu_button = tk.Button(self.master, text="Back to Main Menu", command=self.create_main_dashboard)
        mainmenu_button.configure(bg='LightSkyBlue')
        mainmenu_button.pack()

    def display_management_report(self, option):
        self.clear_screen()

        if option == 1:
            tk.Label(self.master, text=f"The total number of doctors: {len(self.doctors)}").pack()
            
        elif option == 2:
            for doctor in self.doctors:
                total_patients = doctor.get_total_patients()
                tk.Label(self.master, text=f"{doctor.full_name()} has {total_patients} patients").pack()
        elif option == 3:
            for doctor in self.doctors:
                total_appointments = doctor.get_total_appointments()
                tk.Label(self.master, text=f"{doctor.full_name()} has {total_appointments} this month").pack()
        elif option == 4:
            symptoms_list = {}

            for patient in self.patients:
                for symptom in patient.get_symptoms():
                    if symptom in symptoms_list:
                        symptoms_list[symptom] += 1
                    else:
                        symptoms_list[symptom] = 1
            
            for symptom, count in symptoms_list.items():
                tk.Label(self.master, text=f"The total number of patients with {symptom}: {count}").pack()

        report_button = tk.Button(self.master, text="Back to Management Reports", command=self.get_management_report)
        report_button.configure(bg='LightSkyBlue')
        report_button.pack()
       
        mainmenu_button = tk.Button(self.master, text="Back to Main Menu", command=self.create_main_dashboard)
        mainmenu_button.configure(bg='LightSkyBlue')
        mainmenu_button.pack()

    def view_patients_from_same_family(self):
        self.clear_screen()
        tk.Label(self.master, text="Enter Family Name:").pack()
        self.family_name_entry = tk.Entry(self.master)
        self.family_name_entry.pack()
        tk.Button(self.master, text="View", command=self.display_patients_from_same_family).pack()
     
        mainmenu_button = tk.Button(self.master, text="Back to Main Menu", command=self.create_main_dashboard)
        mainmenu_button.configure(bg='LightSkyBlue')
        mainmenu_button.pack()

    def display_patients_from_same_family(self):
        family_name = self.family_name_entry.get().strip().lower()
        self.clear_screen()
        same_family_patients = [patient for patient in self.patients if patient.get_surname().strip().lower() == family_name]
        if same_family_patients:
            for patient in same_family_patients:
                tk.Label(self.master, text=str(patient)).pack()
        else:
            tk.Label(self.master, text="No patients found from the same family.").pack()
        
        mainmenu_button = tk.Button(self.master, text="Back to Main Menu", command=self.create_main_dashboard)
        mainmenu_button.configure(bg='LightSkyBlue')
        mainmenu_button.pack()

    def relocate_doctor(self):
        self.clear_screen()
        tk.Label(self.master, text="-----Relocate Doctor-----").pack()
        if len(self.patients) != 0:
            tk.Label(self.master, text="-----List of Patients-----").pack()
            for idx, patient in enumerate(self.patients, start=1):
                tk.Label(self.master, text=f"{idx}. {patient}").pack()
            tk.Label(self.master, text="Enter the ID of the patient to relocate the doctor from:").pack()
            self.patient_index_entry = tk.Entry(self.master)
            self.patient_index_entry.pack()
            tk.Button(self.master, text="Next", command=self.select_new_doctor).pack()
        else:
            tk.Label(self.master, text="No patients available for relocation.").pack()
            tk.Button(self.master, text="Back to Main Menu", command=self.create_main_dashboard).pack()

    def select_new_doctor(self):
        patient_index = int(self.patient_index_entry.get()) - 1
        if 0 <= patient_index < len(self.patients):
            self.clear_screen()
            tk.Label(self.master, text="-----List of Doctors-----").pack()
            for idx, doctor in enumerate(self.doctors, start=1):
                tk.Label(self.master, text=f"{idx}. {doctor}").pack()
            tk.Label(self.master, text="Enter the ID of the new doctor:").pack()
            self.new_doctor_index_entry = tk.Entry(self.master)
            self.new_doctor_index_entry.pack()
            tk.Button(self.master, text="Relocate", command=lambda: self.relocate_doctor_to_new(patient_index)).pack()
        else:
            messagebox.showerror("Error", "Invalid patient ID. Check your input.")
            self.relocate_doctor()

    def relocate_doctor_to_new(self, patient_index):
        new_doctor_index = int(self.new_doctor_index_entry.get()) - 1
        if 0 <= new_doctor_index < len(self.doctors):
            old_doctor_full_name = self.patients[patient_index].get_doctor()
            self.patients[patient_index].link(self.doctors[new_doctor_index].full_name())
            self.doctors[new_doctor_index].add_patient(self.patients[patient_index])
            messagebox.showinfo("Success", f"Successfully relocated {old_doctor_full_name} to {self.doctors[new_doctor_index].full_name()}.")
            self.create_main_dashboard()
        else:
            messagebox.showerror("Error", "Invalid new doctor ID. Check your input.")
            self.relocate_doctor()

    def clear_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def quit(self):
        self.master.destroy()