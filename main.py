from os import scandir
from typing import Dict, Tuple
from op_counter import OpCounter
from doctor import Doctor

reception = OpCounter()
dr = Doctor()
dr.set_obj(reception)


def add(name: str, age: int, place: str, specialist: str,
        doctor: str, email: str) -> None:

    reception.add_patient(name=name, age=age, place=place,
                          specialist=specialist, doctor=doctor, email=email)


def patient_view(name: str) -> Tuple[int, Dict]:
    '''return Total patients'''
    dr.set_doctor_name(name)
    return dr.total_patients()


def nex_patient(name: str) -> Tuple[str, int]:
    '''return Next patient detial'''
    dr.set_doctor_name(name)
    return dr.next_patient()

def add_next_patient(name: str):
    dr.set_doctor_name(name)
    dr.add_current_patient()

if __name__ == '__main__':
    add(name='Lal', age='19', place='calicut',
        specialist='Heart', doctor='V Venugopal',
        email='lalu@gmail.com')

    add(name='Arun', age='9', place='kochi',
        specialist='Eye', doctor='Dr Venugopal',
        email='arun@gmail.com')

    add(name='Gopal', age='29', place='palakkad',
        specialist='Eye', doctor='Dr Rajesh',
        email='gopal@gmail.com')

    add(name='Agitha', age='9', place='kannur',
        specialist='Eye', doctor='Dr Rajesh',
        email='agitha@gmail.com')

    add(name='Aruthathi', age='4', place='Ernakkulam',
        specialist='Eye', doctor='Dr Rajesh',
        email='aruthathi@gmail.com')

    print(patient_view('Dr Venugopal'))
    print(nex_patient('Dr Venugopal'))
    print()
    print(patient_view('Dr Rajesh'))
    print(nex_patient('Dr Rajesh'))
