from PySide6.QtWidgets import QApplication
from SmartContract import ContractCreator, ContractMetaData
from UserInterface import MainWindow
from web3 import Web3
import sys
import json
import glob


class DesktopClient:
    def __init__(self):
        # connect to ganache
        self.w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

        # deploy the contract or get the most recent version of the contract
        self.configure()

        # call this last!
        self.create_gui()

    def create_gui(self):
        # login screen
        num_wallets = len(glob.glob("Wallets/*_wallet.json"))
        if num_wallets == 0:
            print("wallet not found")
            print("creating account")
            self.account = self.w3.eth.account.create()

        if num_wallets > 1:
            print("more than one wallet found")

        wallet_exists = num_wallets == 1

        self.app = QApplication([])
        self.window = MainWindow(self.create_account,
                                 self.login, wallet_exists,
                                 self.account.address,
                                 self.copy_to_clipboard,
                                 self.contract.functions.getAccounts().call(),
                                 self.contract.functions.addAccount(bytes("1234123412341234", encoding='utf8'),
                                                                    bytes("aaaaaaaaaaaaaaaa", encoding='utf8'))
                                                                    .estimateGas())
        self.window.show()
        sys.exit(self.app.exec_())

    def copy_to_clipboard(self, text):
        self.app.clipboard().setText(text)

    def login(self):
        self.username = self.window.login_username()
        self.password = self.window.login_password()

        if len(self.username) == 0:
            print("please enter a username")
            return False
        if len(self.password) == 0:
            print("please enter a password")
            return False

        try:
            with open("Wallets/" + self.username + "_wallet.json") as wallet_file:
                wallet = json.load(wallet_file)
                try:
                    self.account = self.w3.eth.account.decrypt(wallet, self.password)
                    self.private_key = self.w3.toHex(self.account)
                    self.public_key = self.w3.toChecksumAddress("0x" + wallet['address'])
                    return True
                except:
                    print("invalid password")
                    return False
        except:
            print("error opening file")
            return False

    def create_account(self):
        if self.window.create_account_username() == "":
            print("username cannot be blank")
            return

        if self.window.create_account_password() == "":
            print("password cannot be blank")
            return

        if self.username_exists(self.window.create_account_username()):
            print("username already exists!")
            return

        if self.window.create_account_password() != self.window.create_account_confirm_password():
            print("passwords do not match!")
            return

        self.username = self.window.create_account_username()
        self.password = self.window.create_account_password()

        self.wallet_file_name = self.username + '_wallet.json'
        with open("Wallets/" + self.wallet_file_name, 'w') as json_file:
            wallet = self.account.encrypt(self.password)
            json.dump(wallet, json_file)


    def username_exists(self, username: str):
        print(self.contract.functions.getAddress(username).call())
        return "0x0000000000000000000000000000000000000000" != self.contract.functions.getAddress(username).call()

    def configure(self):
        if "-d" in sys.argv:
            file_path = "SmartContract/Metallic.sol"
            file_name = "Metallic.sol"
            contract_name = "Metallic"
            self.contract, self.abi = ContractCreator.compile_and_deploy_contract(file_path, file_name, contract_name, self.w3)
            print(self.contract.functions.helloWorld().call())
        else:
            # connect to an existing contract
            self.abi = ContractMetaData.abi
            self.address = ContractMetaData.address
            self.contract = self.w3.eth.contract(address=self.address, abi=self.abi)
            print("did not deploy, message:", self.contract.functions.helloWorld().call())


DesktopClient()
