#!/bin/bash

create_tables:
	mysql -uuser -puserpass --host=127.0.0.1 --port=3306 app_db < ./src/mysql/create_table.sql

run:
	python app.py

run_all:
	$(MAKE) create_tables
	$(MAKE) run
