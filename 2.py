Name = str(input('Enter your name'))
Surname = str(input('Enter your surname'))
year = int(input('Enter year'))
City = str(input('Enter city'))
email = str(input("Enter your email"))
tel = str(input("Enter your phone num"))

def my_func(Name, Surname, year, City, email, tel):
    return Name, Surname, year, City, email, tel

print(my_func((f'Name: {Name}'), (f'Surname = {Surname}'), (f'Year = {year}'), (f'City = {City}'), (f'Email = {email}'), (f'Tel= {tel}') ))