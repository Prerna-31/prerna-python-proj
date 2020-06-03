class hostel:                          ##outer class
    #def __init__(self,n_floors,n_rooms,n_sharing,rent): #*
    def __init__(self, n_floors, n_rooms):
        self.n_floors = n_floors
        self.n_rooms = n_rooms
        #self.o_room = self.room(n_sharing,rent)  #*

    def get_details(self):
        print('The hostel has {} floors and {} rooms'.format(self.n_floors,(self.n_floors*self.n_rooms)))
       # self.o_room.get_earnings()  #*

    class room:                   ##inner class
        def __init__(self,n_sharing,rent,n_flr,n_rm):
            self.n_sharing = n_sharing
            self.rent = rent
            self.n_flr = n_flr
            self.n_rm = n_rm

        def get_earnings(self):
            #h2 = hostel(4,10)     ## can instantiate class inside itself
            #print 'Inside earning:', h2.n_rooms, h2.n_floors
            print('Total earnings from the hostel : ', (self.n_flr*self.n_rm*self.n_sharing*self.rent)) ## might not need that many paarameters as we can use outer class attributes.

print('Enter building details::')
n_floors = int(input('Enter number of floors: '))
n_rooms  = int(input('Enter number of rooms on each floor: '))

h1 = hostel(n_floors,n_rooms)
h1.get_details()

n_seater = int(input('Enter number of sharing: '))
h_rent  = int(input('Enter room rent in rupees: '))

#h1 = hostel(n_floors,n_rooms,n_seater,h_rent)   #*   Creating object of inner class inside the init method of outer class.
#h1.get_details()       #*

r1 = hostel.room(n_seater,h_rent,h1.n_floors,h1.n_rooms)   ##instantiation of inner class object
r1.get_earnings()

## another room can have different rent. so instantitate different object
#r2 = hostel.room(2,9000,h1.n_floors,h1.n_rooms)
#r2.get_earnings()
