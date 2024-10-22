from enum import Enum

class Employee(Enum):
    HEAD = ""
    Expert = ""
    Assistant = ""

def management_control(auth: Employee):
    match auth:
        case auth.HEAD:
            print("The Manager has the required permission!")
        case auth.Expert:
            print("An expert has limited control power")
        case auth.Assistant:
            print("An assistant... He/She should wait...")
        case _:
            print("Unknown person and control request!")
        

management_control(Employee.HEAD) # The Manager has the required permission!
