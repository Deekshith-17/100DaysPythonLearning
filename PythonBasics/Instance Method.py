from datetime import timedelta
year = timedelta(days=365)
years = 5 * year
print (years)
print (years.days // 365)
646
year_1 = years // 5
print(year_1.days)