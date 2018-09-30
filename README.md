# Prouster
## A Deep Learning Writing Aid

This project is a python-based application for inviduals who may be experiencing Creative Block.
Creative Block is commonly defined as a period of time when ideas and creative thinking seem to run dry. It is a problem that can manifest itself in different ways:

* Technology: Impaired ability to think out-of-the-box to deliver solutions.
* Artists: Lack of inspiration to produce new material.
* Individuals:  Depression & Anxiety, Demotivation

### Motivation:
The motivation for this project was to provide a plausible solution to creative block, and the general inability for individuals to brainstorm or improvise new ideas. The most obvious example of this problem is writer's block, and as such my project targets that dilemma. 

#### Stimulate creative thinking!
Prouster is a Deep Learning based writing prompt generator designed to form interesting ideas for users to respond to or develop upon.
The website for Prouster currently generates text from a Recurrent Neural Net to create unique writing prompts that users can borrow as inspiration for new stories, monologues, or editorials. 
![Early Version](https://raw.githubusercontent.com/ander265/prouster/master/Prompt.png)

### Potential Use Cases:
It is an exciting product that can be used for various purposes:
* Interactive Brainstorming
* Writing Contests
* Improvised Response
* English Teaching
* Beneficial to Mental Health

### Data:

#### Sources

* Writing Prompts from Reddit
* * https://www.reddit.com/r/datasets/comments/8z1g24/rwritingprompts_dataset_for_language_models/

#### Tags
* WP - General Writing Prompt
* CW - Constrained Writing
* * Example: Write without using pronouns.
* TT - Theme Thursday
* * Example: Detective Stories
* EU - Established Universe
* * Example: Harry Potter Prompts.

The website Prouster generates stories based off prompts with the Reality Fiction tag (RF).

### Modeling:
Different approaches to recurrent Neural Networks were used to build Prouster, including:

* PyTorch, Character-Level Model
* Keras, Word-Level & Character-Level Model

These models were trained using kernels provided by Kaggle. The current main branch includes a website that deploys the Word-Level Keras model. 

### Results:
Here is a demo of the current functionality of the Prouster website.
![Newest Version](https://raw.githubusercontent.com/ander265/prouster/master/demo.gif)

### In Development:
* IBM Watson API is being implemented for more advanced user writing style analysis. 
* Training an Adversarial Neural Net to compare results with the current Keras functionality.

## References
* Kudos to MachineLearningMastery for the resources I needed to build the right RNN for this project.
https://machinelearningmastery.com/how-to-develop-a-word-level-neural-language-model-in-keras/
