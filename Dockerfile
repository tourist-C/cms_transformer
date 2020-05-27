FROM python:3.6
RUN pip3 install -r requirements.txt
CMD ['python', 'cms_transformer.py']