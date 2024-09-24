## Pull from existing image
FROM pytorch/pytorch:1.8.0-cuda11.1-cudnn8-runtime

# New Work dir for MBAS
WORKDIR /hpc/fxu244/mbas24

## Copy requirements
COPY ./requirements.txt .

## Install Python packages in Docker image
RUN pip3 install -r requirements.txt

## Copy all files
COPY ./ ./

## Execute the inference command 
CMD ["./predict.py"]
ENTRYPOINT ["python3"]
