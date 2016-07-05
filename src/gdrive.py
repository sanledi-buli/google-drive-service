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

    def get_file_by_id(self,file_id):
        result = self.__service_v2.files().get(fileId=file_id).execute()
        return result

    def set_permissions(self, file_id, permissions = {}):
        self.__service_v2.permissions().insert(fileId=file_id, body=permissions).execute()