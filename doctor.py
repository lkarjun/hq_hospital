from typing import Dict, List, Tuple
from op_counter import Labeled_Detail, OpCounter
from pprint import pprint


class Doctor(OpCounter):

    def __init__(self, doctor: str, obj: object) -> None:
        self.doctor = doctor  # Further process dr name is needed
        self.appointments = OpCounter.display_appointments(obj)

    def total_patients(self) -> Tuple[int, Dict]:
        # Include patients details for respective doctors
        patients = [i for i in self.appointments
                    if i.Doctor_name == self.doctor]

        return len(patients), {patient.Op_number: patient.Name
                               for patient in patients
                               if patient.Doctor_name == self.doctor}
