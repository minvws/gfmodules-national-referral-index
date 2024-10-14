import inject
from app import application
from app import container
from app.config import Config
from app import dependencies

if __name__ == "__main__":
    container.configure()

    config = inject.instance(Config)
    application.setup_logging(config)

    db = dependencies.get_database()
    db.generate_tables()
