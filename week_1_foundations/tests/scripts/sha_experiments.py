import hashlib
import time
import matplotlib.pyplot as plt

# Simula un fitxer gran (6 GB) llegint blocs petits repetidament
class LargeFileSimulator:
    def __init__(self, total_size_gb, block_size=1024*1024):
        self.total_size = total_size_gb * 1024**3  # GB a bytes
        self.block_size = block_size
        self.read_bytes = 0
        self.data_block = b'0' * self.block_size  # bloc fix repetit

    def read(self, size=-1):
        if self.read_bytes >= self.total_size:
            return b''  # Final del fitxer simulat

        remaining_bytes = self.total_size - self.read_bytes
        read_size = min(size if size > 0 else self.block_size, remaining_bytes)
        self.read_bytes += read_size
        return self.data_block[:read_size]

# Calcula tots els SHA disponibles d'un fitxer simulat
def calculate_sha_large_file(file_simulator):
    sha_algorithms = {
        "SHA-1": hashlib.sha1(),
        "SHA-224": hashlib.sha224(),
        "SHA-256": hashlib.sha256(),
        "SHA-384": hashlib.sha384(),
        "SHA-512": hashlib.sha512(),
        "SHA3-224": hashlib.sha3_224(),
        "SHA3-256": hashlib.sha3_256(),
        "SHA3-384": hashlib.sha3_384(),
        "SHA3-512": hashlib.sha3_512()
    }

    results = {}
    for name, sha in sha_algorithms.items():
        file_simulator.read_bytes = 0  # reiniciar lectura per cada algorisme
        start_time = time.time()
        
        while True:
            data = file_simulator.read()
            if not data:
                break
            sha.update(data)

        end_time = time.time()
        elapsed_time = (end_time - start_time)
        results[name] = (sha.hexdigest(), elapsed_time)

    return results

# Crea un gràfic de barres amb els resultats
def plot_results(results):
    algorithms = list(results.keys())
    times = [results[alg][1] for alg in algorithms]

    plt.figure(figsize=(10, 6))
    plt.bar(algorithms, times, color='skyblue')
    plt.ylabel('Temps de càlcul (segons)')
    plt.xlabel('Algorisme SHA')
    plt.title('Temps necessari per calcular el hash SHA (fitxer simulat 6 GB)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    simulated_size_gb = 6  # Simulació fitxer de 6 GB
    file_simulator = LargeFileSimulator(simulated_size_gb)

    hashes = calculate_sha_large_file(file_simulator)

    print(f"Hashes SHA per un fitxer simulat de {simulated_size_gb} GB\n")
    for sha_name, (sha_hash, elapsed_time) in hashes.items():
        print(f"{sha_name}:\nTemps càlcul: {elapsed_time:.2f} segons\nHash: {sha_hash}\n")

    plot_results(hashes)


