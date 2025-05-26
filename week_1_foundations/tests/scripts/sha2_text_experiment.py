import hashlib

# Defineix el missatge de prova
missatge_prova = "Aquest és el missatge per provar els algorismes SHA-2 a l'apartat d)."

# Funció que calcula SHA-2 amb les variants disponibles
def calcular_sha2(text):
    algorismes_sha2 = {
        "SHA-224": hashlib.sha224,
        "SHA-256": hashlib.sha256,
        "SHA-384": hashlib.sha384,
        "SHA-512": hashlib.sha512
    }

    resultats = {}
    for nom_alg, funcio_alg in algorismes_sha2.items():
        hash_value = funcio_alg(text.encode('utf-8')).hexdigest()
        resultats[nom_alg] = hash_value

    return resultats

# Executa la funció i mostra els resultats clarament
if __name__ == "__main__":
    print(f"Missatge original:\n'{missatge_prova}'\n")
    
    hashes = calcular_sha2(missatge_prova)

    for tipus_sha, resultat_hash in hashes.items():
        print(f"Tipus SHA-2: {tipus_sha}")
        print(f"Hash obtingut: {resultat_hash}\n")


