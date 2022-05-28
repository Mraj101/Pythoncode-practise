class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats 
    def getStatus(self):
        print(f"The name of train is {self.name}")
        print(f"The seats avalilable in the train  {self.seats}")
    def fareInfo(self):
        print(f"The price of the ticket is: {self.fare}BDT")

    def bookTicket(self):
        if(self.seats)>0:
            print(f"your Ticket has been booked \nyour seat number is {self.seats}")
            self.seats=self.seats-1
        else:
            print("no seats avalible")
    def cancelTicket(self):
        print(f"Your number {self.seats+1} tickets has been canceled")
        self.seats=self.seats+1

      
    def seatDetails(self):
        pass
        # total_seat=self.seats
        # print(f"these seats are available:{list(range(1,self.seats+1))}")


intercity=Train("intercity Express: 1450",90, 10)
intercity.getStatus()
print("*******")
intercity.bookTicket()
intercity.getStatus()
intercity.cancelTicket()
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
intercity.cancelTicket()
intercity.getStatus()