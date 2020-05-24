"""
Created on Sun Apr  7 15:05:26 2019
@author: June
"""

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import argparse
gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")
drive = GoogleDrive(gauth)


parser = argparse.ArgumentParser()
parser.add_argument("something", help="Folder name")
args = parser.parse_args()
# View all folders and file in your Google Drive
fileList = drive.ListFile({
        'q': "'0AEWapxTnVfbZUk9PVA' in parents and trashed=false",
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
       

      

