from os import curdir
from typing import Dict, List, NamedTuple, Tuple
from op_counter import Labeled_Detail, OpCounter


class DoctorRemark(NamedTuple):
    Op_number: int
    Op_detail: Labeled_Detail
    Remark: str


class Doctor(OpCounter):

    receiption_obj = None  # Need Reception Object

    def __init__(self) -> None:
        self.doctor = 'Admin'  # Further process dr name is needed
        self.appointed_patients: List = []  # to keep track appointed patients
        self.current_patient: int = None  # Current patient detail.
        self.remark: List[DoctorRemark] = []  # Doctor remarks.

    def appointments(self) -> List[Labeled_Detail]:
        '''it returns total appointments '''
        total_appointments: List = [
            i for i in OpCounter.display_appointments(self.receiption_obj)
            if i.Doctor_name == self.doctor
            if i.Op_number not in self.appointed_patients]
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

    def add_current_patient(self) -> None:
        '''add op_number to current patient at the same time append to appointed patients detail'''
        try:
            self.current_patient = self.next_patient()
            self.appointed_patients.append(self.current_patient[1])
        except:
            return 'There is no patient'

    def medical(self, remark: str) -> None:
        '''append to remark List with Object "DoctorRemark"'''
        _, opNumber = self.current_patient
        self.remark.append(DoctorRemark(opNumber, self.get_patient_opobjec(), remark))

    def set_doctor_name(self, name: str) -> None:
        # sets doctor name
        self.doctor: str = name

    def get_patient_opobjec(self) -> Labeled_Detail:
        _,OpNumber = self.current_patient
        for i in OpCounter.display_appointments(self.receiption_obj):
            if i.Op_number == OpNumber:
                return i 

    @classmethod
    def set_obj(cls, obj: OpCounter) -> None:
        # set reception obj
        cls.receiption_obj: OpCounter = obj




if __name__ == '__main__':
    op = OpCounter()
    dr = Doctor()
    dr.set_obj(op)
    dr.set_doctor_name('Dr Rajesh')
    op.add_patient(name='Lal', age='19', place='calicut',
        specialist='Heart', doctor='Dr Rajesh',
        email='lalu@gmail.com')

    op.add_patient(name='Arun', age='9', place='kochi',
        specialist='Eye', doctor='Dr Rajesh',
        email='arun@gmail.com')

    op.add_patient(name='Gopal', age='29', place='palakkad',
        specialist='Eye', doctor='Dr Rajesh',
        email='gopal@gmail.com')

    op.add_patient(name='Agitha', age='9', place='kannur',
        specialist='Eye', doctor='Dr Rajesh',
        email='agitha@gmail.com')

    op.add_patient(name='Aruthathi', age='4', place='Ernakkulam',
        specialist='Eye', doctor='Dr Rajesh',
        email='aruthathi@gmail.com')

    values = ['Not so serious. Medicine Parasitamole', 'Normal bp', 'Imediate blood test',\
              'Do excerise', 'Do eye focusing excerise']

    for i in range(len(dr.appointments())):
        dr.add_current_patient()
        dr.medical(values[i])
        print('--------------------------------------')
        print('current patient =', dr.current_patient)
        print('appointed patients op =', dr.appointed_patients)
        print('Remarks\n')
        print(dr.remark[i])
        print('--------------------------------------')