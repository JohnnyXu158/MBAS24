# Instructions for the submission of MBAS2024

## Instructions for Validation Phase Submission

During the validation phase, competitors are required to submit mask predictions (*.nii.gz). We require zipped submissions for both tasks to the submission page.

Validation Phase

During the validation phase, competitors are required to submit mask predictions (.nii.gz). The submission should be zipped as the following structure: 

── teamname_ValPhase_Try1.zip (Note that: total 3 times for validation from Try1 to Try3)

    ├── MBAS_071_label.nii.gz
    
    └── MBAS_072_label.nii.gz
    
    ├── ...
    
    └── MBAS_100_label.nii.gz

It is of note that your submission should not contain any folders or unrelated files. The file id of prediction masks must be as same as that of the original validation MRI scans (e.g., MBAS_071_label.nii.gz). 

 

## Instructions for Test Phase Submission

The MBAS2024 challenge will be held as a Type II challenge that will not release the test set to its competitors. For the test phase submission, we will require the competitors to submit their containerized docker images. 

## NOTE THAT: Please see [Tutorial-PDF](https://github.com/JohnnyXu158/MBAS24/blob/main/Submission/MBAS24-HowToSubmit.pdf) for more latest information!

<!--
### Step 1. Organize an inference script

We require a script file that automatically performs inference on the test set, i.e., outputting the predicted segmentation masks on the test set.

For task 1, we require that the input folder be mounted into *input* and the output folder be *output*. In addition, the output files should have the same file name as the input, e.g. the input file input/MBAS_001_gt.nii.gz must have a matched output prediction named output/MBAS_001_label.nii.gz. An example of the inference script can be found [here](./DockerSample/predict.py).

Please note that following our [sample](./DockerSample/save_pths), each team must submit two parameter files such as ABC_val.pth and ABC_test.pth, saved under the "save_pths" directory. Additionally, the `predict.py` script should be able to accept several parameters, including the input path, output path, and parameters path.




### Step 2. Containerize the application using Docker

We require the competitors to use [Docker] to containerize their applications. Docker images can be created using Dockerfiles, which contain all commands that help to run applications. An example of a Dockerfile can be found [here](./DockerSample/Dockerfile). Four basic components are required to be included in the Docker file:

1. Pulling a pre-existing image with an operating system and, if needed, CUDA (FROM instruction).
2. Installing additional dependencies (RUN instructions).
3. Transferring local files into your Docker image (COPY instructions).
4. Executing your algorithm (CMD  and ENTRYPOINT instructions).

After finishing the Dockerfile, you can build your Docker image with:
docker build -f Dockerfile -t [**teamname**].


### Step 3. Docker running commands

Your container will be run with the following command:

```
docker run --rm -v [input directory]:/input -v [output directory]:/output -it [teamname]

or

singularity exec --pwd /workspace --bind [input directory]:/input --bind [output directory]:/output [teamname].sif python3 /workspace/predict.py --model_pth './save_pths/ABC_test.pth'

```

[input directory] will be the absolute path of our directory containing the test set, [output directory] will be the absolute path of the prediction directory.

### Step 4. Docker container submission

Before submission, please upload the built Docker images to DockerHub.

Then, send the name of the Docker image and the complete code in a zip file (excluding the pth files, as they are already included in the Docker image) to our mbas24miccai@gmail.com. 

For all teams, we will re-evaluate the results of the validation set to ensure the fairness of the final ranking.



**Submission Example:**

Titile: Final Test for MBAS 2024

Contents:

Hi MBAS Committee,

Here is our docker image name: mbas24miccai/example

And the docker link is: https://hub.docker.com/repository/docker/mbas24miccai/example

See the attached file for the completed code.


teamname_code.zip

 ├── data_processing.py
 
 ├── train.py
 
 ├── test.py
 
 ├── predict.py
 
 ├── networks
 
  ├── ABC.Net
  
 ├── loss.py
 
 ├── readme.md    # explain how to process data, train and test.
  

Thanks,

Team ABC
-->

## References

This tutorial and the examples contained are based on [CrossModa](https://crossmoda.grand-challenge.org/submission/).
