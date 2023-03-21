# download nginx image and copy index.html to /usr/share/nginx/html
FROM nginx:latest
COPY index.html /usr/share/nginx/html
