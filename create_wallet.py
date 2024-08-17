import bittensor as bt

wallet = bt.wallet(name = 'm_coldkey1', hotkey = 'm_hotkey1')
wallet.create_if_non_existent()
