PYTHON=python
START=main.py
TRAIN=train.py

help:
	@echo "-help-"
	@echo "make help - show help message"
	@echo "make run - run the bot"
	@echo "make train - train the bot"
	@echo "make setup - install dependencies"

run:
	@echo "-run-"
	${PYTHON} ${START}

train:
	@echo "-train-"
	${PYTHON} ${TRAIN}

setup:
	@echo "-setup-"
	${PYTHON} -m pip install -r requirements.txt