from typing import Dict, Tuple
from op_counter import OpCounter
from doctor import Doctor

reception = OpCounter()
dr = Doctor()
dr.set_obj(reception)


def add(name: str, age: int, place: str, specialist: str,
        doctor: str) -> None:

    reception.add_patient(name=name, age=age, place=place,
                          specialist=specialist, doctor=doctor)


def patient_view(name: str) -> Tuple[int, Dict]:
    '''return Total patients'''
    dr.set_doctor_name(name)
    return dr.total_patients()


def nex_patient(name: str) -> Tuple[str, int]:
    '''return Next patient detial'''
    dr.set_doctor_name(name)
    return dr.next_patient()


if __name__ == '__main__':
    add(name='Lal', age='19', place='calicut',
        specialist='Heart', doctor='V Venugopal')

    add(name='Arun', age='9', place='kochi',
        specialist='Eye', doctor='Dr Venugopal')

    add(name='Gopal', age='29', place='palakkad',
        specialist='Eye', doctor='Dr Rajesh')

    add(name='Agitha', age='9', place='kannur',
        specialist='Eye', doctor='Dr Rajesh')

    add(name='Aruthathi', age='4', place='Ernakkulam',
        specialist='Eye', doctor='Dr Rajesh')

    print(patient_view('Dr Venugopal'))
    print(nex_patient('Dr Venugopal'))
    print()
    print(patient_view('Dr Rajesh'))
    print(nex_patient('Dr Rajesh'))
