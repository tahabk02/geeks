from datetime import datetime

birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")
birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
today = datetime.today()

age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
candles = age % 10
if candles == 0:
    candles = 10  

candle_line = " " * 7 + "_" * candles
year = birthdate.year
is_leap = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

cake = f"""
       {candle_line}
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""

if is_leap:
    print(cake * 2)
else:
    print(cake)

print(f"\nYou are {age} years old today! ")
