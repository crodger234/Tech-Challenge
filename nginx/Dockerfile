FROM nginx:latest
COPY ssl/certs/nginx-selfsigned.crt /etc/nginx/certs/nginx-selfsigned.crt
COPY ssl/certs/nginx-selfsigned.key /etc/nginx/certs/nginx-selfsigned.key
COPY nginx.conf /tmp/secure-site.conf
COPY index.html /etc/nginx/html/index.html
EXPOSE 443
