FROM python
COPY . /opt/app
WORKDIR /opt/app
# RUN pip install requests
# RUN pip install Flask
# RUN pip install selenium
# RUN pip install webdriver-manager

#RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#EXPOSE 8777
CMD ["python","MainGame.py"]
CMD ["python","MainScores.py"]