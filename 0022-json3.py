import json

salary_data_usd = '{"ayhan": 4000, "hakan": 1500, "bilge": 3200}'

new_salary_data_usd = json.loads(salary_data_usd, parse_int = int) # if float, use float

for key, value in new_salary_data_usd.items():
    print(f"Employee: {key.title()} and salary $: {value}")


# Employee: Ayhan and salary $: 4000
# Employee: Hakan and salary $: 1500
# Employee: Bilge and salary $: 3200
