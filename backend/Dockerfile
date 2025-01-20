FROM continuumio/miniconda3

WORKDIR /host_files

COPY . /host_files/

RUN apt-get update

RUN apt-get install curl -y

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

ENV PATH="/root/.cargo/bin:${PATH}"

RUN apt install build-essential -y

RUN conda env create -f environment.yml

RUN conda init bash

CMD /bin/bash -c "source ~/.bashrc && conda activate nw-plate && python main.py"
