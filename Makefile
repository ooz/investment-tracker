all: track

track:
	pipenv run python3 tracker.py

install_pipenv:
	pip3 install pipenv

init:
	pipenv --python 3
	pipenv install

publish: all
	git commit -am "Update by CircleCI `date` [skip ci]" || true
	git push

# Cleanup
clean_vscode:
	rm -rf .vscode

clean: clean_vscode

.PHONY: track \
install_pipenv init \
clean_vscode
