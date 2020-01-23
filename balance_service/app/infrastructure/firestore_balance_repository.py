from google.cloud import firestore


class FirestoreBalanceRepository:

    def __init__(self, balance_collection):
        db = firestore.Client()
        self.balance_repo = db.collection(balance_collection)

    def store(self, account_number, account_data):
        doc_ref = self.balance_repo.document(account_number)
        doc_ref.set(account_data)

    def fetch_by_account_number(self, account_number):
        doc_ref = self.balance_repo.document(account_number)
        return doc_ref.get().to_dict()


class AccountNotFound(RuntimeError):
    def __init__(self, message='Account not found'):
        self.message = message
