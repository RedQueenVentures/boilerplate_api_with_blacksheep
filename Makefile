MAKEFLAGS += --no-builtin-rules

###################################################
# API AND STARTUP
###################################################

api-start-local:
	@docker compose run api uvicorn api.server:app --port 8080 --reload --log-level info

# Sets up the api and db docker containers
setup-containers:
	@docker compose --profile dev up -d

###################################################
# DB AND MIGRATIONS
###################################################
