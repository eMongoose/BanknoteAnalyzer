
# Coin Analyzer Setup Guide
Requirements: Python, Flask, NodeJS (with the npm package installed)

---

### 1. Download Dataset
1. Download and extract dataset samples from [here](https://www.kaggle.com/datasets/sergiosaharovskiy/uscoins)
2. Move samples into `Dataset/` folder. Further details for file structure are included in the folder's [README.md](Dataset/README.md)

### 2. Training the model

1. Run command `python train_model.py` from main directory

There are 2 options to running the coin analyzer locally after the model is trained:

## Option 1: Predict images using the console

This option allows for CLI image analyzation. This option can be run directly from the console.

### 3. Pass image to model through CLI

1. Run command:

```
python main.py [image path]
```

---

## Option 2: Run Coin Analyzer through web server

This option allows for GUI interaction with the app. This option requires more set up.

### 3. Start Python server

1. Install dependencies from `requirements.txt`:
```
pip install -r requirements.txt
```

3. From the main directory, run the command:

```
flask --app server run
``` 
### 4. Start Web App

1. In the main terminal, install the required packages:

```
npm install
```

2. After installing the packages, run the following command:

```
npx expo start
```
3. Follow console instructions to navigate to app web page

If you run into any error with the start command, try:

```
npx expo start -- tunnel
```
Try out the application! If you find that the analyze button does not work, you must run the ```server.py``` file.

---
## Option 3: Visit the website 

Since the program is also hosted externally, you can visit the website(s) and use the program yourself!

1. Start the server by visiting the [Render site](https://banknoteanalyzer-so7n.onrender.com/)

When you visit this link, it will take about 2-3 minutes for it to start up. Please do not leave the site. You will know it is ready when you see a single line:

```
Server Active
```

2. Interact with the program by visiting the [Vercel site](https://banknote-analyzer-mdym.vercel.app/)

