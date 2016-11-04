setup:
	pip install -r requirements.txt

run:
	python app/comentario.py

test:
	python app/tests.py

pep8:
	@pep8 --ignore=E501 .

pep8-total:
	@pep8 --ignore=E501 . | wc -l