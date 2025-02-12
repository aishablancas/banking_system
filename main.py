from use_cases.create_account import CreateAccountUseCase
from use_cases.make_transaction import MakeTransactionUseCase
from use_cases.generate_account_statement import GenerateAccountStatementUseCase
from infrastructure.account_repository import AccountRepository
import uuid

# Initialize repository
account_repository = AccountRepository()

# Use Case Instances
create_account_use_case = CreateAccountUseCase(account_repository)
make_transaction_use_case = MakeTransactionUseCase(account_repository)
generate_statement_use_case = GenerateAccountStatementUseCase(account_repository)

# Test Data
customer_id = str(uuid.uuid4())
name = "John Doe"
email = "john.doe@example.com"
phone_number = "123-456-7890"

# Create Account
account = create_account_use_case.create_account(customer_id, name, email, phone_number)
print(f"Account created: {account.account_number}, Balance: {account.get_balance()}")

# Make Transactions
make_transaction_use_case.make_transaction(account.account_id, 1000, "deposit")
make_transaction_use_case.make_transaction(account.account_id, 500, "withdraw")

# Generate Account Statement
statement = generate_statement_use_case.generate_account_statement(account.account_id)
print("\n" + statement)
