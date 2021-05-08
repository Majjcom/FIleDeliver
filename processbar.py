import time

# █
def probar(precent, lenth=0, time0=0):
    len = int(precent * lenth)
    bar = '|'
    for i in range(len):
        bar += '='
    for i in range(lenth - len):
        bar += ' '
    bar += '|' + str(round(precent * 100, 1)) + '%/100%'
    if time0 != 0:
        try:
            timerest = (1 - precent) / (precent / (time.time() - time0))
            bar += ' res=' + str(round(timerest))
        except:
            pass
    print('\r', bar + '   ', end='', flush=True)
