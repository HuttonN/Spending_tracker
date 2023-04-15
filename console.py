from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

from models.tag import Tag
import repositories.tag_repository as tag_repository

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository


transaction_repository.delete_all()
merchant_repository.delete_all()
tag_repository.delete_all()