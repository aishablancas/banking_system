from infrastructure.account_repository import AccountRepository

class GenerateAccountStatementUseCase:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def generate_account_statement(self, account_id: str) -> str:
        account = self.account_repository.find_account_by_id(account_id)
        
        if account is None:
            return "Account not found."

        statement = f"Account Statement for {account.account_number}:\n"
        statement += "\n".join(account.transactions) if account.transactions else "No transactions yet."
        return statement
