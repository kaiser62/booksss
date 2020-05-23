"""
Created on Sun Apr  7 15:05:26 2019
@author: June
"""

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials


auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)
tgt_folder_id = '0AEWapxTnVfbZUk9PVA'

# View all folders and file in your Google Drive
fileList = drive.ListFile({
        'q': "'0AEWapxTnVfbZUk9PVA' in parents and trashed=false",
        'corpora': "teamDrive",
        'teamDriveId': "0AEWapxTnVfbZUk9PVA",
        'includeTeamDriveItems': "true",
        'supportsTeamDrives': "true"
    }).GetList()
for file in fileList:
 print('Title: %s, ID: %s' % (file['title'], file['id']))