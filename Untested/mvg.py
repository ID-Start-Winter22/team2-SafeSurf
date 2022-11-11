#pip install mvg-api
from mvg_api import *

# Stationen = input("Bitte Station eingeben: ") #Input Proof of concept
# EndStation = input("Bitte end Station angeben: ") #Input Proof of concept

# Stationen = Station(Stationen) #Input Proof of concept
# EndStation = Station(EndStation) #Input Proof of concept
# departures = Stationen.get_departures() #Input Proof of concept

# for departure in departures:
#     print(departure['product'] + departure['label'] + "\t" + departure['destination'] + "\t" + str(departure['departureTimeMinutes'])) #Proof of concept

# print(get_route(1, 2)) #Für den Kompletten output

route = get_route(2, 1)

for connection in route:
  print(connection['arrival_daytime'] + "\t" + connection['departure_daytime'])
