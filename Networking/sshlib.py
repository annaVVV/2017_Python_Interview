#!/usr/bin/env python

import warnings
warnings.simplefilter('ignore')
import paramiko
import socket
import time

class SshClient(object):

    TIMEOUT = None

    def __init__(self, host, port, username, password, keyfile=None, timeout=None):
        self.username = username
        self.password = password
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if keyfile is not None:
            self.client.connect(host, port, username=username,
                                password=password, key_filename=keyfile,
                                timeout=timeout)
        else:
            self.client.connect(host, port, username=username,
                                password=password, timeout=timeout)
        self.client.get_transport().set_keepalive(20)

    def close(self):
        if self.client is not None:
            self.client.close()
            self.client = None

    def execute_cmd(self, command, sudo=False):
        feed_password = False
        if sudo and self.username != "root":
            command = "sudo -k -S -p '' %s" % command
            feed_password = self.password is not None and len(self.password) > 0
        stdin, stdout, stderr = self.client.exec_command(command)
        if feed_password:
            stdin.write(self.password + "\n")
            stdin.flush()
        return {'out': stdout.readlines(),
                'err': stderr.readlines(),
                'retval': stdout.channel.recv_exit_status()}

    def copyfile(self, localfile, remotefile):
        transport = self.client.get_transport()
        self.sftp = paramiko.SFTPClient.from_transport(transport)
        self.sftp.put(localfile, remotefile)

    def getfile(self, remotefile, localfile):
        transport = self.client.get_transport()
        self.sftp = paramiko.SFTPClient.from_transport(transport)
        self.sftp.get(remotefile, localfile)

    def get_session(self):
        sess =  self.client.invoke_shell()
        sess.settimeout(99999)
        #sess.settimeout(None)
        return sess

    @staticmethod
    def execute_session_cmd(session, cmd, prompt='#'):
        session.send(cmd+"\n")
        output = ""
        while True: 
            output += session.recv(1024)
            if cmd.find('start_all') != -1: 
                time.sleep(5)
                session.send("\n")
                break
            if output.endswith((prompt,prompt+' ')):
                break
        return output

class ProxySshClient(object):
 
    TIMEOUT = None 

    def __init__(self, proxy_host, proxy_username, proxy_password, dest_host, dest_username, dest_password, keyfile=None, timeout=None):
       self._username = dest_username
       self._password = dest_password
       self._proxy_client = paramiko.SSHClient()
       self._proxy_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       if keyfile is not None:
           self._proxy_client.connect(proxy_host, port=22,
                                username=proxy_username, key_filename=keyfile,
                                timeout=timeout)
       else:
           self._proxy_client.connect(proxy_host, port=22,
                                username=proxy_username, password=proxy_password,
                                timeout=timeout)

       transport = self._proxy_client.get_transport()
       transport.set_keepalive(20)
       self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       self._s.bind(("",0))
       self._s.listen(1)
       self._port = self._s.getsockname()[1]
       self._s.close()

       self._dest_addr = (dest_host, 22)
       self._local_addr = ('127.0.0.1', self._port)
       channel = transport.open_channel("direct-tcpip", self._dest_addr, self._local_addr)

       self._client = paramiko.SSHClient()
       self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       self._client.connect('localhost', port=self._port, username=dest_username, sock=channel, password=dest_password)
       self._client.get_transport().set_keepalive(20)
       
 
    def close(self):
        if self._client is not None:
            self._client.close()
            self._client = None

    def execute_cmd(self, command, sudo=False):
        feed_password = False
        if sudo and self._username != "root":
            command = "sudo -k -S -p '' %s" % command
            feed_password = self._password is not None and len(self._password) > 0
        stdin, stdout, stderr = self._client.exec_command(command)
        if feed_password:
            stdin.write(self._password + "\n")
            stdin.flush()
        return {'out': stdout.readlines(),
                'err': stderr.readlines(),
                'retval': stdout.channel.recv_exit_status()}

    def copyfile(self, localfile, remotefile):
        transport = self._client.get_transport()
        self._sftp = paramiko.SFTPClient.from_transport(transport)
        self._sftp.put(localfile, remotefile)

    def getfile(self, remotefile, localfile):
        transport = self._client.get_transport()
        self._sftp = paramiko.SFTPClient.from_transport(transport)
        self._sftp.get(remotefile, localfile)

    def get_session(self):
        sess =  self._client.invoke_shell()
        sess.settimeout(99999)
        return sess

    @staticmethod
    def execute_session_cmd(session, cmd, prompt='#'):
        session.send(cmd+"\n")
        output = ""
        while True: 
            output += session.recv(1024)
            if cmd.find('start_all') != -1: 
                time.sleep(30)
                session.send("\n")
                break
            if output.endswith(prompt+' '):
                break
        return output
