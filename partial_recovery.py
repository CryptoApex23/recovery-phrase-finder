import itertools
from mnemonic import Mnemonic
from eth_account import Account
from tqdm import tqdm
from web3 import Web3

def print_logo():
    logo = r"""
  ______   _______   __      __  _______   ________  ______  
 /      \ /       \ /  \    /  |/       \ /        |/      \ 
/$$$$$$  |$$$$$$$  |$$  \  /$$/ $$$$$$$  |$$$$$$$$//$$$$$$  |
$$ |  $$/ $$ |__$$ | $$  \/$$/  $$ |__$$ |   $$ |  $$ |  $$ |
$$ |      $$    $$<   $$  $$/   $$    $$/    $$ |  $$ |  $$ |
$$ |   __ $$$$$$$  |   $$$$/    $$$$$$$/     $$ |  $$ |  $$ |
$$ \__/  |$$ |  $$ |    $$ |    $$ |         $$ |  $$ \__$$ |
$$    $$/ $$ |  $$ |    $$ |    $$ |         $$ |  $$    $$/ 
 $$$$$$/  $$/   $$/     $$/     $$/          $$/    $$$$$$/                                                
  ______   _______   ________  __    __                      
 /      \ /       \ /        |/  |  /  |                     
/$$$$$$  |$$$$$$$  |$$$$$$$$/ $$ |  $$ |                     
$$ |__$$ |$$ |__$$ |$$ |__    $$  \/$$/                      
$$    $$ |$$    $$/ $$    |    $$  $$<                       
$$$$$$$$ |$$$$$$$/  $$$$$/      $$$$  \                      
$$ |  $$ |$$ |      $$ |_____  $$ /$$  |                     
$$ |  $$ |$$ |      $$       |$$ |  $$ |                     
$$/   $$/ $$/       $$$$$$$$/ $$/   $$/

###############################
#                             #
#        CryptoAppex          #
# ETH Partial Mnemonic Phrase #
# Recovery Tool               #
# V0.1                        #
###############################
    """
    print(logo)


Account.enable_unaudited_hdwallet_features()
wordlist_file = "wordlist.txt"
def load_wordlist(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

def generate_mnemonic_combinations(partial_mnemonic, wordlist):
    slots = partial_mnemonic.count('x')
    combinations = itertools.product(wordlist, repeat=slots)

    for combo in combinations:
        mnemonic = partial_mnemonic
        for word in combo:
            mnemonic = mnemonic.replace('x', word, 1)
        yield mnemonic

def get_eth_address_from_mnemonic(mnemonic):
    account = Account.from_mnemonic(mnemonic)
    return account.address


def find_correct_mnemonic(partial_mnemonic, target_address, wordlist):
    mnemo = Mnemonic("english")
    total_combinations = len(wordlist) ** partial_mnemonic.count('x')

    with tqdm(total=total_combinations, desc="Processing", unit="mnemonic") as pbar:
        for mnemonic in generate_mnemonic_combinations(partial_mnemonic, wordlist):
            pbar.update(1)
            try:
                if not mnemo.check(mnemonic):
                    continue
                if get_eth_address_from_mnemonic(mnemonic) == target_address:
                    write_result_to_file(mnemonic, target_address)
                    return mnemonic
            except:
                continue
    return None    

def validate_mnemonic(phrase):
    words = phrase.split()
    return len(words) == 12


def is_valid_ethereum_address(address):
    return Web3.is_address(address)

def write_result_to_file(mnemonic, address, filename="Result.txt"):
    with open(filename, "w") as file:
        file.write("Recovered Mnemonic Phrase:\n")
        file.write(f"{mnemonic}\n\n")
        file.write("Associated Ethereum Address:\n")
        file.write(f"{address}\n")
    print(f"Results have been written to {filename}")
    

def main():
    print_logo()

    while True:
        # Get user inputs
        partial_mnemonic = input("What is the mnemonic phrase (put 'x' where you are missing a word)?\n")
        
        # Validate mnemonic
        if not validate_mnemonic(partial_mnemonic):
            print("Invalid mnemonic phrase. It must be 12 words with 'x' placeholders for missing words.")
            continue
        
        target_address = input("What is the target wallet address?\n")

        # Validate Ethereum address
        if not is_valid_ethereum_address(target_address):
            print("Invalid Ethereum address.")
            continue
        
        # Load wordlist
        wordlist_file = "wordlist.txt"
        wordlist = load_wordlist(wordlist_file)

        # Find the correct mnemonic
        correct_mnemonic = find_correct_mnemonic(partial_mnemonic, target_address, wordlist)

        if correct_mnemonic:
            print("Found correct mnemonic:", correct_mnemonic)
        else:
            print("No matching mnemonic found.")
        break


if __name__ == "__main__":
    main()
