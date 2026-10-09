# Introduction to programming and vibe coding

Welcome to this crash course on programming and vibe coding! 

With the advanced coding agent which can write code for us, there's no need to dive into coding details, e.g., syntax of each programming language. Therefore, in this beginner course, I want to focus on some basic and transferable concepts in programming, and emphasis some useful principals to keep in mind when you build more complexe "code eco-system" with agent. The aime of this course, is not to teach you to become an independant programmer, but to help you understand "what is programming" in a general way, and show you how to better use LLMs to help you coding (so called vibe coding), as well as the limitations if it. Python will be the programming language being used in this course, since it's widely used and its syntax is the most human-friendly.

## A word about the running environment

We will run the Notebook in Google Colab, to avoid complicate running environment setups. 

If you want to run this Notebook on your own computer, apart from basic installation of Python, you may also need to install some additional packages for running Notebooks(`.ipynb` files) (e.g., ipykernel, ipywidgets, IPython, etc.). I'll suggest beginner's to install Python within [Anaconda](https://www.anaconda.com/download), with which you should be able to run Notebooks directly with **Jupyter Notebook**, and some of the packages (like `openpyxl`) are already installed inside. But you may still need to install and download supplementary packages (`dateparser`, `spaCy` and its English model `en_core_web_sm`) for NLP-tasks in this notebook.

## Mental setup for this course

Try whatever you want in this notebook to see what happens, it's your playground, you won't crush anything. 

**Don't be afraid of errors and bugs.** Having errors, taking time to analyse the reason, and then fixing them, that's how we learn to code. Of course you can ask LLMs for help, but if you want to learn, take some time to read and understand its explainations instead of copy paste directly its solution. You'll learn much more by solving the bugs than having everything run smoothly and zero problems.

## Short explanation about files in this repository

- **Most important file: [`TD_student.ipynb`](TD_student.ipynb)**, it explains everything, has exercices to be finished (marked with `TODO`), and linked to other supportive files (e.g. data and answers) for the tasks.

- [`Slides_programming_intro_VF.pdf`](Slides_programming_intro_VF.pdf): Just show with graphics want I explained in "Analogies for programming" section in `TD_student.ipynb`, credits to GPT for generating the first version of these beautiful illustrations in these slides, hooray 🙌

- [`tools.py`](tools.py): it includes functiions created specifically for this notebook, you don't need to understand each line in this script, consider it as a toolkit and observe how the functions in it are used/called in [`TD_student.ipynb`](TD_student.ipynb) will be enough. The objectif is to show you how scripts collaborate among them, or, in other words, how to import existing functions.

- If you're curious and want to learn more: I chose some functiions in [`tools.py`](tools.py) and annotated them in [`tools_annotated.py`](tools_annotated.py) with comments. You can check this file and try to understand them.



<p align="center"><strong>Now, enjoy your coding journey !</strong></p>