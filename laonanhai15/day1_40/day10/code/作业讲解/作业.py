# by luffycity.com
import os
with open("a1.txt", mode="r", encoding="utf-8") as f1,\
    open("a1_副本.txt", mode="w", encoding="utf-8") as f2:
    f1.readable()
    f1.writable()
    for line in f1:
        if line == '我说的都是真的。哈哈':
            f2.write("你们就信吧~\n")

        f2.write(line)
os.remove("a1.txt")
os.rename("a1_副本.txt","a1.txt")