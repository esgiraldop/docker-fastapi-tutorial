# docker-fastapi-tutorial
docker-fastapi-tutorial


Tutorial from --> https://www.youtube.com/watch?v=iqrS7Q174Ac

Hugging face model --> https://huggingface.co/dandelin/vilt-b32-finetuned-vqa

Commands to install the rust compiler in Docker (To be placed in the Dockerfile)

RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}" //Setting rust compiler as env variable