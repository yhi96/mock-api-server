FROM library/debian:bookworm-slim
USER root

RUN mkdir -p /opt/project/upload
WORKDIR /opt/project

# COPY debian_packages.txt    /opt/project/debian_packages.txt
RUN apt-get update --allow-insecure-repositories && \
    # DEBIAN_FRONTEND=noninteractive xargs -a /opt/project/debian_packages.txt \
    apt-get install -y --allow-unauthenticated  \
        curl \
        iproute2 \
        iputils-ping \
        net-tools \
        python3 \
        python3-flask \
        python3-gunicorn \
        python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
    
    # rm -rf /opt/project/debian_packages.txt

# Unset because of https://github.com/psf/requests/issues/3829
ENV REQUESTS_CA_BUNDLE=

# Ignore warnings during requests calls
ENV PYTHONWARNINGS="ignore:Unverified HTTPS request"

ENV MOCK_HOSTNAME=api-mock-server

COPY rsa-cert-generation/create_certs.sh            /root/ca/rsa/create_certs.sh
COPY rsa-cert-generation/root-openssl.conf          /root/ca/rsa/openssl.cnf
COPY rsa-cert-generation/intermediate-openssl.conf  /root/ca/rsa/intermediate/openssl.cnf

COPY app  /opt/project/
COPY bin  /opt/project/

RUN chmod +x /root/ca/rsa/create_certs.sh
RUN chmod +x /opt/project/start.sh

ENTRYPOINT ["/opt/project/start.sh"]