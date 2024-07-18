class Doctor:
    _id_counter = 1

    def __init__(self, first_name, surname, speciality):
        self.__id = Doctor._id_counter
        Doctor._id_counter += 1
        self.__first_name = first_name
        self.__surname = surname
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = []

    def full_name(self):
        return f"{self.__first_name} {self.__surname}"

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name

    def get_surname(self):
        return self.__surname

    def set_surname(self, new_surname):
        self.__surname = new_surname

    def get_speciality(self):
        return self.__speciality
    
    def get_symptoms(self):
        return len(self.__patients)

    def set_speciality(self, new_speciality):
        self.__speciality = new_speciality

    def add_patient(self, patient):
        self.__patients.append(patient)

    def add_patient(self, patient):
        self.__patients.append(patient)

    def get_total_patients(self):
        return len(self.__patients)
    
    def get_total_appointments(self):
        return len(self.__appointments)
    
    def get_id(self):
        return self.__id

    def __str__(self):
        return f"{self.__id:^5}|{self.full_name():^30}|{self.__speciality:^15}"
    

