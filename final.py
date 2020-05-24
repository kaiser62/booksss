"""
Created on Sun Apr  7 15:05:26 2019
@author: June
"""

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
import argparse


auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)
parser = argparse.ArgumentParser()
parser.add_argument("something", help="Folder name")
args = parser.parse_args()
# View all folders and file in your Google Drive
fileList = drive.ListFile({
        'q': "'1JL10euIKvhBuncBUbWBSu4gNrWG_QpwO' in parents and trashed=false",
        'corpora': "teamDrive",
        'teamDriveId': "0AEWapxTnVfbZUk9PVA",
        'includeTeamDriveItems': "true",
        'supportsTeamDrives': "true"
    }).GetList()
for file in fileList:
 #print('Title: %s, ID: %s' % (file['title'], file['id']))
 if(file['title'] == (args.something)):
    fileID = file['id']
    a = str(('%s' % (file['id'])))
print('%s' % a)
