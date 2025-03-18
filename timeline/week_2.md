# Day 1

Today I init `users` apps and create custom user model with 
it's fields which is on this [diagrams](https://drawsql.app/teams/test-1748/diagrams/youtube)

> NOTE: Not all fields has been created

Then i use my package `socail_auth` to login via google using it.

# Day 2

- Changes in `users` app : 
   
    1. create profile serializer
    2. create profile endpoint
    3. write test file for users app


- Then i added `JWT configuration` on the system


- Init `videos` app
- create `Video` schema depends on the diagram which i written

- created `globals` app for use it as a base app for other apps


# Day 3

- Created 2 apps : 

    1. `hasgtag`
    2. `comment`

- created 2 models : 

    1. `Comment`
    2. `Hashtag`

- re-edit on User model and add these fields : 
    
    - user_hashtags
    - user_liked_videos
    - user_history


# Day 4

- Done writing these endpoints : 
    1. `video/get/` -> get list of all videos
    2. `video/get/{id}` -> get video by id
    2. `video/delete/{id}` -> delete video by id
    2. `video/update/{id}` -> update video by id

- Create custom permission `IsVideoOwner` for checking if the request action is accured by the owner of the video

- Create `playlist` app and `PlayList` model inside this app.

- create custom functions to get the user timeline in `globals/filter_videos` : 

    1. `anonymus_filtering` -> filter videos for anonymous user

    2. `user_filtering(user)` -> filter videos for incoming user request
