# StudyHelper

Python program that helps student study for their exams by randomly generating questions on subjects, provided a `.csv` file with all sub-subjects listed. 

To be able to work, you need to have installed the following libraries

- `pandas`
- `numpy`

You can install each of them running the following command in terminal :

```
pip install -r requirements.txt
```

## Structure of the directory

The directory should have such structure :

```
StudyHelper
├───course1
│   ├───subjects.csv
├───course2
│   ├───subjects.csv
...
// List of subjects 
├───courses.txt
├───requirements.txt
└───main.py
```

1. You **must update** the `path` variable in `main.py` with the **full path** to the clone of this repository

2. You have to organize the `subjects.csv` file as the following, with **each column a chapter** :

``` csv
// First line correponds to the list of chapters
Week 1,Week 2,Week 3,Week 4,Week 5,Week 6,Week 7,Week 8,Week 9,Week 10,Week 11,Week 12,Week 13,Week 14

//Next lines are subjects per chapter (column)
"Subset sequence (R, N, Z, C, I, ...)",Multiple conditioning,"Cumulative distribution function (def, prop (6))",Notions of convergence,Uniform continuous distribution,,,,,,,,,
Union,Independence,PMF from CDF,Law of small numbers,Exponential distribution,,,,,,,,,
Intersection,Types of independence,Transformations of discrete random variables,WHICH DISTRIBUTION ?,Gamma distribution,,,,,,,,,
Complement,Probability mass function (PMF),Expectation : def,Continuous random variables,Laplace distribution,,,,,,,,,
Difference,"Binomial random variable (PMF, prop, meaning)",Expected value of a function,Probability density functions,Pareto distribution,,,,,,,,,
Symmetric difference,"Geometric distribution (PMF, prop, meaning)",Properties of expected value,,Moment of continuous variable : expectation,,,,,,,,,
Complement of infinite union,Lack of memory,Moment of a distribution,,Moment of continuous variable : variance,,,,,,,,,
Complement of infinite intersection,"Negative binomial distribution (PMF, prop, meaning)",Central moment of a distribution,,Conditional densities,,,,,,,,,
Partition (2),"Gamma function (def, prop (4))",Variance of a distribution,,X discrete or continuous ?,,,,,,,,,

...

```

3. You can rename the `course1` and `course2` folders by `Analysis`, `Programming` for instance, update their names in `courses.txt` (an update will consist of doing this automatically based on the folders' names). You can also create new folders, with the names you want ; all it needs is to have a `subjects.csv` in it, structured as above.

```
...
├───course_name
│   ├───subjects.csv
...
```

Everything is now settled, enjoy !

## Example of an instance of the program in practice


```
[1] Analyse IV
[2] Introduciton to Machine Learning
[3] Introduction to Visual Computing
[4] Musical Improvisation and Creativity
[5] Parallelism & Concurrency
[6] Probabilities and Statistics
[7] Programmation OS
[8] Signals and Systems
[9] Theory of Computation

[Q] Quit
> s
Wrong input. Please type in a number between '1' and '9' or 'Q'
> 6
Random ? [y/n] : y
```

```
PROBABILITIES AND STATISTICS

[1] Week 1
[2] Week 2
[3] Week 3
[4] Week 4
[5] Week 5
[6] Week 6
[7] Week 7
[8] Week 8
[9] Week 9
[10] Week 10
[11] Week 11
[12] Week 12
[13] Week 13
[14] Week 14

[A] All chapters

[Q] Quit
> s
Wrong value. Please try again with a value between 1 and 14
> A
```

**Press `ENTER` to pass from a sub-subject to another**

```
Press [ENTER] to pass to next subject

Law of small numbers                                                [1/70]
Hypergeometric distribution (PMF, meaning)                          [2/70]
Moment of a distribution                                            [3/70]
Probability space (3)                                               [4/70]
Pascal's triangle                                                   [5/70]
Union                                                               [6/70]
X discrete or continuous ?                                          [7/70]
Partition (2)                                                       [8/70]
Complement of infinite intersection                                 [9/70]
Geometric distribution (PMF, prop, meaning)                        [10/70]
Continuous random variables                                        [11/70]
```