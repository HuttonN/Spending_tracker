from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

from models.tag import Tag
import repositories.tag_repository as tag_repository

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository

from datetime import datetime


transaction_repository.delete_all()
merchant_repository.delete_all()
tag_repository.delete_all()


# Create merchants
Amazon = Merchant("Amazon")
merchant_repository.save(Amazon)
Apple = Merchant("Apple")
merchant_repository.save(Apple)
Deliveroo = Merchant("Deliveroo")
merchant_repository.save(Deliveroo)
Natwest_Bank = Merchant("Natwest Bank")
merchant_repository.save(Natwest_Bank)
Puregym = Merchant("Puregym")
merchant_repository.save(Puregym)
Starbucks = Merchant("Starbucks")
merchant_repository.save(Starbucks)
Tesco = Merchant("Tesco")
merchant_repository.save(Tesco)
Virgin = Merchant("Virgin")
merchant_repository.save(Virgin)
WHSmith = Merchant("WHSmith")
merchant_repository.save(WHSmith)

#Create tags
Housing = Tag("Housing")
tag_repository.save(Housing)
Groceries = Tag("Groceries")
tag_repository.save(Groceries)
Entertainment = Tag("Entertainment")
tag_repository.save(Entertainment)
Transportation = Tag("Transportation")
tag_repository.save(Transportation)
Health = Tag("Health")
tag_repository.save(Health)
Pets = Tag("Pets")
tag_repository.save(Pets)
Gifts = Tag("Gifts")
tag_repository.save(Gifts)
Utilities = Tag("Utilities")
tag_repository.save(Utilities)
Take_aways = Tag("Take Aways")
tag_repository.save(Take_aways)

#Create transaction
mortage_Mar_23 = Transaction(663.35,Natwest_Bank,Housing,datetime(2023,3,3))
transaction_repository.save(mortage_Mar_23)
gym_Mar_23 = Transaction(14.99,Puregym,Health,datetime(2023,3,31))
transaction_repository.save(gym_Mar_23)
take_out = Transaction(14.80,Deliveroo,Take_aways,datetime(2023,3,15))
transaction_repository.save(take_out)
internet = Transaction(48.49,Virgin,Utilities,datetime(2023,3,3))
transaction_repository.save(internet)
grocery_shop = Transaction(50.94,Tesco,Groceries,datetime(2023,3,6))
transaction_repository.save(grocery_shop)