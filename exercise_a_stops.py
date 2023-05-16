
stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]
stops.append("Edinburgh Waverley")
print(stops)

stops.insert(0,"Glasgow Queen st"),
stops.insert(4, "polmont")
print(stops)

index = stops.index('Linlithgow')
print(index)

stops.remove('Livingston')
print(stops)

stops.pop(2)
print(stops)

num_items = len(stops)
print(num_items)

stops.sort()
print(stops)

stops.reverse()
print(stops)

stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

for stop in stops:
    print(f'{stop} is one of the stops on the train')
#1. Add "Edinburgh Waverley" to the end of the list
#2. Add "Glasgow Queen St" to the start of the list
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
#4. Print out the index position of "Linlithgow"
#5. Remove "Livingston" from the list using its name
#6. Delete "Cumbernauld" from the list by index
#7. Print the number of stops there are in the list
#8. Sort the list alphabetically
#9. Reverse the positions of the stops in the list
#10 Print out all the stops using a for loop