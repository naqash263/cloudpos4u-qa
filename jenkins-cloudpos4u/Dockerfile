FROM jenkins/jenkins:lts

USER root

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    chromium \
    chromium-driver \
    wget \
    unzip \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install JMeter
RUN wget https://archive.apache.org/dist/jmeter/binaries/apache-jmeter-5.6.3.zip \
    && unzip apache-jmeter-5.6.3.zip -d /opt \
    && rm apache-jmeter-5.6.3.zip \
    && ln -sf /opt/apache-jmeter-5.6.3/bin/jmeter /usr/local/bin/jmeter

# Install Allure CLI
RUN wget https://github.com/allure-framework/allure2/releases/download/2.29.0/allure-2.29.0.zip \
    && unzip allure-2.29.0.zip -d /opt \
    && rm allure-2.29.0.zip \
    && ln -sf /opt/allure-2.29.0/bin/allure /usr/local/bin/allure

USER jenkins