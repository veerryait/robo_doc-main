# RoboDoc
### Health Chatbot

How to run locally -

Requirements
- NodeJS Installed
- Python Installed
 ---
Running webapp locally

In bot_frontend\public\index.html remove /static before every path, then,
In the root folder of project, run
```sh
cd bot_frontend
npm i
npm run dev
```

This will start a local development server for the frontend app
After making your changes to the frontend app, to build the app, run the following commands

```sh
npm run build
```
then copy bot_frontend\public\build folder and replace static\build folder with it

To run the frontend with python backend, run

```sh
python server.py
```