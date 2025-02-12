from infrastructure.account_repository import AccountRepository

class MakeTransactionUseCase:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def make_transaction(self, account_id: str, amount: float, transaction_type: str):
        account = self.account_repository.find_account_by_id(account_id)

        if account is None:
            raise ValueError("Account not found")

        if transaction_type == "deposit":
            account.deposit(amount)
        elif transaction_type == "withdraw":
            account.withdraw(amount)
        else:
            raise ValueError("Invalid transaction type. Use 'deposit' or 'withdraw'.")

        self.account_repository.save_account(account)
