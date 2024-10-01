import socket
import sys
import time

print('Usage: python host-resolve.py host port timeout(sec) msg')

argc = len(sys.argv)
if argc < 5:
    sys.exit()

print('Number of arguments:', argc, 'arguments.')
print('Argument List:', str(sys.argv))

host = sys.argv[1]
port = sys.argv[2]
timeout = float(sys.argv[3])
msg = sys.argv[4]

s = None
for res in socket.getaddrinfo(host, port):
    start = time.time()
    times = []
    error = ''
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
        s.settimeout(timeout)
        times.append(time.time())
        with s:
            s.connect(sa)
            times.append(time.time())
            s.sendall(msg.encode())
            times.append(time.time())
    except OSError as e:
        times.append(time.time())
        error = e
    finally:
        print(res, ' '.join(format((x - start), '.2f') for x in times), error)
