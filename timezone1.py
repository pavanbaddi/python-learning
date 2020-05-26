from datetime import timedelta

year = timedelta(days=365)
ten_years = 10 * year

print(ten_years)

print(ten_years.days)

nine_years = ten_years-year
print(nine_years)

three_years = nine_years
print(three_years, three_years.days)