# Multilabel Game Genre Classifier

## Introduction

This project is a multilabel game genre classifier that takes the description of a game as input and predicts its genres. The model was fine-tuned using a BERT model of base-uncased varient with a dataset collected from [metacritic.com](https://metacritic.com). The dataset includes game descriptions and genres for major platforms, such as Nintendo 3DS, iOS, PC, PS4, Nintendo Switch, PS Vita, Wii-u, and Xbox One.

Using this dataset was highly encouraged because games are a unique form of entertainment and may not be the initial choice for many people compared to movies, books, or TV shows. The accuracy of the game genre classifier was around 96.4%, making it highly reliable.

The model has been deployed to [Hugging Face Spaces](https://huggingface.co/), and its API is linked to a website deployed on [Render](https://render.com/). Check out the live demo [HERE](https://multilabel-game-classifier.onrender.com)

## Preview of the deployed webpage
![webpage_demo](https://user-images.githubusercontent.com/52294804/219456382-1656158b-057b-48c5-84dd-791a93d46a71.jpg)



## Dataset Collection and Cleaning

The game description and genre data were collected using [Selenium](https://selenium-python.readthedocs.io/) from [metacritic.com](https://metacritic.com) for different platforms. [metacritic.com](https://metacritic.com) has a huge database of reviews and ratings of various games of different platforms along with movies and TV series. Initially, the URLs of the games were collected from the list of games for each platform. Then, the URLs of each game were visited to retrieve their descriptions and genres. The total number of collected descriptions was 122,857. After removing duplicates or null data, the final dataset contained 91,179 rows.


The model can predict upto 74 lables. These are:

Miscellaneous, Compilation, Action, General, Platformer, 2D, Simulation, Virtual, Virtual Life, Puzzle, Logic, Flight, Shooter, Shoot-'Em-Up, Combat, Vertical, Beat-'Em-Up, Driving, Racing, Arcade, Other, Automobile, Fighting, Horizontal, Board Games, Board / Card Game, Adventure, 3D, First-Person, Matching, Role-Playing, Japanese-Style, Vehicle, Roguelike, Action Adventure, Fantasy, Third-Person, Open-World, Sports, Individual, Strategy, Turn-Based, Tactics, Career, Visual Novel, Team, Soccer, Edutainment, Hidden Object, Party / Minigame, Sandbox, Sci-Fi, Tactical, Card Battle, Rhythm, Music, Real-Time, Defense, Top-Down, Light Gun, Action RPG, Historic, Management, Business / Tycoon, Survival, Civilian, Linear, Sim, Modern, Point-and-Click, Government, Massively Multiplayer, Text and Massively Multiplayer Online.

Duplicates of descriptions were removed, as many games are released on multiple platforms. Duplicate data based on game title was not removed, as some games have different versions on different platforms.
Check out the dataset in the the repo at datasets/merged_descriptions.csv

## Model training
The model was trained using huggingface/fastAI, and the BERT-base-uncased model was used since it is widely used and effective. The BERT large model requires a high system requirement, but the base model is fast and less resource-intensive. After training the model, it was converted into a smaller and more efficient version using ONNX. 
<br>
The accuracy score of the model are
<br>
F1 Score (Micro) = 0.6381031613976705
<br>
F1 Score (Macro) = 0.5104485475364295

## Model Compression with ONNX
The initial model was 416MB in size and through onnx quantization method the final size came down to 104MB and a bit faster at the same time.

## Model deployment
The model was deployed on Hugging Face, and the model API was connected to a website that was set up on Render using Flask.


## Building and running the source code

The codes used are given in the codes folder with comments explaining their use cases. The system to build the source code is given below.

1. Download the repository on your pc using the following command. 
```bash
git clone https://github.com/AbrarAdnan/multilabel-game-genre-classifier.git
```
2. Activate the virtual environment
On Windows:
```bash
virtualenv venv
venv\Scripts\activate
```
On Mac/Linux:
```bash
virtualenv --no-site-packages  venv
source venv/bin/activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Open jupyter notebook by running the following command in the terminal 
```bash
jupyter notebook
```
5. Navigate to the codes folder and run the notebooks serially as per their given name. Further instructions are given in the comments of each notebook.

# Note
1. Data scraping takes a very long time.
2. The pictures used on the render website were made using DALL-E-2
3. Model training was done on colab. The rest of the code was run on local pc.
