DOCUMENT_1 = """
Q1 c (BB?)
For the second part of question 1, c we assume that we have one dirty input and one clean input right?

If we were allowed to have two dirty inputs then this seems false. Eg:

Input 1 = [1,1,0]

Input 2 = [1,0,0]

Output 1 (Hi) = [1,1,1]

Output 2 (Lo) = [0,0,0]
"""

DOCUMENT_2 = """
Take home final Q1a what does it ask exactly?
"a merge-and-split element can be implemented by a sorting network"

I don't quite get it on the English level to be honest. 

So a merge-and-split element is a node of a merge-and-split network that take in 2 input lists and do sth(merge sorting in this case) to make sure merge-and-split network eventually output a sorted array right? it's a {N^L, N^L} -> N^2L function?

and a sorting network is just sort a sequence whatever how it's implemented,

Now isn't by definition the sorting network implemented the merge-and-split network??
"""

DOCUMENT_3 = """
Take home Q2 a) i. Can't find optimal n without running out of memory
This is a duplicate of @564 and @544.



I was thinking that the question implies that once you reach the optimal n, you need to get a few measurements above that n to show that the FLOPS go down after peaking at n. But in my trials, the FLOPS continue increasing with n, although the growth slows, until the computations take way too long (>15 sec) or the memory runs out.

Am I misinterpreting the question? Sorry for the duplicate but I’m not sure how to answer the question without knowing this.
"""


