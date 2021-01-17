// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.8.0;
pragma experimental ABIEncoderV2;

contract UsernameDatabase {
    struct UserAccount {
        string username;
        string public_name;
        address public_address;
    }

    UserAccount[] listOfAccounts;
    mapping (string => UserAccount) private accounts;

    constructor() {}

    function getAccounts() public view returns (UserAccount[] memory){ return listOfAccounts; }

    function _addAccount(string memory username, 
                        string memory public_name) internal virtual {
        require (bytes(username).length != 0, "Username cannot be empty");
        require (bytes(public_name).length != 0, "Public Name cannot be empty");

        UserAccount memory user = accounts[username];
        bool usernameExists = user.public_address != address(0x0000000000000000000000000000000000000000);

        require (!usernameExists, "Username already exists.");

        UserAccount memory newUser = UserAccount(username, public_name, msg.sender);
        accounts[username] = newUser;
        listOfAccounts.push(newUser);
    }

    function getAddress(string memory username) public view returns (address) {
        UserAccount memory user = accounts[username];
        return user.public_address;
    }
}

contract Metallic is UsernameDatabase{
    function substring(string memory str, uint startIndex, uint endIndex) internal pure returns (string memory) {
        bytes memory strBytes = bytes(str);
        bytes memory result = new bytes(endIndex-startIndex);
        for(uint i = startIndex; i < endIndex; i++) {
            result[i-startIndex] = strBytes[i];
        }
        return string(result);
    }

    function helloWorld() public pure returns (string memory) {
        return "Hello World";
    }

    function addAccount(string memory username, string memory public_name) public {
        require(bytes(username).length <= 32, "Usernames must be 32 characters or less.");
        require(bytes(username).length >= 1, "Usernames must be at least one character");
        require(bytes(public_name).length <= 32, "Public Name must be 32 characters or less.");
        require(bytes(public_name).length > 1, "Public Name must be at least one character");

        bool isValidUsername = true;
        for (uint i = 0; i < bytes(username).length; i++ ){
            bytes1 char = bytes(substring(username, i, i+1))[0];
            if (!(char >= 0x30 && char <= 0x39) //digits
                && !((char >= 0x41 && char <= 0x5A) || (char >= 0x61 && char <= 0x7A)) //letters
                && !(char == 0x5F)){ //underscore
                isValidUsername = false;
                break;
            }
        }
        require(isValidUsername, "Username invalid");

        bool isValidPublicName = true;
        for (uint i = 0; i < bytes(public_name).length; i++) {
            bytes1 char = bytes(substring(public_name, i, i+1))[0];
            if (!((char >= 0x41 && char <= 0x5A) || (char >= 0x61 && char <= 0x7A))  // letters
                || !(char == 0x20)){ // space char
                isValidPublicName = false;
                break;
            }
        }
        require(isValidPublicName, "Currency invalid");
        super._addAccount(username, public_name);
    }
}
