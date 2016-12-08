COMENTARIO_MYSQL_DB_NAME := comentarios_blog
COMENTARIO_MYSQL_TABLE_NAME := comentarios

setup:
	pip install -r requirements.txt

run:
	python app/server.py

test:
	python app/tests.py

pep8:
	@pep8 --ignore=E501 .

pep8-total:
	@pep8 --ignore=E501 . | wc -l

db:
	mysql -u root -e 'CREATE DATABASE IF NOT EXISTS $(COMENTARIO_MYSQL_DB_NAME);'
	mysql -u root -e " \
	USE $(COMENTARIO_MYSQL_DB_NAME); \
	CREATE TABLE $(COMENTARIO_MYSQL_TABLE_NAME)( \
    	id INT(11) NOT NULL AUTO_INCREMENT, \
    	nome VARCHAR(20) NOT NULL, \
    	comentario LONGTEXT NOT NULL, \
    	data DATE NOT NULL, \
    	post_id INT(11) NOT NULL, \
    	PRIMARY KEY(id) \
    ); "
	@echo "DB e Table criados!"
