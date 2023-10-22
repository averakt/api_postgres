#!/usr/bin/env bash

alembic upgrade head

export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d minibank -f fund.sql

exit 0