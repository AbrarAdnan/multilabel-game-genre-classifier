# Multilabel Game Genre Classifier

## Introduction

This project is a multilabel game genre classifier that takes the description of a game as input and predicts its genres. The model was fine-tuned using a BERT-base model with a dataset collected from metacritic.com. The dataset includes game descriptions and genres for major platforms, such as Nintendo 3DS, iOS, PC, PS4, Nintendo Switch, PS Vita, Wii-u, and Xbox One.

Using this dataset was highly encouraged because games are a unique form of entertainment and may not be the initial choice for many people compared to movies, books, or TV shows. The accuracy of the game genre classifier was around 96%, making it highly reliable.

The model has been deployed to Hugging Face Spaces, and its API is linked to a website deployed on Render. You can visit the website to see a live demonstration of the model.

## Dataset Collection and Cleaning

The game description and genre data were collected using Selenium from metacritic.com for different platforms. Initially, the URLs of the games were collected from the list of games for each platform. Then, the URLs of each game were visited to retrieve their descriptions and genres. The total number of collected descriptions was 122,857. After removing duplicates or null data, the final dataset contained 91,184 rows.

The labels that the model can predict include
Miscellaneous, Compilation, Action, General, Platformer, 2D, Simulation, Virtual, Virtual Life, Puzzle, Logic, Flight, Shooter, Shoot-'Em-Up, Combat, Vertical, Beat-'Em-Up, Driving, Racing, Arcade, Other, Automobile, Fighting, Horizontal, Board Games, Board / Card Game, Adventure, 3D, First-Person, Matching, Role-Playing, Japanese-Style, Vehicle, Roguelike, Action Adventure, Fantasy, Third-Person, Open-World, Sports, Individual, Strategy, Turn-Based, Tactics, Career, Visual Novel, Team, Soccer, Edutainment, Hidden Object, Party / Minigame, Sandbox, Sci-Fi, Tactical, Card Battle, Rhythm, Music, Real-Time, Defense, Top-Down, Light Gun, Action RPG, Historic, Management, Business / Tycoon, Survival, Civilian, Linear, Sim, Modern, Point-and-Click, Government, Massively Multiplayer, Text and Massively Multiplayer Online.

Duplicates of descriptions were removed, as many games are released on multiple platforms. Duplicate data based on game title was not removed, as some games have different versions on different platforms.

## Model training
The model was trained using huggingface/fastAI, and the BERT-base-uncased model was used since it is widely used and effective. The BERT large model requires a high system requirement, but the base model is fast and less resource-intensive. After training the model, it was converted into a smaller and more efficient version using ONNX.

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
2. The picture used on the render website was made using DALL-E-2
3. Model training was done on colab. The rest of the code was run on local pc.
