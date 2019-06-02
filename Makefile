PROJECT = enigma_rsa 
VIRTUAL_ENV = env

install: virtual download_and_activate prepare


virtual:
	@echo "--> Setup and activate virtualenv"
	if test -d "$(VIRTUAL_ENV)"; then \
		rm -rf $(VIRTUAL_ENV); \
	fi
	if test ! -d "$(VIRTUAL_ENV)"; then \
		pip3 install virtualenv; \
		virtualenv -p python3 $(VIRTUAL_ENV); \
	fi
	@echo ""

download_and_activate:
	@echo "-->Activating virtual environment"
	if test -d "$(VIRTUAL_ENV)"; then \
		. ./$(VIRTUAL_ENV)/bin/activate; \
		pip3 install -r requirements.txt; \
	fi
	@echo "Now type 'source ./env/bin/activate'"

prepare:
	@echo "Preparing chat environment"
	if test -d "$(VIRTUAL_ENV)"; then \
		. ./$(VIRTUAL_ENV)/bin/activate; \
		python3 ./chat_files/main.py; \
	fi
