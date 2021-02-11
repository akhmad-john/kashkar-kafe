FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

ADD entrypoint.sh /
ENTRYPOINT ["/entrypoint.prod.sh"]
CMD [""]

RUN chmod +x entrypoint.prod.sh
