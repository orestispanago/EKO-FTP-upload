import logging
import os
from ftplib import FTP, error_perm

logger = logging.getLogger(__name__)


def ftp_mkdir_and_enter(ftp_session, dir_name):
    if dir_name not in ftp_session.nlst():
        ftp_session.mkd(dir_name)
        logger.debug(f"Created FTP directory {dir_name}")
    ftp_session.cwd(dir_name)


def ftp_make_dirs(ftp_session, folder_path):
    for f in folder_path.split("/"):
        ftp_mkdir_and_enter(ftp_session, f)


def ftp_upload_file(ftp_session, local_path, remote_path):
    with open(local_path, "rb") as f:
        ftp_session.storbinary(f"STOR {remote_path}", f)
    logger.info(f"Uploaded {local_path} to {remote_path}")


def ftp_upload_files(
    local_files,
    ip=None,
    user=None,
    passwd=None,
    dir=None,
    monthly_folders=False,
    prefix="",
):
    with FTP(ip, user, passwd) as ftp:
        ftp.cwd(dir)
        for local_file in local_files:
            base_name = os.path.basename(local_file)
            if monthly_folders:
                year = base_name[:4]
                month = base_name[4:6]
                remote_path = f"{year}/{month}/{prefix}{base_name}"
            else:
                remote_path = f"{prefix}{base_name}"
            try:
                ftp_upload_file(ftp, local_file, remote_path)
            except error_perm as e:
                if "55" in str(e):
                    ftp_make_dirs(ftp, os.path.dirname(remote_path))
                    ftp.cwd(dir)
                    ftp_upload_file(ftp, local_file, remote_path)
