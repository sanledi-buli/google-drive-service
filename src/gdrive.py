from apiclient import discovery
from apiclient.discovery import build

class GoogleDrive(object):

    def __init__(self,http):
        self.__http = http

    def fetch_all_files(self):
        service = discovery.build('drive', 'v3', http=self.__http)
        results = service.files().list().execute()
        items = results.get('files', [])
        return items