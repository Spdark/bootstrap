from flask import Flask, redirect, render_template, request, url_for
from flask_socketio import SocketIO
import hashlib
import json
import time
from db import save_block


class Block():
    def __init__(self,nonce,tstamp,transaction,prevhash = ''):
        self.nonce = nonce
        self.tstamp = tstamp
        self.transaction = transaction
        self.prevhash = prevhash
        self.hash = self.calcHash()

    def calcHash(self):
        block_string=json.dumps({"nonce":self.nonce,"tstamp":self.tstamp,"transaction":self.transaction,"prevhash":self.prevhash},sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def __str__(self):
        string  = "nonce: " + str(self.nonce) + "\n"
        string += "tstamp: " + str(self.tstamp)+ "\n"
        string += "transaction: " + str(self.transaction)+ "\n"
        string += "prevhas: " + str (self.prevhash)+ "\n"
        string += "hash: " + str (self.hash)+ "\n"
        save_block(self.nonce,self.tstamp,self.transaction,self.prevhash,self.hash)
        return string

class Blockchain():
    def __init__(self):
        self.chain=[self.generateGensisBlock(),]
        self.t_block = ['Gensis Block',]
    def generateGensisBlock(self):
        return Block(1,'01/01/2017','Gensis Block')
    def getLastBlock(self):
        return self.chain[-1]
    def addBlock(self,newBlock,msg):
        newBlock.prevhash = self.getLastBlock().hash
        newBlock.hash = newBlock.calcHash()
        self.chain.append(newBlock)
        self.t_block.append(msg)


    def isChainValid(self):
        for i in range(1,len(self.chain)):
            prevb = self.chain[i-1]
            currb = self.chain[-1]
            if(currb.hash != currb.calcHash()):
                return False
            if(currb.prevhash != prevb.hash):
                return False
        return True

blockchain = Blockchain()
#blockchain.addBlock(Block(1,'20/05/2020','100'))

app = Flask(__name__)
app.secret_key = "my secret key"
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('bar.html')


@socketio.on('send_message')
def handle_msg(data):
    n = 0
    msg = ''
    l = len(blockchain.chain)
    if (data['currentStep'] == 1):
        msg1 = "Importer send the Bill of landing to Custom "
        msg2 = "Custom owns Bill of Landing send by Importer"
        msg = msg1 + msg2
        blockchain.addBlock(Block(l+1,time.time(),msg),msg)
        data.update({'msg':msg})
        socketio.emit('receive_message', data)
    elif (data['currentStep'] == 2):
        n = data['currentStep']
        msg1 = "Custom send the Bill of landing to Exporter Bank "
        msg2 = "Exporter Bank owns Bill of Landing send by Custom"
        msg = msg1 + msg2
        blockchain.addBlock(Block(l+1,time.time(),msg),msg)
        data.update({'msg':msg})
        socketio.emit('receive_message', data)
    elif (data['currentStep'] == 3):
        n = data['currentStep']
        msg1 = "Exporter Bank send the Bill of landing to Custom "
        msg2 = "Custom owns Bill of Landing send by Custom"
        msg = msg1 + msg2
        blockchain.addBlock(Block(l+1,time.time(),msg),msg)
        data.update({'msg':msg})
        socketio.emit('receive_message', data)
    elif (data['currentStep'] == 4):
        n = data['currentStep']
        msg1 = "Custom send the Bill of landing to Exporter "
        msg2 = "Exporter owns Bill of Landing send by Customs"
        msg = msg1 + msg2
        blockchain.addBlock(Block(l+1,time.time(),msg),msg)
        data.update({'msg':msg})
        socketio.emit('receive_message', data)

    for i in blockchain.chain:
        print(i)

if __name__ == '__main__':
    socketio.run(app,port=5001,debug=True)