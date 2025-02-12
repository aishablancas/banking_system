from domain.account import Account
from domain.customer import Customer
from infrastructure.account_repository import AccountRepository
import uuid

class CreateAccountUseCase:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def create_account(self, customer_id: str, name: str, email: str, phone_number: str) -> Account:
        customer = Customer(customer_id, name, email, phone_number)
        account_id = str(uuid.uuid4())
        account_number = str(uuid.uuid4())[:8]  # Simulating an 8-digit account number
        new_account = Account(account_id, customer_id, account_number)

        self.account_repository.save_account(new_account)
        return new_account
