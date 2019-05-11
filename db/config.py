import configparser
import os
from dataclasses import dataclass


path = "settings.ini"

def createConfig(path):
    """
    Create a config file postgresql+psycopg2://postgres:123@localhost:port/publishing_company3
    """
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "backend", "postgresql+psycopg2")
    config.set("Settings", "user", "postgres")
    config.set("Settings", "password", "123")
    config.set("Settings", "hostname", "localhost")
    config.set("Settings", "port", "5432")
    config.set("Settings", "database", "publishing_company3")

    with open(path, "w") as config_file:
        config.write(config_file)


def get_settings():
    conf_path = 'settings.ini'
    config = configparser.ConfigParser()
    config.read(conf_path)

    backend = config.get("Settings", "backend")
    user = config.get("Settings", "user")
    password = config.get("Settings", "password")
    hostname = config.get("Settings", "hostname")
    port = config.get("Settings", "port")
    database = config.get("Settings", "database")
    return backend, user, password, hostname, port, database


@dataclass
class Config:
    backend: str
    user: str
    password: str
    hostname: str
    port: str
    database: str



if not os.path.exists(path):
    createConfig(path)
conf = Config(*get_settings())

if __name__ == "__main__":

    print(conf)
