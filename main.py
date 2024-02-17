import os
import time
import hashlib
import binascii
import csv
import signal
from ecdsa import SigningKey, SECP256k1
from mnemonic import Mnemonic

# Define a global variable to indicate whether the program should continue running
running = True

# Define a signal handler to catch termination signal (e.g., clicking 'X' button)
def signal_handler(sig, frame):
    global running
    print("\nStopping the program...")
    running = False

def generate_private_key():
    return SigningKey.generate(curve=SECP256k1)

def derive_public_key(private_key):
    return private_key.get_verifying_key()

def generate_wallet_address(public_key):
    public_key_bytes = public_key.to_string()
    sha256_hash = hashlib.sha256(public_key_bytes).digest()
    ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()
    wallet_address = ripemd160_hash
    return wallet_address.hex()

def generate_mnemonic():
    mnemo = Mnemonic("english")
    return mnemo.generate(strength=128)

def load_generated_data(file_path):
    data = []
    if os.path.exists(file_path):
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                data.append(row)
    return data

def save_to_csv(file_path, data):
    headers = ["Private Key", "Mnemonic", "Wallet Address"]
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

def main():
    global running
    attempts = 0
    generated_data = []

    # Register the signal handler for SIGINT (termination signal)
    signal.signal(signal.SIGINT, signal_handler)

    # Load previously generated data
    generated_data += load_generated_data("generated_wallets.csv")

    start_time = time.time()
    try:
        while running:
            private_key = generate_private_key()
            public_key = derive_public_key(private_key)
            wallet_address = generate_wallet_address(public_key)
            mnemonic = generate_mnemonic()
            attempts += 1

            if [private_key.to_string().hex(), mnemonic, f"0x{wallet_address}"] not in generated_data:
                generated_data.append([private_key.to_string().hex(), mnemonic, f"0x{wallet_address}"])

            if attempts % 1000 == 0:
                elapsed_time = time.time() - start_time
                rate = attempts / elapsed_time
                print(f"Attempts made: {attempts}")
                print(f"Rate of checking: {rate:.2f} attempts per second")

                # Save generated keys to CSV every 1000 attempts
                save_to_csv("generated_wallets.csv", generated_data)
    except KeyboardInterrupt:
        print("Stopping the program...")

if __name__ == "__main__":
    main()
