# Get the script to install docker
curl -fsSL https://get.docker.com -o get-docker.sh

# See the docker file
ls -l get-docker.sh

# Install the script with docker
sudo sh get-docker.sh

sudo docker run --rm -it python:3
