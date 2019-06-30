


hotel = {
 '1': {
   '101': ['George Jefferson', 'Wheezy Jefferson'],
   '105':['Jon', 'Jonathan', 'Johnny'],
 },
 '2': {
   '237': ['Jack Torrance', 'Wendy Torrance'],
 },
 '3': {
   '333': ['Neo', 'Trinity', 'Morpheus']
 },
 '4': {
   '444': ['Mitchell', 'Morgan', 'Xander']
 },
 '5': {
   '533': ['Anne', 'James', 'Elliot', 'Jonathan']
 }
}


def greeting():
    front_desk = input("Welcome to the Python Hotel.\nWould you like to:\n1. check-in \n2. check out\n3. list of guests\n4. exit?\n")

    while front_desk == "check in" or front_desk == "1":
        floor = input("What is your floor number [1-5]? ")
        room = input("What is your room number? ")
        
        if hotel.get(floor) != None and hotel.get(floor).get(room) != None:
            print("That room is taken, please choose another room.")
            
        else:
            print("Great, welcome to the hotel.")
            occupants = int(input("How many occupants do you have? "))
            count = 0
            occupant_list = []
            while count < occupants:
                names = input(str(count+1) + " Occupant's Name: ")
                occupant_list.append(names)
                count+=1
            hotel[floor][room] = occupant_list
            print(hotel[floor][room])
            front_desk = None
            greeting()
            
    while front_desk == "check out" or front_desk == "2":
        floor = input("What is your floor number? ")
        room = input("What is your room number? ")
        if hotel.get(floor).get(room) != None:
            hotel[floor][room] = None
            print("\nThank you for staying with us.\n")
            print("Floor ", floor,"\tRoom ", room,":\t", hotel[floor][room], "\n")
            #print("\t\t\t", hotel[floor][room])
            front_desk = None
            greeting()
        else:
            print("That room is not occupied, please enter your room number.")

    if front_desk == "list" or front_desk == "3":
        list_criteria = input("Please enter a floor number or 'all' for all current guests: ")
        if list_criteria == 'all':
            print("Here's a list of our current guests:")
            for key, value in hotel.items():
                indent = 0
                print("Floor " + key + ":")
                for values, names in value.items():
                    print("\t\t", "Room: ", values)
                    for name in names:
                        print("\t\t\t", name)
                    #print("\t\t\t" + names)
            front_desk = None
            greeting()
        else:
            print("Here's a list of our current guests on Floor " + list_criteria + ":")
            for key, value in hotel[list_criteria].items():
                print("\t", "Room ", key)
                for names in value:
                    print("\t\t\t", names)
            front_desk = None
            greeting()
    else:
        return
    

    
greeting()