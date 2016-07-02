install:
	@echo "Install"
	git clone 

test:
	@echo "Testing your installation for Cambridge Coding"
	@echo "Standby ..."
	python test.py
  
help:
	@echo "Commands"
	@echo "build"
	@echo "run"
	@echo "notebook"

notebook:
	@echo "Starting Jupyter notebook"
	cd machinelearningbootcamp && jupyter notebook

build:
	docker build -t CambridgeCode .

run:
	docker run -it -p 8888:8888 -t CambridgeCode .

all:
	@echo "Please run a command"

#.PHONY all