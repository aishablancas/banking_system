from domain.account import Account

class AccountRepository:
    def __init__(self):
        self.accounts = {}

    def save_account(self, account: Account):
        self.accounts[account.account_id] = account

    def find_account_by_id(self, account_id: str) -> Account:
        return self.accounts.get(account_id, None)

    def find_accounts_by_customer_id(self, customer_id: str):
        return [account for account in self.accounts.values() if account.customer_id == customer_id]

