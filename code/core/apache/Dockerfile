# Use the official Apache image
FROM httpd:2.4

# Copy the Apache configuration file
COPY 000-default.conf /usr/local/apache2/conf/extra/000-default.conf

# Enable required modules
RUN echo "LoadModule proxy_module modules/mod_proxy.so" >> /usr/local/apache2/conf/httpd.conf && \
    echo "LoadModule proxy_http_module modules/mod_proxy_http.so" >> /usr/local/apache2/conf/httpd.conf && \
    echo "LoadModule proxy_balancer_module modules/mod_proxy_balancer.so" >> /usr/local/apache2/conf/httpd.conf && \
    echo "LoadModule lbmethod_byrequests_module modules/mod_lbmethod_byrequests.so" >> /usr/local/apache2/conf/httpd.conf && \
    echo "LoadModule slotmem_shm_module modules/mod_slotmem_shm.so" >> /usr/local/apache2/conf/httpd.conf && \
    echo "Include conf/extra/000-default.conf" >> /usr/local/apache2/conf/httpd.conf

# Expose port 80
EXPOSE 80