# Defines base docker image.
# Pulls an official image, which includes Python, from Docker Hub Container Image Library.
FROM python:3.9-slim-buster

# Sets working directory in image.
# And uses this path as the default location for all subsequent commands.
WORKDIR /app

# Copies requirements.txt (from current directory) into working directory (/app) in image.
# . dot means current directory ( /app in image).
COPY requirements.txt .

# Pip installs packages from 'to image copied requirements.txt'.
RUN pip install -r requirements.txt

# Copies Python file(s) into working directory (/app) in image.
COPY rest_api.py .

# Runs following commands when docker image is executed (on start of docker container).
CMD [ "python", "./rest_api.py" ]

# ^^ that is entire dockerfile.
# To build docker image, run on console (in this directory, so use dot .):
# docker build .

# Show all docker images:
# docker images --all 
# or short:
# docker images -a

# To run docker image - by IMAGE ID (but if ports are used, see below):
# docker run 358b28865ffa
# ^^ if your image id is 358b28865ffa

# In this case, the Python app is a flask app that uses port 5000.
# Must expose port 5000 inside the container to port, e.g., 3000 outside the container.
# docker run --publish 3000:5000 358b28865ffa
# or short:
# docker run -p 3000:5000 358b28865ffa

# Note, flask will display "Running on", e.g.,http://172.17.0.2:5000/
# But has to use 127.0.0.1:3000 to access flask app from local machine
# or hosts IP address, e.g., 192.168.0.100:3000 to access flask in local network. 
# If no access in local network from non-host machine, possible solution:
# https://stackoverflow.com/questions/39111247/how-to-access-docker-container-from-another-machine-on-local-network

# Open console in docker container (running image):
# Docker desktop app >> have a running container >> CLI button ">_"
# and in the open console all Linux CLI commands work, e.g., have a look at directory structure:
# dir    cd ..