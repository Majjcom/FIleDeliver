import processbar
import socket
import time
import os

def send(addr, file, name):
    os.system('cls')
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 键入文件路径和名称  *注意：路径最后请务必加上“/”
        #file = '/home/pi/Bookshelf/'
        #name = '电脑视频转换工具+教程视频（右键解压）.rar'

        byte = 1024
        f = open(file + name, 'rb+')
        lenth = os.path.getsize(file + name)
        send_packs = int(lenth / byte) + 1
        if lenth % byte == 0:
            send_packs -= 1
        send_head = '{}#{}#{}'.format('1024', send_packs, name)
        #addr = ('121.4.176.158', 12568)

        s.connect(addr)
        s.send(send_head.encode('utf-8'))

        while True:
            tmp = s.recv(512)
            if tmp.decode('utf-8') == '1':
                break
        print('Sending...')
        for i in range(send_packs):
            s.send(f.read(byte))
            while True:
                tmp = s.recv(512)
                if tmp.decode('utf-8') == '1':
                    break
            processbar.probar((i + 1) / send_packs, 25)

        s.close()
        f.close()

        print('\nfinish')
        time.sleep(2)
    except FileNotFoundError:
        print('\nNo such file...')
        try:
            s.close()
        except:
            pass
        time.sleep(1)
    except IsADirectoryError:
        print('\nPlease don\'t input DIRECTORY...')
        try:
            s.close()
        except:
            pass
        time.sleep(1)
    except ConnectionRefusedError:
        print('\nConnection Refused...')
        try:
            s.close()
        except:
            pass
        time.sleep(1)
    except KeyboardInterrupt:
        print('\nStop...')
        try:
            s.close()
            f.close()
        except:
            pass
        time.sleep(1)
    except:
        print("\nUnexpected error:", sys.exc_info()[0])
        try:
            s.close()
            f.close()
        except:
            pass
        input('\nPress ENTER to continue...')
