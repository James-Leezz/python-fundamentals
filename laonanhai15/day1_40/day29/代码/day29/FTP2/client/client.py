

import socket
import os
import json
import struct
import hashlib

sock=socket.socket()
sock.connect(("127.0.0.1",8800))


while 1 :
    cmd=input("请输入命令：") # put 111.jpg

    action,filename=cmd.strip().split(" ")
    filesize=os.path.getsize(filename)

    file_info={
        "action": action,
        "filename": filename,
        "filesize": filesize,
    }
    file_info_json=json.dumps(file_info).encode("utf8")

    ret=struct.pack("i",len(file_info_json))
    # 发送 file_info_json的打包长度
    sock.send(ret)
    # 发送 file_info_json字节串
    sock.send(file_info_json)
    # 发送 文件数据
    md5=hashlib.md5()
    with open(filename,"rb") as f:
        for line in f:
            sock.send(line)
            md5.update(line)

    data=sock.recv(1024)
    print(md5.hexdigest())
    md5_val=md5.hexdigest()
    sock.send(md5_val.encode("utf8"))
    is_valid=sock.recv(1024).decode('utf8')
    if is_valid=="203":
        print("文件完整！")
    else:
        print("文件上传失败！")















