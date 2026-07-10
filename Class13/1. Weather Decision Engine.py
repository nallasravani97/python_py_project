Weather = int(input('enter the weather condition(Temperature):'))

if Weather < 0:
    print("Freeing: Wear a heavy coat.")
elif Weather < 15:
    print("Chilly: You might need a jacket.")
elif Weather < 25:
    print("Mild: A light sweater is enough.")
else:
    print("Hot: Stay cool and hydrated.")