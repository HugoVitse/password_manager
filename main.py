from utils import aes,write

test = [
    {
        "id":1,
        "data":{
            "host":"google.com",
            "username":"hugo",
            "password":"azerty"
        }
    }
]

t, tag , nonce = aes.encrypt(test,"ok")

write.write(t,"data/passwords")
write.write(tag,"data/tag")
write.write(nonce,"data/nonce")



t1 = write.read("data/passwords")
tag1 = write.read("data/tag")
nonce1 = write.read("data/nonce")


dec = aes.decrypt(t1,"ok",tag1,nonce1)

print(dec[0]["data"])