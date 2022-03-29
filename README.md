# Tech-Challenge
Summary: 
    The web page is to encrypt and decrypt messages. There are two textboxes one to encrypt a message and one to decrypt a message. The user will type a word or group of letters in the encrypted textbox and press the encrypt button. Once the user clicks the encrypt button, it will move each letter in the textbox five spots to the right in the alphabet. To decrypt a message, the user will put a word or group of letters in the decrypt textbox. When the user clicks the decrypt button, it will move each letter five spots to the left in the alphabet. If the user encrypted the word "happyclouds," the word will come out to mfuudhqtzix. If the user decrypts the letters "mfuudhqtzix," the word happyclouds would be presented. 

How to Build:  
	There are two directories called "Nginx" and "app."  The app directory has two files called app.py and encryptme.py. Inside the Nginx directory are the ssl certificates, Dockerfile, index.html, and nginx.conf. A docker-compose file on the same level Nginx directory and app directory. In your terminal on your laptop, go to the directory where you stored the files. You should be able to type docker-compose up -d --build. This command runs the application in the background in the docker container. Both web pages should be up and running in the Docker container. The user can type https://localhost:443 to access the web page with the encrypt and decrypt functions. In a new window, the user can type localhost:5000 to access the flask web page saying "Hello from flask." The user can have multiple containers in one docker. They can decide which one they want to have up running or have both running simultaneously.  

How to Cleanup: 
	If you have docker desktop installed, we can access the docker container within the docker desktop. We can turn off the docker container in the docker desktop or the terminal with the command "docker-compose down." If you make changes to the application, it's good practice to "docker-compose down" and then "docker-compose up -d --build." If you type "docker-compose up," it will not run in the background. Then you will have to press CTRL + C, which will stop the docker container and allow you to type "docker-compose up -d --build."