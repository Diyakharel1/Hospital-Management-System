from person import Person

class Patient(Person):
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode,Symptoms):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """

        super().__init__(first_name, surname)
        self.__first_name = first_name
        # self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = 'None'
        self.__symptoms = Symptoms

    def full_name(self):
        return f"{self.get_first_name()} {self.get_surname()}"

    def get_doctor(self):
        return self.__doctor
    
    def get_symptoms(self):
        return self.__symptoms
   
    
    def link(self, doctor):
        self.doctor = doctor  


    def link(self, doctor):
        self.__doctor = doctor

    def __str__(self):
        return f"{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}"