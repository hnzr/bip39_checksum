# bip39_checksum

bip39_checksum is a Python code developed for understanding how bip39 mnemonic codes designed.

Checksum calculation is the first part of the code.

On top of checksum calculation added the functionality for finding any missing word if checksum is given.

## Usage
You can generate random 24 words with dice rolls using instructions on the link. Then fix the last word with calculation using bip39_checksum. If you are planning to use it with real seed phrase generation use an OFFLINE computer to execute the code. You can copy it with USB stick as you will not be connected.

[https://en.bitcoin.se/articles/create-your-own-wallet-seed-using-regular-dice](https://en.bitcoin.se/articles/create-your-own-wallet-seed-using-regular-dice)


You can find usage example in main.py file.

```python
import bip39checksum

# find last word for any given 24 word seed phrase :
param_words="ignore sponsor decline nerve brain vast short hollow cheap rotate stadium scale elevator kit legend planet alcohol broken syrup bubble sight approve hover test"
calculate checksum = bip39checksum.calculate_last_word(param_words))

# brute force item #1 (sponsor) to find checksum item #23 (plastic)
param_words="ignore sponsor decline nerve brain vast short hollow cheap rotate stadium scale elevator kit legend planet alcohol broken syrup bubble sight approve hover plastic"
print("brute force word 1 for one result -> ", bip39checksum.brute_force(param_words, 1, 0))


```

## Contributing
Pull requests are always welcome. ;)

## License
[MIT](https://choosealicense.com/licenses/mit/)
