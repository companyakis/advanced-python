class Instructor:
    
    def __init__(self, name, lecture) -> None:
        self.name = name
        self.lecture = lecture
        
    def __repr__(self) -> str:
        return f"Instructor: {self.name} and lecture: {self.lecture}"


if __name__ == "__main__":
    
    instructor_aybuke = Instructor("Aybüke Bilir", "Econ 101")
    
    instructor_ayhan = Instructor("Ayhan Atarlı", "FinTech 101")

    print(instructor_aybuke)
    
    print(instructor_ayhan)
    
# Instructor: Aybüke Bilir and lecture: Econ 101
# Instructor: Ayhan Atarlı and lecture: FinTech 101
