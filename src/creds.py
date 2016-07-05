import httplib2
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials

class AuthorizeHttp(object):

    def __init__(self, scopes, client_email, creds_file):
        self.__scopes = scopes
        self.__client_email = client_email
        self.__creds_file = creds_file
        self.http = self._set_http()

    def _set_http(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.__creds_file, self.__scopes)
        http = httplib2.Http()
        http = credentials.authorize(http)
        return http