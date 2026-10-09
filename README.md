# Introduction to Programming and Vibe Coding

Welcome to this crash course on programming and vibe coding! 

With advanced coding agents that can write code for us, there's no need to dive into coding details such as the syntax of each programming language any more. Therefore, this beginner-level course focuses on basic, transferable programming concepts, and highlights useful principles to keep in mind when building more complex "coding ecosystem" with AI agents. 

The aime of this course is not to teach you to become an independent programmer. Instead, it will help you **understand programming in general**, and show you how to better use LLMs when coding (a practice widely known as **vibe coding**), as well as be aware of their limitations. 

Python is the programming language used in this course, because it is widely used and has relatively readable, beginner-friendly syntax.

## A Word About the Runtime Environment

We will run the notebook in Google Colab to avoid complicated environment setup. 

If you want to run this notebook on your own computer, in addition to the core Python installation, you may need to install some packages for running notebooks(`.ipynb` files), such as `ipykernel`, `ipywidgets` and `IPython`. I recommend that beginners install Python by installing [Anaconda Distribution](https://www.anaconda.com/download). It allows you to run notebooks directly with **Jupyter Notebook**, and already includes some of the packages required for this course (like `openpyxl`). However, you may still need to install some additional packages (`dateparser`, `spaCy` and its English model `en_core_web_sm`) for the natural language processing tasks in this notebook.

## A Mindset for Learning to Code

Try whatever you want in this notebook and see what happens. It's your **playground**, you will not break anything. 

**Don't be afraid of errors and bugs.** Encountering errors, taking time to analyse their causes, and then fixing them, that is how we learn to code. Of course you can ask LLMs for help. However, if you want to learn, take some time to read and understand their explanations instead of directly copying and pasting their solutions. You will learn much more by solving bugs than by having everything run smoothly without any problems.

## A Short Explanation of the Files in This Repository

- **Most important file: [`TD_student.ipynb`](TD_student.ipynb)**, it explains everything, has exercises to complete (marked with `TODO`), and links to other supporting files (e.g. data and answers to the exercises).

- [TD_en_answer.ipynb](TD_en_answer.ipynb): it has exactly the same content as [`TD_student.ipynb`](TD_student.ipynb), but includes solutions to the exercises. [TD_en_answer.pdf](TD_en_answer.pdf) is the PDF version.

- [`Slides_programming_intro_VF.pdf`](Slides_programming_intro_VF.pdf): it visually presents the ideas explained in the "Analogies for programming" section of `TD_student.ipynb`. Credit to GPT for generating the first version of the illustrations used in these slides, hooray! 🙌

- [`tools.py`](tools.py): it contains functions created specifically for this notebook. You do not need to understand every line in this script. Think of it as a toolkit and observe how its functions are imported and called in [`TD_student.ipynb`](TD_student.ipynb). The objective is to show you how scripts can work together, or, in other words, how existing functions can be imported and reused.

- If you are curious and want to learn more: I selected some functiions from [`tools.py`](tools.py) and added explanatory comments to them in [`tools_annotated.py`](tools_annotated.py). You can read this file and try to understand how the functions work.



<p align="center"><strong>Now, enjoy your coding journey!</strong></p>