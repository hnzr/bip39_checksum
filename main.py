import bip39checksum

# usage :
# calculate checkshum problem "ignore sponsor decline nerve brain vast short hollow cheap rotate stadium scale elevator kit legend planet alcohol broken syrup bubble sight approve hover test"
# entropy="0111000011011010010011001110001111001010001100011010111111100011011100011011001101100111001001101111011110000111010011111110000000000100011111101111010111011111111001010010111100000110000000111001001101110010100011101010110010000010000101011001101110011110"
# fixed checkword = taxi

# find checksum params:
param_words="ignore sponsor decline nerve brain vast short hollow cheap rotate stadium scale elevator kit legend planet alcohol broken syrup bubble sight approve hover test"
print("calculate checksum -> ", bip39checksum.calculate_last_word(param_words))


# brute force problem "ignore sponsor decline nerve brain vast short hollow cheap rotate stadium scale elevator kit legend planet alcohol broken syrup bubble sight approve hover plastic"
# brute force item #1 (sponsor) to find checksum item #23 (plastic)
# fixed item #1 = adapt

param_words="ignore sponsor decline nerve brain vast short hollow cheap rotate stadium scale elevator kit legend planet alcohol broken syrup bubble sight approve hover plastic"
print("brute force word 1 for one result -> ", bip39checksum.brute_force(param_words, 1, 0))

# brute force all problem "ignore sponsor decline nerve brain vast short hollow cheap rotate stadium scale elevator kit legend planet alcohol broken syrup bubble sight approve hover plastic"
# brute force item #2 (decline) to find all checksum item #23 (plastic)
# fixed items for #2 = bring, bring, decade, include, season, smile, virus

param_words="ignore sponsor decline nerve brain vast short hollow cheap rotate stadium scale elevator kit legend planet alcohol broken syrup bubble sight approve hover plastic"
print("brute force word 2 for many result -> ", bip39checksum.brute_force(param_words, 2, -1))



# references :
# I have used for cross checking my results https://learnmeabitcoin.com/technical/mnemonic
# I have used for SHA256 computation logic. https://medium.com/bitbees/python-code-to-manually-create-12-24-worded-seed-and-passphrase-without-trusting-bitcoin-wallets-9d158535dfc6
# Directly used following three lines from the web page
# data = binascii.unhexlify(data)
# h = hashlib.sha256(data).hexdigest()
# b = bin(int(binascii.hexlify(data),16))[2:].zfill(len(data)*8) + bin(int(h,16))[2:].zfill(256)[: len(data)* 8//32]
