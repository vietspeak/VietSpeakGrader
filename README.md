# VietSpeakOJ
A module that gives pronunciation score based on the audio transcript produced by Kaldi/Slack and the model transcript. Powered by the Carnegie Mellon University Pronouncing Dictionary and VOSK API

## Development installation
```
python3 -m venv env
source env/bin/activate
pip3 install black isort pytest pytest-cov sqlalchemy wheel gunicorn flask vosk slack_bolt scikit-learn aiohttp selenium webdriver-manager
sudo apt-get install ffmpeg unzip
mkdir database
mkdir tmp
mkdir firefox_drivers
tar -xzf geckodriver-v0.32.0-linux64.tar.gz -C firefox_drivers
python3 installer.py
```

Add the following lines to the end of your `~/.bashrc` file
```
export SLACK_BOT_TOKEN=<your Slack bot token>
export SLACK_SIGNING_SECRET=<your Slack signing secret>
export PORT=<port>
```

Run the following command
```
. ~/.bashrc
```

Download a model from https://alphacephei.com/vosk/models, and unzip the model. Then, rename the new folder `vosk_model`
## Testing
```
coverage run -m pytest tests && coverage report --show-missing
```
## Deployment
```
sudo ufw allow $PORT
gunicorn --bind 0.0.0.0:$PORT wsgi:flask_app
```
