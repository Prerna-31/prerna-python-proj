class book_store:

    b_genre = 'Love Story'

    def __init__(self,b_name,b_author):   ## in-built constructor
        self.b_name = b_name
        self.b_author = b_author

    def book_details(self):              ## accessor instance method
        print('Name: ',self.b_name , ' Author: ', self.b_author)

    def update_details(self, new_nm):           ## mutator instance method
        self.b_name=new_nm
        print('\nBook\'s updated name : ',self.b_name)

    @classmethod
    def display_book_genre(cls):       ## Class method
        print('The genre of book is', cls.b_genre)

    @staticmethod
    def display_cls_info():            ## Static method
        print('This class is book store.......')

book_store.display_cls_info()

book_store.display_book_genre()

print('')

print('Enter book details: ')
name = input('Name: ')
author = input('Author: ')

bk1 = book_store(name,author)

print('\nBefore updating-->Book description: ')
bk1.book_details()

new_nm = input('\nEnter book name to replace original:')
bk1.update_details(new_nm)

print('\nAfter upating-->Book description: ')
bk1.book_details()
