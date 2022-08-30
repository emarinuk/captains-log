# Captains log

## August 30th, 2022
I am starting  this log as a way of tracking my progress in the learning of Python.
My goal is to work on it every day, even a bit, and commit code daily.
The first exercises will be simple, but as the learning progresses I expect to be adding solutions to complex problems too.
I started the course on September 25th, and I plan to finish it by October 7th.

### Lesson 144 Exercise
Had to rethink twice the use of reverse() and extend() as they act upon the original object and return None. Other than that it was a good refresher of these four odd functions: map(), filter(), zip(), and return()
I realised that I made an error of judgement using reverse() as in real life the list may have not been "just" reversed but unsorted.

### Lesson 146 Exercise
Fascinating exercise which I could have gotten at first I had paid attention to the explanation of the exercise. I missed the way of sorting it (second element) because I was doing the first part of the exercise.

### Lesson 148
Comprehensions are really powerful!

### Lesson 149
I got this right at first :) Good thinking of the use of set. I think my solution is a bit cleaner than Andrei's.

High Order Function:
 - either a function that accepts another function<br /> 
&nbsp;&nbsp;&nbsp;&nbsp;def greet(func):<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;func()<br />
- or a function that returns other function<br />
&nbsp;&nbsp;&nbsp;&nbsp;def greet2(): <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;def func():<br /> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pass<br /> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return func()<br />

### Lesson 156 Exercise
Took a while to figure out how to find the parameter, but once I did the solution was spot on 