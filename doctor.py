from typing import Dict, List, Tuple
from op_counter import Labeled_Detail, OpCounter
from pprint import pprint


class Doctor(OpCounter):

    def __init__(self, doctor: str, obj: object) -> None:
        self.doctor = doctor  # Further process dr name is needed
        self.appointments = [i for i in OpCounter.display_appointments(obj)
                             if i.Doctor_name == self.doctor]

    def total_patients(self) -> Tuple[int, Dict]:
        # Include patients details for respective doctors
        return len(self.appointments), {patient.Op_number:
                                        patient.Name
                                        for patient in self.appointments
                                        if patient.Doctor_name == self.doctor}

    def next_patient(self) -> Tuple[str, int]:
        '''It return Next patient Name and Op number'''
        # Sort by op_number
        patients = sorted(self.appointments, key=lambda l: l.Op_number)
        return patients[0].Name, patients[0].Op_number
