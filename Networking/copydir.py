#!/usr/bin/env python

import warnings
warnings.simplefilter('ignore')
import paramiko
import os
from stat import S_ISDIR

class SftpCopy(object):

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(host, port, username, password, timeout=60)
        transport = self.client.get_transport()
        self.sftp = paramiko.SFTPClient.from_transport(transport)

    def putfile(self, localfile, remotefile):
        self.sftp.put(localfile,remotefile)

    def put_all(self, localpath, remotepath):
        os.chdir(os.path.split(localpath)[0])
        parent=os.path.split(localpath)[1]
        for walker in os.walk(parent):
            try:
                self.sftp.mkdir(os.path.join(remotepath,walker[0]))
            except:
                pass
            for f in walker[2]:
                self.putfile(os.path.join(walker[0], f), os.path.join(remotepath,walker[0],f))

    def getfile(self, remotefile, localfile):
        self.sftp.get(remotefile, localfile)

    def sftp_walk(self, remotepath):
        path = remotepath
        files, folders = [], []
        for f in self.sftp.listdir_attr(remotepath):
            if S_ISDIR(f.st_mode):
                folders.append(f.filename)
            else:
                files.append(f.filename)
        yield path,folders,files
        for folder in folders:
            new_path = os.path.join(remotepath, folder)
            for x in self.sftp_walk(new_path):
                yield x

    def get_all(self, remotepath, localpath):
        self.sftp.chdir(os.path.split(remotepath)[0])
        parent = os.path.split(remotepath)[1]
        try:
            os.mkdir(localpath)
        except:
            pass
        for walker in self.sftp_walk(parent):
            try:
                os.mkdir(os.path.join(localpath, walker[0]))
            except:
                pass
            for f in walker[2]:
                self.getfile(os.path.join(walker[0], f), os.path.join(localpath,walker[0], f))

# Example:
if __name__ == '__main__':
    #sftp1 = SftpCopy('server_path', 22, 'usp-guest', 'password')
    #remotepath = r'/usp-archives/dev-snapshots/release-5.1.eft/5_1_0-541'
    localpath = r'/home/ubuntu/Auto_Deploy/5_1_0-541/isos'
    #sftp1.get_all(remotepath, localpath)
    sftp2 = SftpCopy('172.21.201.240', 22, 'ubuntu', 'passw')
    remotepath2 = r'/home/ubuntu'
    sftp2.put_all(localpath, remotepath2)
