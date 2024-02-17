# ETH Wallet Generator

## Overview
This Python script generates Ethereum wallet addresses along with their corresponding private keys and mnemonics. It utilizes elliptic curve cryptography and a mnemonic library to create wallet addresses and secure private keys.

## Prerequisites
Make sure you have Python 3.x installed on your system. Additionally, you need to install the following dependencies:

- ecdsa
- mnemonic

You can install them using pip:


## Usage
1. Clone this repository to your local machine.
```bash
    git clone https://github.com/harshjamdar/ETH-Wallet-Generator.git
    cd ETH-Wallet-Generator
    pip install -r requirements.txt 
```
2. Create a text file (e.g., `wallet_addresses.txt`) containing the ETH addresses you want to analyze .

3. Run the script by executing the following command in your terminal:
```bash
    python main.py 
```

4. The script will start generating wallet addresses along with private keys and mnemonics. It will display the progress and save the generated data to a CSV file named `generated_wallets.csv`.

i have added a sample file with about 1 million legacy address i am not sure are all addresses legacy so if u got error in any address just delete it from file

## Signal Handling
The script handles termination signals gracefully. You can stop the program at any time by pressing `Ctrl + C`.

## File Structure
- `main.py`: The main Python script.
- `generated_wallets.csv`: CSV file to store the generated wallet data.

## Disclaimer
This script is for educational purposes only. It generates wallet addresses and private keys for demonstration purposes and should not be used in a production environment without appropriate modifications and security measures.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
