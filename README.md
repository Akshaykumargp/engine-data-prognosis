# Remaining Useful Life (RUL) prediction for Turbofan Engines

**Exploring NASAs turbofan dataset**

The project objective is to estimate Remaining Useful Life (RUL) with Machine Learning. RUL is defined as a remaining time that a component can function with an acceptable performance before it fails. 
The model should provide prediction uncertainties and be extensively tested with Prognostics metrics.

[Turbofan Engines Degradation Simulation Data Set](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/) provided by NASA is being used in this project for Remaining Useful Life prediction.

**Experimental Scenario** 

Data sets consist of multiple multivariate time series. Each data set is further divided into training and test subsets. Each time series is from a different engine – i.e., the data can be considered to be from a fleet of engines of the same type. Each engine starts with different degrees of initial wear and manufacturing variation which is unknown to the user. This wear and variation is considered normal, i.e., it is not considered a fault condition. There are three operational settings that have a substantial effect on engine performance. These settings are also included in the data. The data is contaminated with sensor noise.

The engine is operating normally at the start of each time series, and develops a fault at some point during the series. In the training set, the fault grows in magnitude until system failure. In the test set, the time series ends some time prior to system failure. The objective of this project is to predict the number of remaining operational cycles before failure in the test set, i.e., the number of operational cycles after the last cycle that the engine will continue to operate. Also provided a vector of true Remaining Useful Life (RUL) values for the test data. 

 The notebooks are used to explore the dataset and try various modelling techniques (both Machine Learning and Neural Networks).
 
# Running the notebooks
- clone this repository to your computer
- navigate into the folder:  `where you saved your data`
- create a folder for the data: `mkdir data`
- download the data from the official [NASA data repository](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/#turbofan) [3] 
- Extract the `.zip` file to `exploring-nasas-turbofan-data-set/data/`
- You should now have all the data in `exploring-nasas-turbofan-data-set/data/CMAPSSData/`
- use the requirements.txt to recreate the Python environment used to run these notebooks. I prefer using Anaconda, but any Python environment manager will do.
- Activate the environment from your preferred command line tool, navigate to `exploring-nasas-turbofan-data-set` and start your local notebook server by typing `jupyter notebook`
- Have fun following along with the notebooks!
The data are provided as a zip-compressed text file with 26 columns of numbers, separated by spaces. Each row is a snapshot of data taken during a single operational cycle, each column is a different variable. The columns correspond to:
1)	Unit number
2)	Time, in cycles
3)	Operational setting 1
4)	Operational setting 2
5)	Operational setting 3
6)	Sensor measurement 1
7)	Sensor measurement 2
...
26)	Sensor measurement 26

**EDA:**

 **Visualize total number of cycles by each engine**
 
 ![image](https://user-images.githubusercontent.com/98378358/210370613-dea3a5f3-03cf-405e-a07b-bcdbf50a0260.png)

 **Observations:**
By observing above visualization we get to know that the number of cycles run by the each engine before failing.

** Mean number of cycles and histogram of number of cycle**
![image](https://user-images.githubusercontent.com/98378358/210370646-d69d2be8-91ff-4d2c-bdef-8ce7f28511cb.png)

**Observations:** 
By observing the above graph we can say that the Mean number of cycles after which jet engine fails is 206

**Histogram representation of each sensor data**

 ![image](https://user-images.githubusercontent.com/98378358/210370691-966d1bb4-828c-4c60-a36c-1650c5a961d6.png)

**Observations:**
As we could see there are many sensor data which aren't following the normal distribution, we will tend to ignore those sensors for our model training. We would try to reduce the curse of dimensionality by doing so.

**Machine learning models**
![image](https://user-images.githubusercontent.com/98378358/210370762-e68d778c-29c3-4d2c-bcb4-b06d8ec00ff0.png)

After doing EDA & Training the data we applied few machine learning models to the training data to see how model behaves. The following table contains machine learning models and the respective results we got.
 
**Summary**

By training with the above all models, XGboost  regressor model is performing best, so i choose the xgboost model for further testing and final predictions.


**References**
[1] [blog post series](https://towardsdatascience.com/tagged/exploring-nasa-turbofan)  
[2] A. Saxena, K. Goebel, D. Simon, and N. Eklund, “Damage Propagation Modelling for Aircraft Engine Run-to-Failure Simulation”, in the Proceedings of the Ist International Conference on Prognostics and Health Management (PHM08),
 Denver CO, Oct 2008.  
[3] Data repository: [https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/#turbofan](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/#turbofan)

