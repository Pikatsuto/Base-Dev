all: start

VENV = venv
VBIN = $(VENV)/bin

$(VENV):
	python3 -m venv venv

	chmod +x $(VBIN)/activate
	./$(VBIN)/activate
	$(VBIN)/pip install -r requirements.txt
	$(VBIN)/pip install -e .

start: $(VENV)
	@echo "Starting base-dev"
	$(VBIN)/python base-dev

clean:
	rm -rf venv
	rm -rf base-dev/logs/.txt base-dev/errors/*.txt
	rm -rf *.-egg-info

.PHONY: all start clean
