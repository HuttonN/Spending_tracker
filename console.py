from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

from models.tag import Tag
import repositories.tag_repository as tag_repository

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository


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
Starbucks = Merchant("Starbucks")
merchant_repository.save(Starbucks)
Tesco = Merchant("Tesco")
merchant_repository.save(Tesco)
Virgin = Merchant("Virgin")
merchant_repository.save(Virgin)
WHSmith = Merchant("WHSmith")
merchant_repository.save(WHSmith)
Puregym = Merchant("Puregym")
merchant_repository.save(Puregym)

#Create tags
Bills = Tag("Bills")
tag_repository.save(Bills)
Groceries = Tag("Groceries")
tag_repository.save(Groceries)
Entertainment = Tag("Entertainment")
tag_repository.save(Entertainment)
Transportation = Tag("Transportation")
tag_repository.save(Transportation)
Health = Tag("Health")
tag_repository.save(Health)

#Create transactions
gym_membership = Transaction(14.99, Puregym,Health)
transaction_repository.save(gym_membership)