# FORKED

### How to run!
_Windows 10 steps_

Open up cmd or Powershell (Powershell prefered) as Administrator and move to this repo directory

Create Python virtual environment
> python -m venv sdp-env

Run virtual environment
> sdp-env/Scripts/activate

Install the library
> pip install -r requirements.txt

_If above command result an error, run the cmd or Powershell as Administrator and then re run the above command_

Run the models
> python src/comparison.py

### Result
The results are present in **_result.txt** file. 

- [Create venv Windows](https://docs.python.org/3/library/venv.html)
- [Activate venv Windows](https://stackoverflow.com/questions/65552171/how-to-activate-virtualenv-on-windows)


# Software_Defect_Prediction

**Software Defect Prediction** is one of the most assisting activities of the testing phase of **Software Development Life Cycle**. It helps to identify the defect-prone modules and provides development groups with observable results.

In this project, we used **NASA** datasets from the [PROMISE Software Engineering Repository](http://promise.site.uottawa.ca/SERepository/datasets-page.html) and built prediction models using **Convolutional Neural Network**, **Random Forest Classifier**, **Support Vector Machine** and tested them on various metrics.

For performance evaluation, we used four widely used metrics: Precision, Recall, Accuracy, and AUC curve.

<strong>Result</strong> <br>
The results are present in **_result.txt** file. 
