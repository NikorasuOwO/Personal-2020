
pragma solidity ^0.6.0;

import "./SimpleStorage.sol";

contract StorageFactory is SimpleStorage{ //INHERITANCE!!
    
    SimpleStorage[] public SimpleStorageArray;
    
    function createSimpleStorageContract() public {
        
        SimpleStorage ss = new SimpleStorage();
        SimpleStorageArray.push(ss);
    }
    
    function sfStore(uint256 _simpleStorageIndex, uint256 _simpleStorageNumber) public {
        // to interact with a contract we need: address and ABI
        
        SimpleStorage simpleStorage = SimpleStorage(address(SimpleStorageArray[_simpleStorageIndex])); //We get the contract
        simpleStorage.store(_simpleStorageNumber);
    }
    
    function sfGet(uint256 _simpleStorageIndex) public view returns (uint256){
        address add = address(SimpleStorageArray[_simpleStorageIndex]);
        return SimpleStorage(add).retrieve();
    }
    
}
