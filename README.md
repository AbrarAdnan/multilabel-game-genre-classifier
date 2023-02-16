# multilabel-game-genre-classifier

In this project I've tried to make a multilabel game genre classifier. Which will take the description of a game as input and it'll tell us what are the genres of the game.
I've fine-tuned a bert-base model with our dataset collected from metacritic.com. I've scraped game description data of all the major platforms along with the genres to prepare out dataset. Then I cleaned up the dataset and trained the game genre classifier. Using this dataset was highly encouraged because usually movies, books or tv series would be initial choice of many and games would be more unique among them. The accuracy of the game genre classifier was very good at around 96%
We've deployed the model to the huggingface spaces and used the model api to link to a website deployed on render. You can visit the website to get a live demonstration of the model.

More detailed documentation of the project is given below.

# Dataset collection and cleaning up
I've collected game description and genre data using selenium from metacritic.com of different platforms such as Nintendo 3DS, iOS, PC, PS4, Nintendo Switch, PS Vita, Wii-u and Xbox One. I initially collected the urls of the games form the list of games of each platforms. Then visited the urls of each game to get the description and the genres. The total number of rows of description collected was 122,857. After removing duplicates or null datas from the list the final size of the dataset contained 91,184 rows.
Since many games are released on multiple platforms I removed any duplicates of description. Some games have different versions on different platforms that's why I didn't remove duplicates based on game title.
The codes used are given in the codes folder with comments explaining their use cases.

# Trainig the model
The model was trainined using the help of huggingface/fastAI. We used bert-base-uncased because it was one of the most used models and also effective. Bert large model had a very high system requirement but the base model was fast and less resource intensive. After training the model we used onnx to convert the model into smaller size and into more efficient version. 

# Model deployment
The model was deployed on huggingface and the model API was conencted to a website which set up on render to get a more customized and user friendly look. The render website was set up using flask. See the deployment here.

# Building and running the source code
1. Download the repository on your pc using the following command. git clone https://github.com/
2. go to the repository directory and run the following command in the terminal. Pip install -r requirements.txt
3. activate the virtual environment by running 'venv/scripts/activate'
4. Open jupyter notebook by running the following command 'jupyter notebook'
5. Navigate to the codes folder and run the notebooks serially as per their given name. Further instructions are given in the comments of each notebook.

# Note
1. Data scraping takes a very long time.
2. The picture used on the render website was made using DALL-E-2
3. Model training was done on colab. The rest of the code was run on local pc.