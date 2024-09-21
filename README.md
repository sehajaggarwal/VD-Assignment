# VakilDesk Technologies Technical Assessment
## Overview
This repository contains the solutions for the technical assessment provided by VakilDesk Technologies. Each solution is organized into directories corresponding to specific questions.
## Directory Structure
VDT1 corresponds to solution for Q1. It consists of a python file named accordingly i.e. Q1.py alongwith snapshot of expected result.
You can change the input values in the 'test the solution' section i.e. in the main block.
*Note:* VDT3 (Django Application) doesn't follow this structure.
## Requirements
Ensure that Python 3.12.6 is installed on your system before proceeding. You can download it from python.org.
## Installation
1. Clone the repository to your local machine:
```git clone <repository-url>```
```cd <repository-name>```
2. Install the required packages:
```pip install -r requirements.txt```
## Running Solutions
### For VDT1,2,4,5,6
Use the following command:
```python <filename.py>```
Example:
```python VDT1/Q1.py```
### For VDT3
1. Open the VDT3 directory:
 ```cd VDT3```
2. Create a virtual environment:
 ```python -m venv <environmentname>```
3. Activate the virtual environment:
   On windows- 
 ```<environmentname>\Scripts\activate```
4. Install Django:
 ```pip install django```
5. Change directory:
```cd vdt3```
6. Run the server:
```python manage.py runserver```
7. Open your browser and navigate to http://localhost:8000/top-customers/ to view the results.
   #### Editing seed data in VDT3
   If you wish to modify the seed data, follow these steps:
      1. Navigate to the JSON file in the fixtures directory.
      2. Make the required changes.
      3. Load the updated data:
         ```python manage.py loaddata myapp/fixtures/orders.json```
      4. Repeat steps 6 and 7 from above to see the updated results.
## Conclusion
This repository serves as a solution to the technical assessment for VakilDesk Technologies. If you have any questions or need further assistance, feel free to reach out.








