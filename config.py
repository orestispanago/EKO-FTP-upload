import json
import os

from dotenv import load_dotenv

dirname = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(dirname, ".env"))

with open(os.path.join(dirname, "config.json"), "r") as f:
    instruments = json.load(f)

INSTRUMENT = os.getenv("INSTRUMENT")
settings = instruments[INSTRUMENT]

FTP_IP = os.getenv("FTP_IP")
FTP_USER = os.getenv("FTP_USER")
FTP_PASS = os.getenv("FTP_PASS")
DIR = settings["DIR"]
PREFIX = settings["PREFIX"]
DATA_DIR = settings["DATA_DIR"]
