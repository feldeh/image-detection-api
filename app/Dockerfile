FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY next.config.js ./next.config.js
