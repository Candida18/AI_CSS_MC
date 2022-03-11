# Genetic Algorithms

## Problem Statement :

<p align="justify">
At a university, Professor Symons wishes to employ two people, John and Mary, to grade papers for his classes. John is a graduate student and can grade 20 papers per hour; John earns ₹15 per hour for grading papers. Mary is an post-doctoral associate and can grade 30 papers per hour; Mary earns ₹25 per hour for grading papers. Each must be employed at least one hour a week to justify their employment.
If Prof. Symons has at least 110 papers to be graded each week, how many hours per week should he employ each person to minimize the cost?</p>

---

>>The problem has been formulated as follows.

```
Minimize 
Subject to:     C=15x+25y
                x≥1
                y≥1

Constraint:     20x+30y≥110
                x≥0
                y≥0
```
<p align="justify">
To minimize cost, we will substitute these points in the objective function to see which point gives us the minimum cost each week. The results are listed below.</p>
<br/>

Critical points |	Income 
---------------- | ---------
(1, 3)	         |15(1) + 25(3) = ₹90
(4, 1)	         |15(4) + 25(1) = ₹85

<br/>
<p align="justify">
The point (4, 1) gives the least cost, and that cost is ₹85. Therefore, we conclude that in order to minimize grading costs, Professor Symons should employ John 4 hours a week, and Mary 1 hour a week at a cost of ₹85 per week.</p>



