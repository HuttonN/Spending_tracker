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

#Create transaction
mortage_Apr_23 = Transaction(663.35,Natwest_Bank,Bills,datetime(2023,4,3))
transaction_repository.save(mortage_Apr_23)
mortage_Mar_23 = Transaction(663.35,Natwest_Bank,Bills,datetime(2023,3,1))
transaction_repository.save(mortage_Mar_23)
mortage_Feb_23 = Transaction(663.35,Natwest_Bank,Bills,datetime(2023,3,1))
transaction_repository.save(mortage_Feb_23)
mortage_Jan_23 = Transaction(663.35,Natwest_Bank,Bills,datetime(2023,2,3))
transaction_repository.save(mortage_Jan_23)
monthly_gym_March = Transaction(14.99,Puregym,Health,datetime(2023,3,31))
transaction_repository.save(monthly_gym_March)

transaction_list = [mortage_Jan_23, mortage_Feb_23, mortage_Apr_23, mortage_Mar_23]

# x = datetime.strftime(mortage_Apr_23.date,'%Y-%m-%d')
# y = datetime.strftime(mortage_Feb_23.date,'%Y-%m-%d')
# list = [x,y]
# list.sort(key= lambda x: datetime.strptime(x, '%Y-%m-%d'))
# print(list)