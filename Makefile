run-db:
	docker run --name crehana_postgres -p 5432:5432 -e POSTGRES_PASSWORD=password -e POSTGRES_DB=crehana -v ${PWD}/db_data:/var/lib/postgresql/data -d postgres
