
import zmq
import can
import time
import canInterface
import concurrent.futures
import threading
can = canInterface.canInterface('vcan0')
print("StartCAN")
#todo: multiprocessing pe can + zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:5560")
def zmqStart():
    print('Start ZMQ')
    while True:
        print('In Loop')
        #time.sleep(100)
        message = socket.recv()
        # if pipe.recv():
        #     messages[0]=pipe.recv()
        if message == b'112':
            socket.send(messages[0].getMessage())
        else:
            socket.send(b'No message')
        

messages=(canInterface.canMessage(112, 8), canInterface.canMessage(113, 8), 
                                       canInterface.canMessage(114, 8),canInterface.canMessage(115, 8),canInterface.canMessage(116, 8))

            
p1 = threading.Thread(target = zmqStart)
p2 = threading.Thread(target = can.start, args=[messages])

p1.start()
p2.start()
p1.join()
p2.join()
