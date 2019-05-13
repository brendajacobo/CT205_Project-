# CST 205 Team 5 Repository
## Description
Our project is a Spotify song suggestor which will analyze whether you look happy or sad and recommend appropriate songs to you. 
## Challenges
The biggest challenge our app faced was how fragmented it was. We have a flask application which needs to "listen" to a face detection app. 
This was a major issue because of a few things:
- Webpages usually only load once, so trying to get data from a dynamically changing webcam image is difficult.
- Our one application needs to basically run two apps together. This was hard mostly because the face detection app needs an infinite loop to continuously analyze the image. 
-- To combat this we utilized threads, so the web server runs in the main thread and it spawns another thread which is running the face detection in the background. 
## Running the app
- Clone the master branch of this repository.
- Retrieve the key information for your Spotify API application and put it in a file called `conf.json`
- Launch the app using `python app.py` from the `/spotify` directory.

