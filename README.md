---------------
API Comentários
--------------- 

#### Passos a seguir:

A configuração necessária será feita a partir do arquivo Makefile com o comando `make target_label`, onde `target_label` é um alvo presente no arquivo a ser executado.

1. Instale as dependências do python para o projeto com o comando abaixo:

	```
	$ make setup
	```

2. Levanta o servidor local. _(Porta: 8001)_:

	```
	$ make run
	```

3. Este item é opcional. Caso queira testar as operações do seu código, execute o comando abaixo:

	```
	$ make test
	```

4. Este item é opcional. Caso queira ver possíveis erros encontrados fora do padrão do código Python, execute o comando abaixo:

	```
	$ make pep8
	```

5. Este item é opcional. Caso queira ver o total de possíveis erros encontrados fora do padrão do código Python, execute o comando abaixo:

	```
	$ make pep8-total
	```
