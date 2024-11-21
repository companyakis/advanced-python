employee_titles = {"Bengü": "Expert", "Hakan": "Coordinator", "Aygün": "Senior Expert", "Mustafa": "Head", "Kutluk": "Assistant Expert"}

employee_experience_years = {"Hakan": 15, "Mustafa": 18, "Aygün": 8, "Bengü": 13, "Kutluk": 9}

experinced_less_10 = {
    (emp, exp) for (emp, exp) in employee_titles.items() if employee_experience_years[emp] < 10 if "Expert" in exp
}

print(experinced_less_10) # {('Kutluk', 'Assistant Expert'), ('Aygün', 'Senior Expert')}
