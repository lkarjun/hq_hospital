from typing import NamedTuple
from doctor import Doctor
import datetime


class MedicalReport(NamedTuple):

    '''basic details needed for medical report'''
    OpNumber: int
    Name: str
    DoctorName: str
    Remark: str
    Date: datetime.date
