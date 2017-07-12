FROM blazemeter/selenium-framework

WORKDIR /code_directory
COPY requirements.txt .

RUN pip install -r requirements.txt
COPY . /code_directory

CMD ["tests/test_purchase_tickets.py"]