from threading import Thread
from typing import Dict, Optional, Union
from io import StringIO
from queue import Queue
from copy import deepcopy
import shortuuid
import socket
import json




class RealmMultiUserServerChat(Thread):
    def __init__(self, chat, id, host, port ):
        self.chat = chat
        self.id = id
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.addr = (host, port)
        Thread.__init__(self)

    def run(self):
        try:
            self.sock.connect(self.addr)
            while True:
                data = self.sock.recv(4096)
                if data:
                    res = self.chat.process(data.decode())
                    res_json = json.dumps(res)

                    self.sock.sendall(res_json.encode())
        except Exception as e:
            print(e)
            self.sock.close()
            return {"status": "ERROR", "message": f"Gagal di realm: {self.id}"}


class Chat:
    def __init__(self):
        self.sessions: Dict[str, str] = {}
        self.users: Dict[str, Union[str, Queue]] = {
            "messi": {
                "nama": "Lionel Messi",
                "negara": "Argentina",
                "password": "surabaya",
                "incoming": {},
                "outgoing": {},
            },
            "henderson": {
                "nama": "Jordan Henderson",
                "negara": "Inggris",
                "password": "surabaya",
                "incoming": {},
                "outgoing": {},
            },
            "lineker": {
                "nama": "Gary Lineker",
                "negara": "Inggris",
                "password": "surabaya",
                "incoming": {},
                "outgoing": {},
            },
        }
        self.realms: Dict[str, RealmMultiUserServerChat] = {
            "realm1": RealmMultiUserServerChat(
                host="127.0.0.1", port=9001, id="realm1", chat=deepcopy(self)
            )
        }

        for _, realm in self.realms.items():
            realm.start()

    def proses(self, data) -> Dict:
        data = data.split(" ")
        print(data)
        try:
            command = data[0].strip()

            if(command== "auth"):
                username = data[1].strip()
                password = data[2].strip()

                token = self.autentikasi_user(username=username, password=password)
                if token is None:
                    raise Exception("User tidak ada")

                return {"status": "OK", "token": token}

            elif(command== "send"):
                token = data[1].strip()
                username_to = data[2].strip()
                msg = StringIO()

                user_from = self.get_user_by_token(token)
                if user_from is None:
                    raise Exception("User belum terauntetikasi")

                if len(data[3:]) == 0:
                    raise IndexError

                for m in data[3:]:
                    msg.write(f"{m} ")

                return self.send_message(
                    username_from=self.get_username_by_dict(user_from),
                    username_to=username_to,
                    msg=msg.getvalue(),
                )

            elif(command== "inbox"):
                    token = data[1].strip()
                    username = self.get_username_by_token(token)
                    if username is None:
                        raise Exception("User belum terauntetikasi")

                    return self.get_inbox(username)

            elif (command == "send_group"):
                token = data[1].strip()
                username_lists = data[2].strip().split(",")
                msg = StringIO()

                user_from = self.get_user_by_token(token)
                if user_from is None:
                    raise Exception("User belum terauntetikasi")

                if len(username_lists) == 0:
                    raise IndexError

                if len(data[3:]) == 0:
                    raise IndexError

                for m in data[3:]:
                    msg.write(f"{m} ")

                return self.send_group(
                    username_from=self.get_username_by_dict(user_from),
                    username_to_send_lists=username_lists,
                    msg=msg.getvalue(),
                )

            elif(command== "send_private_realm"):
                    token = data[1].strip()
                    user_from = self.get_user_by_token(token)
                    if user_from is None:
                        raise Exception("User belum terauntetikasi")

                    username_to, realm_id = data[2].strip().split("#")
                    if realm_id not in self.realms:
                        raise Exception("Realm tidak ditemukan")

                    msg = StringIO()

                    if len(data[3:]) == 0:
                        raise IndexError

                    for m in data[3:]:
                        msg.write(f"{m} ")

                    return self.realms[realm_id].chat.send_message(
                        msg=msg.getvalue(),
                        username_from=self.get_username_by_dict(user_from),
                        username_to=username_to,
                    )

            elif(command== "send_group_realm"):
                    token = data[1].strip()
                    user_from = self.get_user_by_token(token)
                    if user_from is None:
                        raise Exception("User belum terauntetikasi")

                    username_lists = data[2].strip()
                    if len(username_lists) == 0:
                        raise IndexError

                    msg = StringIO()

                    if len(data[3:]) == 0:
                        raise IndexError

                    for m in data[3:]:
                        msg.write(f"{m} ")

                    print(username_lists, msg.getvalue())

                    return self.send_group_realm(
                        username_from=self.get_username_by_dict(user_from),
                        destination=username_lists,
                        msg=msg.getvalue(),
                    )

            elif(command== "send_inbox_realm"):
                    username, realm_id = data[1].strip().split("#")
                    return self.realms[realm_id].chat.get_inbox(
                        username=username, realm_id=realm_id
                    )

            else:
                raise IndexError

        except KeyError:
            return {"status": "ERROR", "message": "Informasi tidak ditemukan"}
        except IndexError:
            return {"status": "ERROR", "message": "**Protocol Tidak Benar"}
        except Exception as e:
            return {"status": "ERROR", "message": f"{e}"}

    def autentikasi_user(self, username, password) -> Optional[str]:
        user = self.users.get(username, None)
        if user is None:
            return None

        if user["password"] != password:
            return None

        token = shortuuid.uuid()
        self.sessions[token] = username

        return token

    def get_user_by_token(self, token) -> Optional[Dict]:
        username = self.sessions.get(token, None)
        return None if username is None else self.users[username]

    def get_username_by_token(self, token) -> Optional[str]:
        return self.sessions.get(token, None)

    def get_user_by_username(self, username) -> Optional[Dict]:
        try:
            return self.users[username]
        except KeyError:
            return None

    def get_username_by_dict(self, user: Dict) -> str:
        for key, val in self.users.items():
            if val == user:
                return key

        raise Exception("Terjadi kesalahan. Coba lagi")

    def send_message(self, msg, username_from, username_to) -> Dict:
        user_from = self.get_user_by_username(username_from)
        if user_from is None:
            raise Exception("User belum terauntetikasi")

        user_to = self.get_user_by_username(username_to)
        if user_to is None:
            raise Exception("User yang diinginkan tidak ditemukan")

        message = {
            "msg_from": user_from["nama"],
            "msg_to": user_to["nama"],
            "msg": msg,
        }

        outqueue_sender = user_from["outgoing"]
        inqueue_receiver = user_to["incoming"]

        username_from = self.get_username_by_dict(user_from)

        try:
            outqueue_sender[username_from].put(message)
        except KeyError:
            outqueue_sender[username_from] = Queue()
            outqueue_sender[username_from].put(message)
        try:
            inqueue_receiver[username_from].put(message)
        except KeyError:
            inqueue_receiver[username_from] = Queue()
            inqueue_receiver[username_from].put(message)
        return {"status": "OK", "message": "Message Sent"}

    def send_group(
        self, username_from, username_to_send_lists: list[str], msg
    ) -> Dict:
        
        for ug in username_to_send_lists:
            user = self.get_user_by_username(ug)
            if user is None:
                raise Exception("User yang diinginkan tidak ditemukan")

        for user_to in username_to_send_lists:
            self.send_message(username_from=username_from, username_to=user_to, msg=msg)

        return {"status": "OK", "message": f"Message Sent to {', '.join(username_to_send_lists)}"}

    def get_inbox(self, username, realm_id = "default") -> Dict:
        user_from = self.get_user_by_username(username)
        incoming = user_from["incoming"]

        msgs = {}

        for users in incoming:
            msgs[users] = []
            while not incoming[users].empty():
                msgs[users].append(user_from["incoming"][users].get_nowait())

        return {"status": "OK", "realm": realm_id, "messages": msgs}

    def send_group_realm(self, username_from, destination, msg) -> Dict:
        user_from = self.get_user_by_username(username_from)
        if user_from is None:
            raise Exception("User tidak ada")

        reformat_destination = self.set_realm_dst(destination)

        response = {"status": "OK"}

        for realm_id, users in reformat_destination.items():
            result = self.realms[realm_id].chat.send_group(
                username_from=username_from, username_to_send_lists=users, msg=msg
            )
            response[realm_id] = result

        return response

    def set_realm_dst(self, destination) -> Dict:
        elements = destination.split(",")
        if len(elements) == 0:
            raise IndexError

        result: Dict[str, list[str]] = {}

        for element in elements:
            username, realm_id = element.split("#")

            if realm_id not in self.realms:
                raise Exception(f"Realm {realm_id} tidak ditemukan")

            if realm_id in result:
                result[realm_id].append(username)
            else:
                result[realm_id] = [username]
        
        return result


if __name__ == "__main__":
    j = Chat()
    while True:
        cmd = input("Command: ")
        print(j.process(cmd))