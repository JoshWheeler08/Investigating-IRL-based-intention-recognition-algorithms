FROM nvcr.io/nvidia/pytorch:22.05-py3
 
ARG local_uid
ARG local_user

RUN adduser --uid ${local_uid} --gecos "" --disabled-password ${local_user}

WORKDIR /home/${local_user}

USER ${local_user}

ENV PATH="/home/${local_user}/.local/bin:${PATH}"

COPY requirements.txt ./

RUN pip install --user --upgrade pip

RUN pip install --user --no-cache-dir -r requirements.txt

