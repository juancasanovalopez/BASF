# BASF
## Coding Challenge
### Prerequisites
The following challenges can be solved in any programming language which is popular today (e.g. COBOL
is not recommended). You can send your source code via email to timo.himmelsbach@basf.com or provide
a link to a public github repo. Your code may be incomplete or may not work - please hand it in anyway!

### Challenge 1 - Algorithms
Given three ordered arrays of arbitrary length containing random capital letters, write an algorithm which
returns the longest ordered array which all arrays share!
#### Example
Given the sequence ADDB and CDDE and EDDF the longest shared array is DD. 
#### Example
Given the sequence UIBAZDBSIAHFB, PQACIZDBIBDLAG and QIDBCZDBKSHDVF, the longest shared
array is ZDB.

### Challenge 2 - Algorithms
Assume an array of arbitrary length whose elements represent colors of the set blue (b), green (g) or red (r).
Write an algorithm which returns the number of subsets in which the array can be split so that every subset
contains equal color representations! Remark: The colors do not have to appear in equal order within the
subsets.
##### Example
Given the array r-r-b-b-g-g, the algorithm will return 1 since the array can be split into one subset of length
6 which contains 2r, 2b and 2g elements.
##### Example
Given the array r-r-b-b-g, the algorithm will return 0 since no equal subsets can be found. 
##### Example
Given the array r-b-g-g-b-r, the algorithm will return 3 since array of length 6 itself features equal color
representation. When splitting the array into two sections of length three, two equal subsets can be identified:
r-b-g and g-b-r.