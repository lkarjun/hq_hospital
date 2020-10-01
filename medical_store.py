from typing import List, NamedTuple
from doctor import Doctor
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
    def __init__(self) -> None:
        self.Report: List[MedicalReport] = []
        self.Receipt_Number: int = 1000
