# Declare a class
class User:
    # Attributes
    def __init__(self,p_first_name,p_last_name,p_email,p_age) -> None:
        self.first_name         = p_first_name
        self.last_name          = p_last_name
        self.email              = p_email
        self.age                = p_age
        # set to False by default
        self.is_rewards_member  = False
        # set to zero by default
        self.gold_card_points   = 0
    
    # Methods
    # This method prints all users' details
    def display_info(self):
        print("-"*40)
        print("First name :",self.first_name)
        print("Last name :",self.last_name)
        print("Email :",self.email)
        print("Age :",self.age)
        print("Is rewards member :",self.is_rewards_member)
        print("Gold_card_points :",self.gold_card_points)
        print("-"*40)
        return self
    
    # This method changes user's member status to True and set gold card points to 200.
    # Also, check if he is a member already, and if it is True, print "User already a member." and return False, otherwise return True.
    def enroll(self):
        if self.is_rewards_member :
            print("-"*40)
            print (f"{self.first_name} {self.last_name} is already member.")
            print("-"*40)
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    # spend_points method
    # This method decrease the user's points by the amount specified in parameter.
    def spend_points(self, amount) :
        if amount < self.gold_card_points :
            self.gold_card_points -= amount
        else:
            print("-"*40)
            print(f"{amount} point(s) cannot be deducted. {self.first_name}'s balance is less than the requested amount.")
            print("-"*40)
        return self

# Adding user instance 
# Calling methods "disply_info", "spend_points" and "enroll" through this instance
# using Short-cut
user_adrean = User("Adrean","Perello","aperello@toto.com",50)
user_adrean.display_info().enroll().display_info().spend_points(50).display_info().enroll()

# 1 more instance of the User class.
# Calling methods using Short-cut
user_gustavo = User("Gustavo","Navaro","gnavaro@toto.com",30)
user_gustavo.display_info().enroll().spend_points(80).display_info()

# 1 more instance of the User class.
user_enrique = User("Enrique","Fernando","efernando@toto.com",35)
user_enrique.display_info().spend_points(40)
