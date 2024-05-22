# Number Prediction App

This application leverages Machine Learning (ML), Artificial Intelligence (AI), and Deep Learning (DL) to predict numbers between one and hundred from an uploaded image. The app uses a fine-tuned EfficientNet model trained on custom data for accurate predictions.

## Features

- **Image Upload**: Users can upload an image containing a number.
- **Number Prediction**: The application processes the image and predicts the number shown in the image.

### Technical Stack

- **TensorFlow**: Used for developing and fine-tuning the EfficientNet model.
- **AWS S3**: For storing and retrieving training data.
- **Python 3.11.x**: Programming language used for developing the application.
- **FastAPI**: Backend framework for handling requests and performing inference.
- **Streamlit**: Frontend framework for creating an interactive user interface.


## Getting Started

Follow these steps to set up and run the project locally.



## Clone the Repository

   Pull the repository to your local system using the following command:
   
   `git clone https://github.com/azmd801/written-number-image-classifier`
   `cd https://github.com/azmd801/written-number-image-classifier`




## Setting up environment
### Creating environment
``virtualenv venv``  
### Activate environment
``source venv/Scripts/activate``  
### Install dependencies
```pip install -r requirements.txt```  

# Run the following commands to tun this project locally
## start backend 
`python app.py`  
## strat front end client
`streamlit run client.py`  

This will start the app having this interface
![alt text](<Screenshot (332).png>)

# Setting up gihub
`git init`  
`git branch -M main`  
`add files not to be tracked in .gitignore`  
`git add .` 
`git commit -m "your commit message"` 
`git branch -M main` 
`git remote add origin https://github.com/azmd801/written-number-image-classifier.git` 
`git push -u origin main` 