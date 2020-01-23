from balance_service.app import app
from balance_service.app.config import config
from balance_service.app.infrastructure.firestore_balance_repository import \
    FirestoreBalanceRepository

if __name__ == "__main__":
    app.create(config=config, balance_repository=FirestoreBalanceRepository(
        config.BALANCE_NAMESPACE)).run(host='0.0.0.0', port=config.PORT)
