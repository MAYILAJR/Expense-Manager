
import hvac
import os

client = hvac.Client(
    url=os.getenv("VAULT_ADDR"),
    token=os.getenv("VAULT_TOKEN")
)

if client.is_authenticated():
    print("Vault authentication successful!")

    secret = client.secrets.kv.v2.read_secret_version(
        path="expense-manager",
        mount_point="secret"
    )

    credentials = secret["data"]["data"]

    print("Secrets retrieved successfully!")
    print("Database:", credentials["DB_NAME"])
    print("User:", credentials["DB_USER"])
    print("Host:", credentials["DB_HOST"])
    print("Port:", credentials["DB_PORT"])

else:
    print("Vault authentication failed!")
