FROM public.ecr.aws/lambda/python:3.8

# Install any additional dependencies if required
RUN pip install numpy

# Copy the Lambda function code
COPY app.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (function n