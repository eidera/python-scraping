FROM ubuntu:17.04

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get update && \
    apt-get install -y curl wget unzip git gcc make openssl libssl-dev libbz2-dev libreadline-dev gconf-service libasound2 libgconf-2-4 libnspr4 libxss1 libnss3 lsb-release xdg-utils libappindicator1 fonts-liberation

RUN git clone git://github.com/pyenv/pyenv.git ~/.pyenv

RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc && \
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc && \
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc && \
    source ~/.bashrc

RUN ~/.pyenv/bin/pyenv install 3.6.1 && \
    ~/.pyenv/bin/pyenv rehash && \
    ~/.pyenv/bin/pyenv global 3.6.1

RUN ~/.pyenv/shims/pip install PyMySQL sqlsoup pyyaml selenium beautifulsoup4 html5lib

RUN mkdir -p /tmp/font && \
    cd /tmp/font && \

    wget --content-disposition http://ipafont.ipa.go.jp/old/ipafont/IPAfont00303.php && \
    unzip IPAfont00303.zip -d /usr/share/fonts/ && \
    fc-cache -fv && \

    cd && \
    rm -rf /tmp/font

# Install of headless chrome
RUN mkdir -p /tmp/chrome && \
    cd /tmp/chrome && \

    # Don't add google repository
    touch /etc/default/google-chrome && \

    curl -O https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb && \

    cd && \
    rm -rf /tmp/chrome

# Install of chrome driver(after Ver. 2.31)
RUN mkdir -p /tmp/chrome && \
    cd /tmp/chrome && \

    curl -O https://chromedriver.storage.googleapis.com/2.31/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    chmod +x chromedriver && \
    mv -f chromedriver /usr/local/share/chromedriver && \
    ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver && \
    ln -s /usr/local/share/chromedriver /usr/bin/chromedriver && \

    cd && \
    rm -rf /tmp/chrome

# For debug
RUN ~/.pyenv/shims/pip install ipython

RUN mkdir -p /app
WORKDIR /app
