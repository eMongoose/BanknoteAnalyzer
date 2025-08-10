
# Coin Analyzer Setup Guide
Requirements: NodeJS (with the npm package installed)

---
# Training the model

1. Run command `python train_model.py` from main directory

There are 2 options to running the coin analyzer after the model is trained:

## Option 1: Run Coin Analyzer through CLI

This option allows for CLI interaction with the app. This option can be run directly from the console.

1. Run command:

```
python main.py [image path]
```

## Option 2: Run Coin Analyzer through web server

This option allows for GUI interaction with the app. This option requires more set up.

1. Install dependencies from `requirements.txt`

2. From the main directory, run the command:

```
flask --app server run
``` 

---
# 3. Start Web UI

## Install the required packages

1. In the main terminal, run the following command:

```
npm install
```
## Start the Web UI

1. After installing the packages, run the following command:

```
npx expo start
```

If you run into any error with this command, try:

```
npx expo start -- tunnel
```

Try out the application! If you find that the analyze button does not work, you must run the ```server.py```file.
*Setup guide end*
---
# Visit the website 

Since the program is hosted externally, you can visit the website(s) and use the program yourself!

1. Start the server by visiting the [Render site](https://banknoteanalyzer-so7n.onrender.com/)

When you visit this link, it will take about 2-3 minutes for it to start up. Please do not leave the site. You will know it is ready when you see a single line:

```
Server Active
```

2. Interact with the program by visiting the [Vercel site](https://banknote-analyzer-mdym.vercel.app/)

