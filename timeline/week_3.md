# Day 1

- Today i created `VideoMediaSerializer` to represent the video path and the video quality

- created `ListVideosSerializer` and updated `GetVideoSerializer`

- Updated the `get_duration()` on `ResolutionParser` class

- Connect `VideoMediaSerializer` with `ListVideosSerializer`

- Write test cases for endpoints : 

    1.`Update Video`
    
    2.`Delete Video`


# Day 2

- Create endpoints in `videos` app :

    1. `Like Video By Id`
    2. `DisLike Video By Id`


- Write Test case for :
    1. `Like Video By Id`
    2. `DisLike Video By Id`

- Create custom permission `IsCommentOwner` in **globals/permissions.py**

- Create endpoints in `comment` app :

    1. `comment/get/{video_id}`
    2. `comment/create/{video_id}`
    2. `comment/delete/{comment_id}`
    3. `comment/update/{comment_id}`

# Day 3

- Write test cases for : 

    1. Get Comment
    2. Update Comment 
    3. Delete Comment
    4. Create Comment

- Solve issues on the comments endpoints 

- Add versioning for the endpoints


# Day 4

- Adding cache in `videos` app when : 

    1. new videos created
    2. videos deleted
    3. videos updated

- Adding cache in `comments` app when : 

    1. new comments created
    2. comments deleted
    3. comments updated

- Add `rate-limiting` on system

- Create custom permission `IsPlayListOwner` in **globals/permissions.py**

- create endpoints in `playlist` app :

    1. create playlist
    2. retrive playlist by id
    3. get owner playlists

# Day 5

- Create caching for playlist model

- Create endpoints : 

    1. add video to playlist
    2. remove video from playlist
    3. update playlist
    4. delete playlist

- Integerate permission `IsPlaylistOwner` into the endpoints

- create class `BaseQueryCache` in `globals/cache.py` for use it as a parent class and implement caching in the endpoints


# Day 6

- Use `BaseQueryCache` in : 
    
    1. `videos endpoints`
    2. `comment endpoints`
    3. `playlist endpoints`

- Test the whole system after adding `BaseQueryCache` and solve the issues that happens.

- Write test cases in app `playlist` for endpoints  :

    1. `create playlist`
    2. `update playlist`
    3. `delete playlist`
    4. `get playlist by id`
    5. `get playlist by owner`
    6. `add video via playlist`
    7. `remove video via playlist`

