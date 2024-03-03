class Guest:
    def search_books(self, info):
        pass

class Library:
    def search_books(self, info):
        pass
    
    def add_book(self, book):
        pass
    
    def remove_book(self, book):
        pass



class BasicUser(Guest):
    def search_books(self, info):
        print(f"searching for: {info}")

class AdminUser(Library):
    def search_books(self, info):
        print(f"Admin user searching for books with: {info}")
    
    def add_book(self, book):
        print(f"Admin user adding book: {book}")
    
    def remove_book(self, book):
        print(f"Admin user removing book: {book}")

# Example usage

def main():
    basic_user = BasicUser()
    basic_user.search_books("Python Coding")

    admin_user = AdminUser()
    admin_user.search_books("Binary")
    admin_user.add_book("Deep Learning")
    admin_user.remove_book("Algorithms")

if __name__ == "__main__":
    main()