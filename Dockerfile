FROM public.ecr.aws/lambda/python:3.8


# COPY Folders
COPY artifacts ${LAMBDA_TASK_ROOT}/artifacts
COPY electricitymap ${LAMBDA_TASK_ROOT}/electricitymap

# Copy Files
#COPY requirements.txt ${LAMBDA_TASK_ROOT}

RUN pip install --no-cache-dir pip==23.1.2
RUN pip install --no-cache-dir setuptools==67.8.0
RUN pip install --no-cache-dir wheel==0.40.0
RUN pip install --no-cache-dir uvicorn
RUN pip install --no-cache-dir fastapi

# Install the specified packages
RUN pip install --no-cache-dir -r artifacts/model/requirements.txt

# Copy function code
COPY lambda_function.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function.handler" ]
