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
