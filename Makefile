SHELL=/bin/bash


default:
	echo Setup, Run or Clean?
setup:
	python3 -m venv make-activtiy2
	source ./make-activtiy2/bin/activate;\
	pip3 install -r requirements.txt
	printf "#!/bin/bash\n./scripts/pre-commit.py" >.git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit
run:
	source ./make-activtiy2/bin/activate;\
	env FLASK_APP=hello.py flask run
clean:
	rm -rf make-activtiy2
	py3clean .

