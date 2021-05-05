from google_drive_downloader import GoogleDriveDownloader

import os


def download_all_model():
    try:
        os.mkdir('model')
    except:
        pass

    GoogleDriveDownloader.download_file_from_google_drive(
        file_id='1_CT6eSu63pfFdq4dXeFlV6OYjUBKfHAn',
        dest_path='model/model.d2v',
        showsize=True

    )

    GoogleDriveDownloader.download_file_from_google_drive(
        file_id='1-0pByu6ljf1JwrGiQSvXnMBOBrnxh-VU',
        dest_path='model/model_final.sav',
        showsize=True
    )
