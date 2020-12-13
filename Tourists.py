""" Tourist recommendation project that runs an engine to evaluate a person's interests and give them a
    recommendation in the area they are visiting to venues, restaurants, and historical destinations. """

destinations = [
               "Paris, France",
               "Shanghai, China",
               "Los Angeles, USA",
               "São Paulo, Brazil",
               "Cairo, Egypt"
              ]

'''GRABS INDEX OF DESTINATION FROM DESTINATIONS LIST'''
def getDestIndex(dest):
  destinationIndex = destinations.index(dest)

  return destinationIndex


'''PULLS THE DESTINATION FROM THE TRAVELER INFO AND GIVES INDEX FOR THE DESTINATION LIST'''
def getTravelerLoc(traveler):
  travelerDest = traveler[1]
  travelerDestinationIndex = getDestIndex(travelerDest)

  return travelerDestinationIndex


#testDestIndex = getTravelerLoc(testTraveler)

attractions = [[] for x in range(len(destinations))]

'''ADDS ATTRACTIONS TO THE ATTRACTIONS LIST'''
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

'''BASED ON TRAVELERS DESTINATION AND INTERESTS, RETURNS ATTRACTIONS THAT CORRESPOND WITH TRAVELERS INTERESTS'''
def findAttractions(dest, interests):
    destIndex = getDestIndex(dest)
    attractionsInCity = attractions[destIndex]
    attractWithInterest = []

    for i in attractionsInCity:
        possibleAttraction = i
        attractionTags = i[1]

        for x in interests:
            if x in attractionTags:
                attractWithInterest.append(possibleAttraction[0])  # Append

    return attractWithInterest

# la = findAttractions("Los Angeles, USA",["museum","beach"]) # Test findAttractions



'''SEPARATES OUT THE TRAVELERS INFORMATION'''
def attractionsForTraveler(traveler):
    travelerDest = traveler[1]
    travelerInterests = traveler[2]
    travelerAttracts = findAttractions(travelerDest, travelerInterests)
    interestString = "Hi " + traveler[0] + ", we think you'll like these places around " + travelerDest + ": "
    secondString = "\n"
    count = len(travelerAttracts)

    '''ADDS LOGIC FOR CONSTRUCTING STRING TO DISPLAY RECOMMENDATIONS'''
    for i in travelerAttracts:
        if count > 1:
            secondString += i + ", "
            count -= 1
        else:
            secondString += i + ".\n"

    return interestString + secondString

# Test attractionsForTraveler below
smillsFrance = attractionsForTraveler(['Dereck Smills', 'Paris, France', ['art', 'monument']])
testTraveler = attractionsForTraveler(['Erin Wilkes', 'Shanghai, China',['historical site',  'art']])
print(testTraveler, smillsFrance)








