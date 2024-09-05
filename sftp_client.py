#from main.models import PsEndpoints, prov_settings,  PsAuths, prov_logs
# перестало работать , похоже на баги в openssh для windows
import paramiko
import requests
import re
import uuid


    

# пример работы с классом sftpclient
# with Sftpclient('msk-co-yealink.ivoin.ru', 22, 'user', 'passwd', 
#                 '/home/testdeb/admin-panel-asterisk/apps/main/models.py', 'C:\\Yealink\\Configs\\tst.txt') as sftp:
#      sftp.upload_file_to_server()
class Sftpclient:

    def __init__(self, host, port, username, password, local_file, remote_path, remote_name):
        self.__host = host
        self.__port = port
        self.__username = username
        self.__password = password
        self.__local_file = local_file
        self.__remote_path = remote_path
        self.__remote_name = remote_name

    
    def create_sftp_client(self):
        transport = paramiko.Transport((self.__host, self.__port))
        transport.connect(username=self.__username, password=self.__password)
        self.__sftp_client = paramiko.SFTPClient.from_transport(transport)
        

    def upload_file_to_server(self):
        try:
            self.__sftp_client.chdir(self.__remote_path)  # Test if remote_path exists
        except IOError:
            self.__sftp_client.mkdir(self.__remote_path)  # Create remote_path
        self.__sftp_client.put(self.__local_file, self.__remote_path + self.__remote_name)

    def download_file_from_server(self):
        self.__sftp_client.get(self.__remote_path + self.__remote_name, self.__local_file)

    def __enter__(self):
        self.create_sftp_client()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__sftp_client.close()



