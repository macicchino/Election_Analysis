# Election_Analysis


## Overview of Election Audit
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received. 
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

In addition to the initial requests, the election commission has also asked for the following:

6. The voter turnout for each county.
7. The percentage of votes from each county out of the total count.
8. The county with the highest turnout. 

## Election Audit Results

The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana Degette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana Degette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Diana Degette, who received 73.8% of the vote and 272,892 number of votes.

The additional analysis shows that:
- The voter turnout by county was the following:
  - Jefferson: 38,855
  - Denver: 306,055
  - Arapahoe: 24,801
- The percetage of votes for each county out of the total votes was the following:
  - Jefferson: 10.5%
  - Denver: 82.8%
  - Arapahoe: 6.7%
- The county with the highest turnout was Denver. 
  - Denver had 82.8% of the vote with 306,055 votes.

## Election Audit Summary

The python script within PyPoll_Challenge.py can be used for any election. As long as the csv file containing the election data has the same 3 columns of variables (Ballot ID, County, Candidate). Add the updated source data to the 'Resources' folder in a csv format. On row 9 of the python code, update the election source data from 'election_results.csv' to the updated source file. In addition, you will want to update the output file on row 11 from 'election_results.txt' to a new .txt file so you do not overwrite the previous election data. 


## Resources
- Data Source: election_results.csv
- Python Template: PyPoll_Challenge_starter_code.py
- Software: Python 3.9.11, Visual Studio Code, 1.71.2
