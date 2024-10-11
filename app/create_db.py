import inject
from app import application
from app import container
from app.config import Config

if __name__ == "__main__":
    config = inject.instance(Config)
    application.setup_logging(config)

    db = container.get_database()
    db.generate_tables()
