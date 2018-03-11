FROM tensorflow/tensorflow:1.4.1
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org -r requirements_docker.txt
RUN python -m nltk.downloader --dir=/usr/local/share/nltk_data perluniprops punkt
