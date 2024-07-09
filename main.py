
import requests
from web3 import Web3
from config import FAUCET_URLS, ALCHEMY_API_KEY, WALLETS, MAIN_WALLET

def request_coins(wallet):
    for faucet_url in FAUCET_URLS:
        response = requests.post(faucet_url, data={"address": wallet})
        if response.status_code == 200:
            print(f"Requested coins for {wallet} from {faucet_url}")
        else:
            print(f"Failed to request coins for {wallet} from {faucet_url}")

def transfer_coins(wallet, amount):
    w3 = Web3(Web3.HTTPProvider(f"https://eth-sepolia.alchemyapi.io/v2/{ALCHEMY_API_KEY}"))
    w3.eth.default_account = wallet

    tx = {
        'to': MAIN_WALLET,
        'value': w3.toWei(amount, 'ether'),
        'gas': 2000000,
        'gasPrice': w3.toWei('50', 'gwei')
    }

    signed_tx = w3.eth.account.sign_transaction(tx, private_key='your_private_key')
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Transaction sent: {tx_hash.hex()}")

def main():
    for wallet in WALLETS:
        request_coins(wallet)
    
    # Assuming some logic to determine the amount to transfer
    for wallet in WALLETS:
        transfer_coins(wallet, 0.1)

if __name__ == "__main__":
    main()
