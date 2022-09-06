# Captains log

### August 30th, 2022
I am starting  this log as a way of tracking my progress in the learning of Python.
My goal is to work on it every day, even a bit, and commit code daily.
The first exercises will be simple, but as the learning progresses I expect to be adding solutions to complex problems too.
I started the course on September 25th, and I plan to finish it by October 7th.

#### Lesson 144 Exercise
Had to rethink twice the use of reverse() and extend() as they act upon the original object and return None. Other than that it was a good refresher of these four odd functions: map(), filter(), zip(), and return()
I realised that I made an error of judgement using reverse() as in real life the list may have not been "just" reversed but unsorted.

#### Lesson 146 Exercise
Fascinating exercise which I could have gotten at first I had paid attention to the explanation of the exercise. I missed the way of sorting it (second element) because I was doing the first part of the exercise.

#### Lesson 148
Comprehensions are really powerful!

#### Lesson 149
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

#### Lesson 156 Exercise
Took a while to figure out how to find the parameter, but once I did the solution was spot on

#### Lesson 166 Fibonacci Exercise
Horribly wrong. Just because I did not think enough and went for the usual recursive solution and tried to apply generators into that. It did not go well...

### August 31st, 2022

#### Lesson 175 Guessing game exercise
Took me a while to get started, but I did pretty easily, with the dynamic prompt by default and an extra attempt counter.

I have decided to jump on Section 19 Web Development with Python to start making and advance in my web / app.

### September 2nd, 2022

#### Lesson 188 Translator
Very nice exercise, with lots of room for improvement (the problem) which I will attempt later today. I have attemped to solve the following exercise, based on the original one:
1.- ask the user for the name of the source file (ENTER will just read from console)
2.- ask the user for the name of the final file (ENTER will just print out in console)
3.- ask the user for input language (ENTER will default to English)
4.- ask the user for out language (ENTER will default to whatever tickles your fancy)
5.- if the input is manual, END will stop the program.
I also thought of limiting the number of languages (you can see the prompts) bau can't be arsed at the moment.

### September 6th, 2022


#### Lesson 212 JPG to PNG Converter
Back after a while. I have done the exercise (hopefully) adding some nice features (I have not yet watched the solution). 
I have also developed a small tiny script to compress JPEG images recursively. This comes from the need to reduce the size of a Wordpress repository. I can now reduce the quality of the jpeg images and upload them in bulk. The next steps for this tool are:
 - comment the code
 - add more parameters, maybe and more options to work with (reduce size, display weight, ) 
