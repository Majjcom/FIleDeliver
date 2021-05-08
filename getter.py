import processbar
import socket
import time
import os

def listento(HostAddr):
    os.system('cls')
    try:
        # HostAddr = ('127.0.0.1', port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(HostAddr)
        s.listen(5)
        s.setblocking(True)

        # 监听，等待连接
        print('Listening: {}'.format(HostAddr))
        Linker, addr = s.accept()
        print('From:', addr)

        get_head = Linker.recv(512).decode('utf-8')
        get_head = get_head.split('#')
        get_packsize = int(get_head[0])
        get_packs = int(get_head[1])
        get_name = get_head[2]
        Linker.send('1'.encode('utf-8'))

        # Linker.close()

        path_f = str(__file__)
        name = os.path.basename(path_f)
        path = path_f[:path_f.find(name)] + 'GetFile\\'
        print('Crate File...')

        f = open(path + get_name, 'wb')

        print('Getting File...')
        for i in range(get_packs):
            while True:
                get = Linker.recv(get_packsize)
                if len(get) != 0:
                    break
            f.write(get)
            Linker.send('1'.encode('utf-8'))
            processbar.probar((i + 1) / get_packs, 25)

        Linker.close()
        s.close()
        f.close()

        print('\nFinish')
        print('File Saved at: \'{}\''.format(path))
        input()
        #time.sleep(2)
    except OSError:
        print('\nThe triminal has been used...')
        time.sleep(1)
    except KeyboardInterrupt:
        print('\nStop...')
        time.sleep(1)
        try:
            Linker.close()
            s.close()
            f.close()
        except:
            pass
    except:
        print("\nUnexpected error:", sys.exc_info()[0])
        try:
            Linker.close()
            s.close()
            f.close()
        except:
            pass
        input('\nPress ENTER to continue...')
