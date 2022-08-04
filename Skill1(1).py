import random
class ticketPrinting:
    def printTicket(self,str,gender,pick,destination):
        print("\n\n     *******PASSENGER TICKET*******")
        print("Name:", str)
        print("Gender:", gender)
        print("from", pick, "to", destination)
        print("PNR NUMBER:",random.randint(999999999,100000000000))

class manager(ticketPrinting):
    name=input("Enter passenger name:")
    gender=input("Enter passenger gender:")
    pick=input("Enter Starting point: ")
    destination=input("Enter Destination: ")
    obj=ticketPrinting()
    obj.printTicket(name,gender,pick,destination)


