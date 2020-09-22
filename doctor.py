from typing import Dict, List, Tuple
from op_counter import Labeled_Detail, OpCounter
from pprint import pprint


class Doctor(OpCounter):

    def __init__(self, doctor: str, obj: object) -> None:
        self.doctor = doctor  # Further process dr name is needed
        self.appointments = OpCounter.display_appointments(obj)

