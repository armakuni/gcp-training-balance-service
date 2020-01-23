import base64
from google.cloud import firestore
import json
import os


def store_account_balance_update(event, context):
    account_data = json.loads(base64.b64decode(event['data']).decode('utf-8'))
    db = firestore.Client()
    balance_repo = db.collection(os.getenv(
        'BALANCE_NAMESPACE', 'account_balances')
    )
    doc_ref = balance_repo.document(account_data['accountNumber'])
    doc_ref.set(account_data)
