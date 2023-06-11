import socket
import json

TARGET_IP = "127.0.0.1"
TARGET_PORT = 9999


class ChatClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (TARGET_IP,TARGET_PORT)
        self.sock.connect(self.server_address)
        self.tokenid=""
    
    def proses(self,cmdline):
        j=cmdline.split(" ")
        try:
            command=j[0].strip()
            if (command=='auth'):
                username=j[1].strip()
                password=j[2].strip()
                return self.login(username,password)
            elif (command=='send'):
                usernameto = j[1].strip()
                message=""
                for w in j[2:]:
                   message="{} {}" . format(message,w)
                return self.sendmessage(usernameto,message)
            elif (command=='inbox'):
                self.inbox()
            elif(command == "send_group"):
                    groups_to = j[1].strip()
                    message = ""
                    for w in j[2:]:
                        message = "{} {}".format(message, w)

                    return self.send_group(groups_to, message)

            elif(command == "send_private_realm"):
                    destination = j[1].strip()
                    message = ""
                    for w in j[2:]:
                        message = "{} {}".format(message, w)

                    return self.send_private_realm(destination, message)

            elif(command == "send_group_realm"):
                    destination = j[1].strip()
                    message = ""
                    for w in j[2:]:
                        message = "{} {}".format(message, w)

                    return self.send_group_realm(destination, message)

            elif(command == "send_inbox_realm"):
                    destination = j[1].strip()
                    return self.send_inbox_realm(destination)

            else :
                return "*Maaf, command tidak benar"
        except IndexError:
            return "-Maaf, command tidak benar"
    def sendstring(self,string):
        try:
            self.sock.sendall(string.encode())
            receivemsg = ""
            while True:
                data = self.sock.recv(64)
                print("diterima dari server",data)
                if (data):
                    receivemsg = "{}{}" . format(receivemsg,data.decode())  #data harus didecode agar dapat di operasikan dalam bentuk string
                    if receivemsg[-4:]=='\r\n\r\n':
                        print("end of string")
                        return json.loads(receivemsg)
        except:
            self.sock.close()
            return { 'status' : 'ERROR', 'message' : 'Gagal'}
    def login(self,username,password):
        string="auth {} {} \r\n" . format(username,password)
        result = self.sendstring(string)
        if result['status']=='OK':
            self.tokenid=result['token']
            return "username {} logged in, token {} " .format(username,self.tokenid)
        else:
            return "Error, {}" . format(result['message'])
    def sendmessage(self,usernameto="xxx",message="xxx"):
        if (self.tokenid==""):
            return "Error, not authorized"
        string="send {} {} {} \r\n" . format(self.tokenid,usernameto,message)
        print(string)
        result = self.sendstring(string)
        if result['status']=='OK':
            return "message sent to {}" . format(usernameto)
        else:
            return "Error, {}" . format(result['message'])
    def inbox(self):
        if (self.tokenid==""):
            return "Error, not authorized"
        string="inbox {} \r\n" . format(self.tokenid)
        result = self.sendstring(string)
        if result['status']=='OK':
            return "{}" . format(json.dumps(result['messages']))
        else:
            return "Error, {}" . format(result['message'])

    def send_group(self, dst, message):
        if self.tokenid == "":
            return "Error, not authorized"
        string = "send_group {} {} {} \r\n".format(self.tokenid, dst, message)
        result = self.sendstring(string)
        if result["status"] == "OK":
            return "{}".format(json.dumps(result["message"]))
        else:
            return "Error, {}".format(result["message"])

    def send_private_realm(self, dst, message):
        if self.tokenid == "":
            return "Error, not authorized"

        string = "send_private_realm {} {} {} \r\n".format(
            self.tokenid, dst, message)
        result = self.sendstring(string)
        if result["status"] == "OK":
            return "{}".format(json.dumps(result["message"]))
        else:
            return "Error, {}".format(result["message"])

    def send_group_realm(self, dst, message):
        if self.tokenid == "":
            return "Error, not authorized"
        string = "send_group_realm {} {} {} \r\n".format(
            self.tokenid, dst, message)
        result = self.sendstring(string)
        if result["status"] == "OK":
            return "{}".format(json.dumps(result))
        else:
            return "Error, {}".format(result)

    def send_inbox_realm(self, dst):
        if self.tokenid == "":
            return "Error, not authorized"

        string = "send_inbox_realm {} \r\n".format(dst)
        result = self.sendstring(string)
        if result["status"] == "OK":
            return "{}".format(json.dumps(result["messages"]))
        else:
            return "Error, {}".format(result["messages"])


if __name__ == "__main__":
    cc = ChatClient()
    while True:
        cmdline = input("Command {}: ".format(cc.tokenid))
        print(cc.proses(cmdline))