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
**UserFollowingRelationship:** relationshipID, _userA_ID_, _userB_ID_
  FK: userA_ID -> Users
  FK: userB_ID -> Users
**Albums:** albumID, albumName
**UserRatingRelationship:** relationshipID, _userID_, _albumID_, rating, review
  FK: userID -> Users
  FK: albumID -> Albums
**Songs:** songID, songName, _albumID_
  FK: albumID -> Albums
**Artists:** artistID, artistName
**AlbumArtistRelationship:** relationshipID, _albumID_, _artistID_
  FK: albumID -> Albums
  FK: artistID -> Artists
