from typing import Dict, List, NamedTuple, Tuple
from op_counter import Labeled_Detail, OpCounter
from pprint import pprint


class Doctor(OpCounter):

    receiption_obj = None  # Need Reception Object

    def __init__(self) -> None:
        self.doctor = 'Admin'  # Further process dr name is needed

    def appointments(self) -> List[Labeled_Detail]:
        '''it returns total appointments '''
        total_appointments: List = [
            i for i in OpCounter.display_appointments(self.receiption_obj)
            if i.Doctor_name == self.doctor]
        return total_appointments

    def total_patients(self) -> Tuple[int, Dict]:
        ''' returns total patients and there details.
        patients details for respective doctors'''
        appointments: List = self.appointments()
        return len(appointments), {patient.Op_number:
                                   patient.Name
                                   for patient in appointments
                                   }

    def next_patient(self) -> Tuple[str, int]:
        '''It return Next patient Name and Op number'''
        # Sort by op_number
        appointments: List = self.appointments()
        patients: List = sorted(appointments, key=lambda l: l.Op_number)
        if len(patients) == 0:
            return 'Doctor You please take rest. There is no patients for you.'
        return patients[0].Name, patients[0].Op_number

    def medical(self) -> List[Labeled_Detail]:
        pass

    def set_doctor_name(self, name: str) -> None:
        # sets doctor name
        self.doctor: str = name

    @classmethod
    def set_obj(cls, obj: OpCounter) -> None:
        # set reception obj
        cls.receiption_obj: OpCounter = obj
