# Prouster (Version 0.1)
## A neural network to generate writing prompts


### Motivation:
This project is a python-based application for inviduals who may be experiencing Creative Block.
Creative Block is commonly defined as a period of time when ideas and creative thinking seem to run dry. It is a problem that can manifest itself in different ways:

* Technology: Impaired ability to think out-of-the-box to deliver solutions.
* Artists: Lack of inspiration to produce new material.
* Individuals:  Depression & Anxiety, Demotivation

#### Stimulate creative thinking!
Prouster, then, is a Neural Network writing prompt generator that uses a trained model to form interesting ideas for users to respond to or develop upon.

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

* Oblique Strategies
* * https://github.com/tomgp/Oblique-Strategies/tree/master/data

#### Tags
* WP - General Writing Prompt
* OS - Oblique Strategies
* CW - Constrained Writing
* * Example: Write without using pronouns.
* TT - Theme Thursday
* * Example: Detective Stories
* EU - Established Universe
* * Example: Harry Potter Prompts.

### Modeling:
Different approaches to recurrent Neural Networks were used to build Prouster, including:

* PyTorch, Character-Level Model
* Keras, Word-Level & Character-Level Model

These models were trained using kernels provided by Kaggle. 

### Results:
![Demo](https://raw.githubusercontent.com/ander265/prouster/master/Prompt.png)


### Backlog/Next Steps:
* Subsequent prompts based on user response
