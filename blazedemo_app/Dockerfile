FROM blazemeter/selenium-framework

# create project folder with the name code
RUN mkdir /code

# project scope
WORKDIR /code

# install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Set Dokcer entry
RUN pwd
COPY ./docker-entry.sh /code
ENTRYPOINT ["/code/docker-entry.sh"]
