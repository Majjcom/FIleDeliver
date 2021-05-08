import os
import time
import getter
import sender

while True:
    try:
        # Show Menu
        os.system('cls')
        print('-----Python File Deliver_By:Majjcom-----\n')
        print(' 1--Get')
        print(' 2--Send')
        print(' 0--Exit')
        print('\n----------------------------------------')
        cho = input('Please input your order: ')

        if cho == '1':
            ip = input('Listen at: ')
            if '.' not in ip or ip.count('.') != 3:
                print('Please input right host...')
                time.sleep(1)
                continue
            port = input('Set your port: ')
            try:
                Addr = (ip, int(port))
                getter.listento(Addr)
            except ValueError:
                print('\nPlease input right number...')
                time.sleep(1)
                continue
        elif cho == '2':
            ip = input('Please input target host: ')
            if '.' not in ip or ip.count('.') != 3:
                print('Please input right host...')
                time.sleep(1)
                continue
            port = input('Please input target port: ')
            try:
                Addr = (ip, int(port))
            except ValueError:
                print('\nPlease input right number...')
                time.sleep(1)
                continue
            path_in = input('Please input file path: ')
            if os.path.exists(path_in):
                path_real = os.path.realpath(path_in)
                path_name = os.path.basename(path_real)
                path_re = path_real[:path_real.find(path_name)]
                sender.send(Addr, path_re, path_name)
            else:
                print('No such File...')
                time.sleep(1)
        elif cho == '0':
            cho = input('Are you sure?(y)')
            if cho == 'y':
                print('Program end...')
                time.sleep(0.75)
                break
        else:
            print('Are you serious?')
            time.sleep(1)
    except KeyboardInterrupt:
        cho = input('\nEXIT?(y)')
        if cho == 'y':
            print('Program end...')
            time.sleep(0.75)
            break
    except:
        print("\nUnexpected error:", sys.exc_info()[0])
        input('\nPress ENTER to continue...')
