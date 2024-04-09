# Rotten Potatoes

Advanced Programming in Python – Final Project

Ideas: 
- Display 3 most recent reviews
- Display 3 favorites (user selects album) ? 
- artist attribute?

Pages: 
- home page
- profile page
- feed page showing friends ratings
- search page
- rating page 

## DB Schema

**Users:** userID, username, password

**UserFollowingRelationship:** relationshipID, _userAID_, _userBID_

&nbsp;&nbsp;&nbsp;&nbsp;FK: userAID -> Users
  
&nbsp;&nbsp;&nbsp;&nbsp;FK: userBID -> Users
  
**Albums:** albumID, albumName

**UserRatingRelationship:** relationshipID, _userID_, _albumID_, rating, review

&nbsp;&nbsp;&nbsp;&nbsp;FK: userID -> Users
  
&nbsp;&nbsp;&nbsp;&nbsp;FK: albumID -> Albums
  
**Songs:** songID, songName, _albumID_

&nbsp;&nbsp;&nbsp;&nbsp;FK: albumID -> Albums
  
**Artists:** artistID, artistName

**AlbumArtistRelationship:** relationshipID, _albumID_, _artistID_

&nbsp;&nbsp;&nbsp;&nbsp;FK: albumID -> Albums
  
&nbsp;&nbsp;&nbsp;&nbsp;FK: artistID -> Artists

## Er Diagram

![erdiagram][erdiagram.jpeg]
