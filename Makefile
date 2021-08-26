PYTHON=python
START=bot.py

help:
	@echo "-help-"
	@echo "make help - show help message"
	@echo "make run - run the bot"
	@echo "make setup - install dependencies"

run:
	@echo "-run-"
	${PYTHON} ${START}

setup:
	@echo "-setup-"
	${PYTHON} -m pip install -r requirements.txt