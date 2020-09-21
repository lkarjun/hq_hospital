from typing import NamedTuple, List
import datetime

class Labeled_Detail(NamedTuple):

    'details needed for op tickets'

    Name: str
    Age: str
    Place: str
    Date: datetime.date
    Specialist: str
    Doctor_name: str


class OpCounter:

    today = datetime.date.today() #date

    def __init__(self) -> None:
        #to store all patients detail
        self.patients: List = []
    
    def add_patient(self, **details) -> None:
        #appending patients details
        add_details = Labeled_Detail(details['name'], details['age'],\
                                     details['place'], self.today,\
                                     details['specialist'], details['doctor'])
        self.patients.append(add_details)

    def display_appointments(self) -> List:
        #returns List of patients
        return self.patients


# Debuging
if __name__ == '__main__':
    a = OpCounter()
    a.add_patient(name='Lal', age='19', place='calicut', specialist='Heart', doctor='V Venugopal')
    a.add_patient(name='Arun', age='9', place='kochi', specialist='Eye', doctor='Dr Rajesh')
    detail = a.display_appointments()
    for i in detail:
        print(f'Name is {i.Name}\nage is {i.Age},\nPlace is {i.Place},\nspecialis is {i.Specialist},\ndoctor is {i.Doctor_name}')
        print('-'*20)
