# Retinal-OCT-classification-and-segmentation

In this project, we made a system to classify scans as normal, pachychoroid, drusen, or diabetic macular edema (DME). If a scan is labeled as DME, we identify the affected area to assist ophthalmologists who have to analyze many scans each day.
For classification, we improved a model we found in our research. It's a 15-layer CNN model, a better version of the VGG16 transfer learning model. We made two main changes: using depthwise separable convolutional layers instead of regular ones and using ELU instead of ReLU activation function. Our custom model trains much faster and is more accurate. The accuracy acheived by the custom model is around 98.35% outperforming all the existing models.
For segmentation, we prepared the scans first by finding valid indexes and enhancing contrast and reducing noise. We used Non-local Means Denoising for noise removal and Contrast Limited Adaptive Histogram Equalization (CLAHE) to enhance contrast. Then we resized the images and split them into training and testing sets.
For segmentation, we simply thresholded the image masks and resized them. Then we trained a U-Net model to predict the masks.

After this, deployed the model on AWS EC2 (Elastic Cloud Compute) using Flask. 
Made a website using Flask then deployed it on AWS EC2 using the following commands.

1. Open Powershell and go to the folder containing the project zip file.
2. Execute the following cmd -> scp -i ssh_key.pem pythonProject.zip ubuntu@ec2-18-191-25-39.us-east-2.compute.amazonaws.com:
3. Next, send your files to the server by executing the following command -> ssh -i "ssh_key.pem" ubuntu@ec2-18-191-25-39.us-east-2.compute.amazonaws.com
4. Execute the following commands to get files on the server provided by the EC2 instance 
  - dir
  - sudo apt install zip unzip
  - unzip pythonProject.zip
  - cd pythonProject
5. Setup the environment by installing all dependencies using the commands below
  - sudo apt-get update
  - sudo apt-get install -y python3-pip
  - downgrade python to 3.11 (https://askubuntu.com/questions/682869/how-do-i-install-a-different-python-version-using-apt-get)
  - pip3 install -r requirements.txt
6. Run the script by executing python3 app.py command
7. Connect to the EC2 instance by running the public DNS ended with :8080/ (Ex - http://ec2-18-191-25-39.us-east-2.compute.amazonaws.com:5000/)

Steps to deploy on AWS ECS using EC2 launch type/ instance
1. Install docker on Ubuntu:  sudo apt update, sudo apt install docker.io
2. Verify the installation: docker --version
3. Start docker: sudo systemctl enable docker, sudo systemctl start docker
4. Verify if the docker is running: sudo systemctl status docker
5. Create docker image: vim Dockerfile, press i to insert, once edited, press esc to come to normal mode, save and exit by typing :wq!
6. Then build image and containerize your web application: sudo docker build -t retinaloct-image . -> sudo docker run -d -p 8080:8080 --name project-container retinaloct-image -> sudo docker ps -> sudo docker run -p 8080:8080 retinaloct-image
7. Create ECR repository
8. Create IAM role with the AdministratorAccess for the EC2 service/ use-case
9. Create IAM > Users > User with policy AmazonEC2ContainerRegistryFullAccess
10. Create an access key in AWS IAM and use that to configure the user profile via the AWS CLI in Amazon Linux/ Ubuntu. To create access key go to IAM> Users> Security Credentials > Create access key
11. To install AWS CLI in the ubuntu machine of EC2 instance
    - curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    - unzip awscliv2.zip
    - sudo ./aws/install
    - aws --version
12. Then run aws configure in terminal to configure user profile
13. 

References 
- https://medium.com/analytics-vidhya/ml-model-deployment-with-flask-using-aws-ec2-part-ii-38ca941e0c4b
- https://www.youtube.com/watch?v=_rwNTY5Mn40&t=1715s
