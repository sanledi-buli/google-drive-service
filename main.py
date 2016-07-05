from src.creds import AuthorizeHttp
from src.gdrive import GoogleDrive
import yaml
import os

with open("settings.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

http  = AuthorizeHttp(cfg['SCOPES'], cfg['CLIENT_EMAIL'], os.path.realpath(cfg['CREDENTIAL_FILE_PATH'])).http
gdrive = GoogleDrive(http)