""" Tourist recommendation project that runs an engine to evaluate a person's interests and give them a
    recommendation in the area they are visiting to venues, restaurants, and historical destinations. """

destinations = [
               "Paris, France",
               "Shanghai, China",
               "Los Angeles, USA",
               "São Paulo, Brazil",
               "Cairo, Egypt"
              ]

testTraveler = ['Erin Wilkes', 'Shanghai, China',['historical site',  'art']]  # Test input for a traveler

# Gets the index of the destination from the destinations list
def getDestIndex(dest):
  destinationIndex = destinations.index(dest)
  return destinationIndex


# Pulls the destination from the traveler info and gives us index
# for the destinations list
def getTravelerLoc(traveler):
  travelerDest = traveler[1]
  travelerDestinationIndex = getDestIndex(travelerDest)
  return travelerDestinationIndex


testDestIndex = getTravelerLoc(testTraveler)
attractions = [[] for x in range(len(destinations))]


def addAttraction(dest, att):
  try:
    destIndex = getDestIndex(dest)  # Gets dest index from destinations
    attractionsForDest = attractions[destIndex]  # Gets list from attractions that corresponds with destination index
    attractionsForDest.append(att)  # Appends attraction to the attractions list
    return attractionsForDest
  except ValueError:
    print('There was an error')
    return


addAttraction('Los Angeles, USA', ['Venice Beach',['beach']])
addAttraction('Paris, France', ['the Louvre',['art','museum']])
addAttraction('Paris, France', ['Arc de Triumphe',['historical site', 'monument']])
addAttraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
addAttraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
addAttraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
addAttraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
addAttraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
addAttraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
addAttraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
addAttraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

for i in attractions:
  print(i)