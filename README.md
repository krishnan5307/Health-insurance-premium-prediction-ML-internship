# Health-insurance-premium-prediction-ML-internship



The goal of this project is to give people an estimate of how much they need based on their individual health situation. After that, customers can work with any health insurance carrier and its plans and perks while keeping the projected cost from our study in mind.

**Screenshots**: 

uploading the data from link to cassandra database for later to be pulled from the DB during training the model
https://www.kaggle.com/datasets/noordeen/insurance-premium-prediction

![image](https://user-images.githubusercontent.com/69358581/216957674-75b77441-5436-49e5-8b05-2b2fbe5d24c0.png)


Technical Aspect
The project was built in two phases and the process is as follows:

Process Phase:-->

Importing Libraries-
Loading Dataset-
Performing Data Analysis-
Feature Engineering-
Data Pre-processing-
Model Selection-
Model Trainig-
Model Evalution-
Model Saving-
Deployment Phase:

Run the application built using flask webframework :--->

Load Model-
Render HTML frontend-
Receive Input-
Data Preprocessing-
Prediction-
Display Results.



1.a) Training the model:

![image](https://user-images.githubusercontent.com/69358581/211560642-00a219f2-3fcb-4db3-b689-7c2d20d649d7.png)


  b) Retraining model with more ensemble-boosting algorithms such as Adaboost and Gradient boosting to improve accuracy of the model
  
  ![image](https://user-images.githubusercontent.com/69358581/211629081-ae13ffdc-e722-4838-aa70-e4be328fa8ad.png)





2.Premium Prediction for user data:

![image](https://user-images.githubusercontent.com/69358581/211561173-5d26c0fc-6fdb-46f5-8966-2a6ff9df8d9f.png)



3.Data drift report using Evidently DataDriftProfileSection framework
![image](https://user-images.githubusercontent.com/69358581/211611436-47c05d19-1a6b-4634-a5b5-4a72e9b518e4.png)


4.CICD deployment to AWS-ECR-EC2
![image](https://user-images.githubusercontent.com/69358581/216830773-b8cc24ce-4ecb-4355-b45d-90061ee6bd74.png)


5.Image uploaded in AWS ECR-repo
![image](https://user-images.githubusercontent.com/69358581/216830819-b30783e1-8845-4b56-9467-46e024a9b25b.png)


6.Code in Vscode.
![image](https://user-images.githubusercontent.com/69358581/216830868-c0145582-9c3a-44ba-b9c2-8a00819bfa69.png)

