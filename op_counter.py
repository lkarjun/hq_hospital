from typing import NamedTuple, List, Dict
from collections import defaultdict
import datetime


class Labeled_Detail(NamedTuple):

    'details needed for op tickets'
    Op_number: str
    Name: str
    Age: str
    Place: str
    Date: datetime.date
    Specialist: str
    Doctor_name: str


class OpCounter:

    today = datetime.date.today()  # date

    def __init__(self) -> None:
        # to store all patients detail
        self.patients: List = []
        self.op_number: int = 100

    def add_patient(self, **details) -> None:
        # appending patients details
        add_details = Labeled_Detail(self.op_number, details['name'],
                                     details['age'], details['place'],
                                     self.today, details['specialist'],
                                     details['doctor'])
        self.op_number += 1
        self.patients.append(add_details)

    def display_appointments(self) -> List:
        # returns List of patients
        return self.patients

    def print_op_receipt(self) -> None:
        '''Ouputs Op tickets'''
        last_patient: Labeled_Detail = self.patients[-1]
        detail = f'-----------------------------------\
                 \n Date:       {last_patient.Date}\
                 \n Op Number:  {last_patient.Op_number}\
                 \n Name:       {last_patient.Name}\
                 \n Age:        {last_patient.Age},\
                 \n Specialist: {last_patient.Specialist},\
                 \n Doctor:     {last_patient.Doctor_name}\
                   \n-----------------------------------'
        print(detail)

    def total_patients(self) -> List[str]:
        '''return number of patients for doctors'''
        counting: Dict[str, int] = defaultdict(int)
        patients: List[Labeled_Detail] = self.display_appointments()
        for i in patients:
            if i.Doctor_name in counting:
                counting[i.Doctor_name] += 1
            else:
                counting[i.Doctor_name] = 1
        return counting


# Debuging
if __name__ == '__main__':
    a = OpCounter()
    a.add_patient(name='Lal', age='19', place='calicut',
                  specialist='Heart', doctor='V Venugopal')

    a.add_patient(name='Arun', age='9', place='kochi',
                  specialist='Eye', doctor='Dr Rajesh')

    a.add_patient(name='Gopal', age='29', place='palakkad',
                  specialist='Eye', doctor='Dr Rajesh')

    a.add_patient(name='Agitha', age='9', place='kannur',
                  specialist='Eye', doctor='Dr Rajesh')

    a.print_op_receipt()

    print(a.total_patients('Dr Rajesh'))
