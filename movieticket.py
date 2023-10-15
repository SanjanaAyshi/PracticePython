
class Star_Cinema:
     __hall_list=[]
     
     @classmethod
     def entry_hall(self,Hall):
        Star_Cinema.__hall_list.append(Hall)

   
class Hall(Star_Cinema):
     def __init__(self, rows, cols, hall_no):
         self.seats = {}
         self.show_list = []
         self.rows = rows
         self.cols = cols
         self.hall_no = hall_no
         Star_Cinema.entry_hall(self)
    
     def entry_show(self, id, movie, time):
        info = (id, movie, time)
        self.show_list.append(info)
        self.seats[id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)] 
         
     def book_seats(self, id, seat_list):
        if id in self.seats:
            for row, col in seat_list:
                if 0 <= row-1 < self.rows and 0 <= col-1 < self.cols:
                    if self.seats[id][row-1][col-1] == 0:
                        self.seats[id][row-1][col-1] = 1
                    else:
                        print(f"Seat at row {row} and column {col} is already booked.")
                else:
                    print(f"Invalid seat position at row {row} and column {col}.")
        else:
            print(f"No show found with id {id}.")
            
     def view_show_list(self):
        for i in self.show_list:
            print(f"ID: {i[0]}\tMovie Name: {i[1]}\tTime: {i[2]}")  
     
     def view_available_seats(self, id):
         if id in self.seats:
            print(f"Available seats for show {id}:")
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.seats[id][i][j] == 0:
                        print(f"({i+1},{j+1})")
         else:
            print(f"No show found with id {id}.")
        
         
hall1=Hall(7,7,1)
hall2=Hall(7,7,2)
hall1.entry_show(111, "Spider-Man: No Way Home", "12:00 PM")
hall2.entry_show(101, "Black Adam", "1:00 PM")

while True:
    print(f"1.View all show time\n2.View available seats\n3.Book ticket\n4.Exit")
    option=int(input())
    if(option==1):
        hall1.view_show_list()
        hall2.view_show_list()
    
    elif(option==2):
        ID=int(input("Enter id: "))
        if (ID==111):
         hall1.view_available_seats(ID)
        elif(ID==101):
         hall2.view_available_seats(ID)
    elif(option==3):
        ID=int(input("Enter id: "))
        ticket=int(input("Enter number of tickets: "))
        seat_list = []
        for i in range(ticket):
            row = int(input(f"Enter row for ticket {i+1}: "))
            col = int(input(f"Enter column for ticket {i+1}: "))
            seat_list.append((row, col))
        if (ID==111):
            hall1.book_seats(ID, seat_list)
        elif(ID==101):
            hall2.book_seats(ID, seat_list)
            
    elif(option==4):
        break