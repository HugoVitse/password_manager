from flask import Flask, jsonify, request
from utils import write, aes

app = Flask(__name__)
from flask_cors import CORS

CORS(app)

@app.route('/get_vault', methods=['GET'])
def get_vault():
    
    vault = write.read("data/passwords")
    tag = write.read("data/tag")
    nonce = write.read("data/nonce")
    
    obj = {
        "vault":vault.hex(),
        "tag":tag.hex(),
        "nonce":nonce.hex()
    }
    

    return jsonify(obj)


@app.route('/get_unlocked_vault', methods=['GET'])
def get_unlocked_vault():
    
    vault = write.read("data/passwords")
    tag = write.read("data/tag")
    nonce = write.read("data/nonce")
    
    dec = aes.decrypt(vault,"ok",tag,nonce)
    

    return jsonify(dec)



@app.route('/set_vault', methods=['POST'])
def set_vault():
    
    vault = bytes.fromhex(request.form.get('vault'))
    tag = bytes.fromhex(request.form.get('tag'))
    nonce = bytes.fromhex(request.form.get('nonce'))
    
    write.write(vault,"data/passwords")
    write.write(tag,"data/tag")
    write.write(nonce,"data/nonce")
    

    return "ok"

@app.route('/get_password', methods=['POST'])
def get_password():
    
    host = request.json['host']
    print(host)
    vault = write.read("data/passwords")
    tag = write.read("data/tag")
    nonce = write.read("data/nonce")
    
    dec = aes.decrypt(vault,"ok",tag,nonce)
    
    info = next((i for i in dec if (host in i['data']['host']) ), None) 
    
    return jsonify(info)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)

