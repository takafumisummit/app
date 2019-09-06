FROM python:3.6

COPY ./application /application

ARG project_dir=/application/

WORKDIR $project_dir

RUN pip install -r requirements.txt
