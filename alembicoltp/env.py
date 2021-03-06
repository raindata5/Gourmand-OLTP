from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
import configparser
from sqlalchemy.ext.declarative import declarative_base

from alembic import context
parser = configparser.ConfigParser()
# parser.read("db.conf")
# host = parser.get("mssqlLocal", "host")
# user = parser.get("mssqlLocal", "user")
# password = parser.get("mssqlLocal", "password")
# db = parser.get("mssqlLocal", "db")

# host = parser.get("postgres_oltp", "DB_HOST")
# user = parser.get("postgres_oltp", "DB_USER")
# password = parser.get("postgres_oltp", "DB_PASS")
# db = parser.get("postgres_oltp", "DB_NAME")
# port = parser.get("postgres_oltp", "DB_PORT")


Base = declarative_base()



# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)
# config.set_main_option("sqlalchemy.url", f"postgresql://{user}:{password}@{host}:{port}/postgres")
# config.set_main_option("sqlalchemy.url", f"mssql+pymssql://{user}:{password}@{host}/{db}")


# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
