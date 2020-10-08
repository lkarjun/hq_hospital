from typing import List, NamedTuple
from doctor import Doctor, DoctorRemark
import datetime


class MedicalReport(NamedTuple):

    '''basic details needed for medical report'''
    ReceiptNumber: int
    OpNumber: int
    Name: str
    DoctorName: str
    Remark: str
    Date: datetime.date
    Specialist: str
    Patient_email: str


class Medical(Doctor):

    def __init__(self, doctor: Doctor) -> None:
        self.Report: List[MedicalReport] = []
        self.medicine_received_ops: List = []
        self.Receipt_Number: int = 1000
        self.obj: Doctor = doctor

    def doctor_receipt_collect(self) -> List[DoctorRemark]:
        '''It returns full List of remarks of doctor'''
        return [i
                for i in self.obj.remark
                if i.Op_number not in self.medicine_received_ops]
        
    def medicine_received(self) -> None:
        # appends op number to medicine_received_ops
        op_numb  = self.next_op()
        self.medicine_received_ops.append(op_numb.Op_number)

    def next_op(self) -> DoctorRemark:
        '''its return next Patients remarks to receive medicine'''
        remarks = self.doctor_receipt_collect()
        return remarks[0]

    def medicine_receipt_create(self) -> None:
        pass