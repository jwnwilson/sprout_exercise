FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /src/

# Install Poetry
ENV PATH="/root/.local/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python - && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* /src/

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"
# Prophanity filter dependency
RUN python -m spacy download en

COPY . /src/
ENV PYTHONPATH=/src/

CMD "uvicorn main:app --host 0.0.0.0 --port 5001"