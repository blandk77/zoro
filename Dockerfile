FROM mysterysd/wzmlx:latest

WORKDIR /usr/src/app

RUN chmod 777 /usr/src/app

COPY . .

RUN python3 -m pip install --no-cache-dir -r requirements.txt

RUN chmod +x start.sh

CMD ["bash", "start.sh"]
