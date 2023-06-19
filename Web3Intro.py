#import packages
from web3 import  Web3

infura_url = "https://mainnet.infura.io/v3/596ca473ac0f403fa5e802b38d7da783"
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.is_connected())


print(web3.eth.block_number)

eth_address = "0x1e0b908c935B9B121aE046A256E45781F56fa4d6"

balance_in_wei = web3.eth.get_balance(eth_address) # gives result in Wei

balance_in_ether = balance_in_wei / 10 ** 18

balance_in_ether_2 = web3.from_wei(balance_in_wei, "ether") # gives result in ether





# This is a test


# # convert 1 ether to the lowest unit 'Wei'
# print(Web3.toWei(1,'ether'))


# # convert from 'Wei' to ether
# print(Web3.fromWei(500000000, 'gwei'))


# w3 = Web3(Web3.EthereumTesterProvider())




