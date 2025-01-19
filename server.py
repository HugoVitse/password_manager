from flask import Flask, jsonify, request
from utils import write

app = Flask(__name__)


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



@app.route('/set_vault', methods=['POST'])
def set_vault():
    
    vault = bytes.fromhex(request.form.get('vault'))
    tag = bytes.fromhex(request.form.get('tag'))
    nonce = bytes.fromhex(request.form.get('nonce'))
    
    write.write(vault,"data/passwords")
    write.write(tag,"data/tag")
    write.write(nonce,"data/nonce")
    

    return "ok"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

