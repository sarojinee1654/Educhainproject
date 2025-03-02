from web3 import Web3

def store_hash_on_blockchain(certificate_hash):
    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))
    contract_address = 'YOUR_CONTRACT_ADDRESS'
    contract_abi = 'YOUR_CONTRACT_ABI'
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)
    tx_hash = contract.functions.storeHash(certificate_hash).transact()
    return tx_hash