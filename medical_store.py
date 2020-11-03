from typing import List, NamedTuple
from doctor import Doctor, DoctorRemark
from op_counter import OpCounter
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

    def create_medicine_report(self) -> None:
        Receipt: DoctorRemark = self.next_op()
        report = MedicalReport(ReceiptNumber = self.Receipt_Number,
                               OpNumber = Receipt.Op_number,
                               Name = Receipt.Op_detail.Name,
                               DoctorName = Receipt.Op_detail.Doctor_name,
                               Remark = Receipt.Remark,
                               Date = Receipt.Op_detail.Date,
                               Specialist = Receipt.Op_detail.Specialist,
                               Patient_email = Receipt.Op_detail.Patient_email)
        
        self.Report.append(report)



# debugging
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
        # print('--------------------------------------')
        # print('current patient =', dr.current_patient)
        # print('appointed patients op =', dr.appointed_patients)
        # print('Remarks\n')
        dr.remark[i]
        # print('--------------------------------------')
    print("_____________");print()
    medicine__ = Medical(dr)
    medicine__.next_op()
    medicine__.create_medicine_report()
    print(medicine__.Report)
