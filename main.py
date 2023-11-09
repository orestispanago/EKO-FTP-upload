import datetime
import glob
import logging
import logging.config
import os
import traceback
from datetime import datetime

from uploader import ftp_upload_files
from utils import archive_past_days

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

IP = ""
USER = ""
PASSWORD = ""
DIR = "/dataloggers/test"
PREFIX = "eko_ms711_"

DATA_DIR = "C:\\Users\\orestis\\Desktop\\EKO-711"
ARCHIVE_DIR = f"{DATA_DIR}\\archive"

csv_files = glob.glob(f"{DATA_DIR}\\*\\*.csv")

today_fmt = datetime.utcnow().strftime("%Y%m%d")
today_files = glob.glob(f"{DATA_DIR}\\*\\{today_fmt}*.csv")
older_files = list(set(csv_files) - set(today_files))


def main():
    ftp_upload_files(
        ip=IP,
        user=USER,
        passwd=PASSWORD,
        dir=DIR,
        local_files=csv_files,
        monthly_folders=True,
        prefix=PREFIX,
    )
    archive_past_days(older_files, folder=ARCHIVE_DIR, prefix=PREFIX)


if __name__ == "__main__":
    try:
        main()
    except:
        logger.error("uncaught exception: %s", traceback.format_exc())
