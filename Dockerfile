#==============×==============#
#    Created by: PunyaAlby
#=======× ALBY-Userbot ×======#

FROM punyaalby/alby-userbot:buster

RUN git clone -b ALBY-Userbot https://github.com/bitchlah/zxz /home/albyuserbot/ \
    && chmod 777 /home/albyuserbot \
    && mkdir /home/albyuserbot/bin/

COPY ./sample_config.env ./config.env* /home/albyuserbot/

WORKDIR /home/albyuserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
