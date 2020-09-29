start_km = int(input('Enter start result'))
finish_km = int(input('Enter finish result'))
start_day = 1
result = start_km
while start_km < finish_km:
    start_km = start_km * 1.1
    start_day += 1
    result = result + start_km
    print(f"Вы достигнете требуемых показателей на %.d день" % start_day)
