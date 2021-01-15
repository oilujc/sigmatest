FROM node:12.13.0-alpine AS alpine
RUN mkdir /front
COPY . /front
WORKDIR /front
ADD package.json /front/package.json
RUN npm install