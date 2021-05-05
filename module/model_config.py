from google_drive_downloader import GoogleDriveDownloader

import os


def download_all_model():
    try:
        os.mkdir('model')
    except:
        pass

    model_1 = '1_CT6eSu63pfFdq4dXeFlV6OYjUBKfHAn'
    model_1_des = 'model/model.d2v'

    model_2 = '1-0pByu6ljf1JwrGiQSvXnMBOBrnxh-VU'
    model_2_des = 'model/model_final.sav'

    try:
        GoogleDriveDownloader.download_file_from_google_drive(
            file_id=model_1,
            dest_path=model_1_des
        )
    except:
        redownload(model_1, model_1_des)

    try:
        GoogleDriveDownloader.download_file_from_google_drive(
            file_id=model_2,
            dest_path=model_2_des
        )
    except:
        redownload(model_2, model_2_des)


def redownload(file_id, destination):
    GoogleDriveDownloader.download_file_from_google_drive(
        file_id=file_id,
        dest_path=destination,
        overwrite=True
    )
