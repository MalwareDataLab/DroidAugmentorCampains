FROM  ubuntu:22.04
WORKDIR /DroidAugmentor

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    unzip \
    && rm -rf /var/lib/apt/lists/*

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN pip3 install pipenv
RUN pip install urllib3

COPY ./ /DroidAugmentor/

RUN pip3 install -r requirements.txt

RUN chmod +x /DroidAugmentor/shared/app_run.sh
CMD ["/DroidAugmentor/shared/app_run.sh"]



