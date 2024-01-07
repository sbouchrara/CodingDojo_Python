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
        print("First name :",self.first_name)
        print("Last name :",self.last_name)
        print("Email :",self.email)
        print("Age :",self.age)
        print("Is rewards member :",self.is_rewards_member)
        print("Gold_card_points :",self.gold_card_points)
        print("-"*40)
    # This method changes user's member status to True and set gold card points to 200.
    # Also, check if he is a member already, and if it is True, print "User already a member." and return False, otherwise return True.
    def enroll(self):
        if self.is_rewards_member :
            print (f"{self.first_name} {self.last_name} is already member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True

    # spend_points method
    # This method decrease the user's points by the amount specified in parameter.
    def spend_points(self, amount) :
        if amount < self.gold_card_points :
            self.gold_card_points -= amount
        else:
            print(f"{amount} point(s) is too large to be deducted from {self.gold_card_points}.")

# Adding user instance and calling "disply_info" method through this instance
user_adrean = User("Adrean","Perello","aperello@toto.com",50)
user_adrean.display_info()

# Calling "enroll" method through instance "user-adrean"
user_adrean.enroll()
user_adrean.display_info()

# Make 2 more instances of the User class.
user_gustavo = User("Gustavo","Navaro","gnavaro@toto.com",30)
user_gustavo.display_info()

user_enrique = User("Enrique","Fernando","efernando@toto.com",35)
user_enrique.display_info()

# Adrean spent 50 points
user_adrean.spend_points(50)

# Enroll Gustavo and spent 80 points
user_gustavo.enroll()
user_gustavo.spend_points(80)

# Print user's details
user_adrean.display_info()
user_gustavo.display_info()

# Bonus - enroll Adrean
user_adrean.enroll()

# Bonus - check for over-spending
user_enrique.spend_points(40)