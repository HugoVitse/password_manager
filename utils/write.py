def write(data:bytes, path: str):
    with open(path, 'wb') as fichier:
        fichier.write(data)
        
def read(path:str) -> bytes :
    with open(path, 'rb') as fichier:
        contenu = fichier.read()
        return contenu