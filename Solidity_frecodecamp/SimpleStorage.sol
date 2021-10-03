
pragma solidity ^0.6.0;

contract SimpleStorage {
    
    //COMMENT
    uint256 favoriteNumber = 5; //That's a view function too
    bool favoriteBool;
    
    struct People {
        uint256 favoriteNumber;
        string name;
    }
    
    People public person = People({favoriteNumber: 2, name: "Nicolás"});
    People[] public people;
    mapping(string => uint256) public nameToFavoriteNumber;
    
    function store(uint256 _favoriteNumber) public{
        favoriteNumber = _favoriteNumber;
    }
    
    //view => we are just reading off the blockchain -> no transaction fee !!!
    //pure => kinda da same idea
    function retrievedouble() public view returns(uint256){
        return favoriteNumber + favoriteNumber;
    }
    
    function addPerson(string memory _name, uint256 _favoriteNumber) public{
        people.push(People({favoriteNumber: _favoriteNumber, name: _name}));
        nameToFavoriteNumber[_name] = _favoriteNumber;
            
    }

    
    
    
    
    
    
}