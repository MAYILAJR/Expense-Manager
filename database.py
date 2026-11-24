
import hvac
import psycopg
import os


def connect_db():
    try:
        # Connect to Vault
        client = hvac.Client(
            url=os.getenv("VAULT_ADDR"),
            token=os.getenv("VAULT_TOKEN")
        )

        if not client.is_authenticated():
            print("Vault authentication failed!")
            return None

        # Retrieve PostgreSQL credentials
        secret = client.secrets.kv.v2.read_secret_version(
            path="expense-manager",
            mount_point="secret"
        )

        credentials = secret["data"]["data"]

        # Connect to PostgreSQL
        connection = psycopg.connect(
            dbname=credentials["DB_NAME"],
            user=credentials["DB_USER"],
            password=credentials["DB_PASSWORD"],
            host=credentials["DB_HOST"],
            port=credentials["DB_PORT"]
        )

        return connection

    except Exception as error:
        print("Database connection failed!")
        print("Error:", error)
        return None
