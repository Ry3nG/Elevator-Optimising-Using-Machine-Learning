# Elevator-Optimising-Using-Machine-Learning
Project developed for NTU DeepLearning Hackathon

## 1. Problem Statement and Aim
Today, more and more IoT devices are already changing every aspect of life, and elevators as an important part of life are no exception. For example, KONE uses the Watson IoT Platform running on IBM Cloud to collect streams of incoming data about movement, vibration, loading, and other information.

However, we've noticed that despite more and more elevator companies are concerned about how their elevators actually perform, not all of their products are running with IoT devices embedded. 

Therefore, we want to provide a solution that can be retrofitted to any existing elevator and provide companies with a range of data about user experience and elevator performance through data processing and Machine Learning.















# Archived(will be deleted once finished)
-------------------------------------------
## Existing Algorithms for Elevator Control
1. FCFS: First Come First Serve
2. SSTF: Shortest Seek Time First
3. SCAN: 
   
## Development
Aim: Develop an algorithm to control TRADITIONAL ELEVATOR based on Machine Learning to beat SSTF and SCAN.
> Traditional Elevator: one elevator, no group control

TODOs
* Decide on a Machine Learning Algorithm
* Decide on what parameters we should consider.

Flow of events
1. Separating the dataset to train and test
2. EDA: histograms, box plots on floors
3. EDA: Time distribution by hour, day, week, if possible (generate time series)
4. 


## Model
* Prediction problem: predict where the elevator is gonna stop
* Consider factors like: work calendar, weather (raining then less people using elevator)