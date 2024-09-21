# VakilDesk Technologies Technical Assessment
## Overview
This repository contains the solutions for the technical assessment provided by VakilDesk Technologies. Each solution is organized into directories corresponding to specific questions.
## Directory Structure
VDT1 corresponds to solution for Q1. It consists of a python file named accordingly i.e. Q1.py alongwith snapshot of expected result.</br>
You can change the input values in the 'test the solution' section i.e. in the main block.</br>
*Note:* VDT3 (Django Application) doesn't follow this structure.
## Requirements
Ensure that Python 3.12.6 is installed on your system before proceeding. You can download it from python.org.
## Installation
1. Clone the repository to your local machine:</br>
```git clone <repository-url>```</br>
```cd <repository-name>```
2. Install the required packages:</br>
```pip install -r requirements.txt```
## Running Solutions
### For VDT- 1,2,4,5,6
Run the following command in your terminal:</br>
```python <filename.py>```</br>
*Example:*
```python VDT1/Q1.py```
### For VDT3
1. Open the VDT3 directory:</br>
 ```cd VDT3```
2. Create a virtual environment:</br>
 ```python -m venv <environmentname>```
3. Activate the virtual environment:</br>
    *On windows:* </br>
```<environmentname>\Scripts\activate```
4. Install Django:</br>
 ```pip install django```
5. Change directory:</br>
```cd vdt3```
6. Run the server:</br>
```python manage.py runserver```
7. Open your browser and navigate to http://localhost:8000/top-customers/ to view the results.
   #### Editing seed data in VDT3
   If you wish to modify the seed data, follow these steps:
      1. Navigate to the JSON file in the fixtures directory.
      2. Make the required changes.
      3. Load the updated data:</br>
         ```python manage.py loaddata myapp/fixtures/orders.json```
      4. Repeat steps 6 and 7 from above to see the updated results.
## Conclusion
This repository serves as a solution to the technical assessment for VakilDesk Technologies. If you have any questions or need further assistance, feel free to reach out.








