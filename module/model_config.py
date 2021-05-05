from google_drive_downloader import GoogleDriveDownloader

import os


def download_all_model():
    try:
        os.mkdir('model')
    except:
        pass

    model_1 = '1Z_Ov1nrMua43lv6vxGsIdRYvHH5nefAU'
    model_1_des = 'model/model.d2v'

    model_2 = '1-F1m_XPpSCitr_cuh1gB_4not15jDLKo'
    model_2_des = 'model/model_final.sav'

    GoogleDriveDownloader.download_file_from_google_drive(
        file_id=model_1,
        dest_path=model_1_des
    )

    GoogleDriveDownloader.download_file_from_google_drive(
        file_id=model_2,
        dest_path=model_2_des
    )
