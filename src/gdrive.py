from apiclient import discovery
from apiclient.discovery import build

class GoogleDrive(object):

    def __init__(self,http):
        self.__service_v2 = discovery.build('drive', 'v2', http=http)
        self.__service_v3 = discovery.build('drive', 'v3', http=http)

    def get_all_files(self):
        results = self.__service_v3.files().list().execute()
        items = results.get('files', [])
        return items