# TSP - Simulated Annealing Implementation
**Simulated annealing** implementation using multiples instances with differents city quantities and diagram display to resolve the **Traveling Salesman Problem (TSP)**.

*Final work of the discipline of design and analysis of algorithms.

## Summary
**1.** TSP Explanation
**2.** Instances
**3.** Build and Run

## TSP Explanation
The **Travelling Salesman Problem (TSP)** is the challenge of finding the shortest yet most efficient route for a person to take given a list of specific destinations. It is a well-known algorithmic problem in the fields of computer science and operations research.

## Instances
All instances has explicity edge weight.
**1.** gr17 - Set of 17 cities with lower diagram format.
**2.** gr24 - Set of 24 cities with lower diagram format.
**3.** gr48 - Set of 48 cities with lower diagram format.
**4.** si175 - Set of 175 cities with upper diagram format.
**5.** si535 - Set of 535 cities with upper diagram format.
**6.** si1032 - Set of 1032 cities with upper diagram format.

## Build and Run
**1.** Create python virtual environment running:
```
virtualenv -p python3 venv
```
**2.** Switch to Python 3 virtual environment:
```
source venv/bin/activate
```
**3.** Install project requirements:
```
sudo pip3 install -r requirements.txt
```
**4.** Run project:
```
python3 SimulatedAnnealing.py
```
**5.** Check results opening the results.txt file.