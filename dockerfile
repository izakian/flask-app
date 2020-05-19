
# alpine is a light vesrion of docker
FROM alpine:latest

# install python3 and pip3
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

# build a working directory for docker containers
WORKDIR /app

# copy current working directory to /app directory
COPY . /app

# install all the packages from requirements.txt
RUN pip3 --no-cache-dir install -r requirements.txt

# expose a port
EXPOSE 5000

# tell the container what to do when started
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]

