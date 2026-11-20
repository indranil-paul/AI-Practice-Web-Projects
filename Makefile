SHELL := /bin/bash
.ONESHELL:

# ==========================================================
# FastAPI Project Makefile
#
# Author		: Indranil Paul
# Description	: Creates a production-ready FastAPI project
# Date			: 2024-06-01
# Usage			:
#     `make`       -> Create project structure
#     `make help`  -> Show help
#     `make clean` -> Remove project files & folders. [ NOTE: This will delete the entire project structure. So, use it with caution! ]
#
# Here is the generated project structure:
#
#├── app
#│   ├── api
#│   │   ├── router.py
#│   │   └── urls.py
#│   ├── core
#│   │   ├── config.py
#│   │   └── constants.py
#│   ├── exceptions
#│   │   └── handlers.py
#│   ├── main.py
#│   ├── models
#│   │   └── models.py
#│   ├── prompts
#│   ├── services
#│   ├── tests
#│   └── utils
#│       ├── logger.py
#│       └── utils.py
#├── Makefile
#├── README.md
#├── requirements.txt
#├── run.py
#└── setup.sh
# =========================================================


.PHONY: all setup create_dirs create_files run clean help

# ------------------------------------------------------------------
# Variables
# ------------------------------------------------------------------
ALLOW_CLEAN:= 0 # Set to 1 to allow cleaning the project structure. Use with caution!

VENV_NAME := .venv

PYTHON_VERSION := 3.14.5

APP_NAME := app

DIRS := \
	app \
	app/api \
	app/core \
	app/models \
	app/services \
	app/prompts \
	app/utils \
	app/exceptions \
	app/tests

FILES := \
	app/main.py \
	app/api/router.py \
	app/api/urls.py \
	app/core/config.py \
	app/core/constants.py \
	app/models/models.py \
	app/utils/logger.py \
	app/utils/utils.py \
	app/exceptions/handlers.py \
	run.py \
	setup.sh \
	requirements.txt \
	README.md \
	.gitignore \
	.env

# ------------------------------------------------------------------
# Default Target
# ------------------------------------------------------------------
all: setup

# ------------------------------------------------------------------
# Help
# ------------------------------------------------------------------
help:
	@printf "\n"
	@printf "======================================================\n"
	@printf "             FastAPI Project Generator\n"
	@printf "======================================================\n\n"
	@printf "Targets:\n\n"
	@printf "  make            Create project scaffold\n"
	@printf "  make setup      Create project scaffold\n"
	@printf "  make clean      Remove generated files\n"
	@printf "  make help       Show this help\n\n"

# ------------------------------------------------------------------
# Setup
# ------------------------------------------------------------------
setup: banner create_dirs create_files setup_files

	@printf "======================================================\n"
	@printf "\nProject scaffold created successfully!\n"
	@printf "\nNext steps:\n"
	@printf "  1. Run: ./setup.sh\n"
	@printf "  2. Activate the virtual environment: source $(VENV_NAME)/bin/activate\n"
	@printf "  3. Run the application: python run.py\n"
	@printf "\n======================================================\n\n"

# ------------------------------------------------------------------
# Banner
# ------------------------------------------------------------------
banner:
	@printf "\n"
	@printf "======================================================\n"
	@printf "         FastAPI Project Template Generator\n"
	@printf "======================================================\n"

# ------------------------------------------------------------------
# Create Directories
# ------------------------------------------------------------------
create_dirs:
	@printf "\n[INFO] Creating project directories...\n\n"
	@for dirname in $(DIRS); do \
		mkdir -p $$dirname; \
		printf "[OK]   %s\n" "$$dirname"; \
	done

# ------------------------------------------------------------------
# Create Files
# ------------------------------------------------------------------
create_files:
	@printf "\n[INFO] Creating initial project files...\n\n"
	@for filename in $(FILES); do \
		touch $$filename; \
		printf "[OK]   %s\n" "$$filename"; \
	done

# ------------------------------------------------------------------
# Setup Files
# ------------------------------------------------------------------
setup_files: requirements setup_script gitignore readme sample_code

# ------------------------------------------------------------------
# Requirements
# ------------------------------------------------------------------
requirements:
	@printf "\n[INFO] Generating requirements.txt...\n"

	@printf "%s\n" \
	"fastapi" \
	"uvicorn[standard]" \
	"openai" \
	"httpx" \
	"python-dotenv" \
	"pydantic" \
	"pydantic-settings" \
	"python-multipart" \
	"google-genai" \
	"streamlit" \
	"requests" \
	> requirements.txt

	@printf "[OK] requirements.txt created.\n\n"

# ------------------------------------------------------------------
# Setup Script
# ------------------------------------------------------------------
setup_script:
	@printf "[INFO] Generating setup.sh...\n"

	@printf "%s\n" \
	"#!/bin/bash" \
	"" \
	"set -e" \
	"" \
	"PYTHON_VERSION=\"$(PYTHON_VERSION)\"" \
	"VENV_NAME=\"$(VENV_NAME)\"" \
	"" \
	"echo" \
	"echo \"===========================================\"" \
	"echo \"        FastAPI Project Setup\"" \
	"echo \"===========================================\"" \
	"echo" \
	"" \
	"if command -v pyenv >/dev/null 2>&1; then" \
	"    echo \"Installing Python \$${PYTHON_VERSION} (if needed)...\"" \
	"    pyenv install -s \$${PYTHON_VERSION}" \
	"    pyenv local \$${PYTHON_VERSION}" \
	"fi" \
	"" \
	"echo" \
	"echo \"Creating virtual environment...\"" \
	"python -m venv \$${VENV_NAME}" \
	"" \
	"echo" \
	"echo \"Activating virtual environment...\"" \
	"source \$${VENV_NAME}/bin/activate" \
	"" \
	"echo" \
	"echo \"Upgrading pip...\"" \
	"python -m pip install --upgrade pip" \
	"" \
	"echo" \
	"echo \"Installing packages...\"" \
	"pip install -r requirements.txt" \
	"" \
	"echo" \
	"echo \"===========================================\"" \
	"echo \"        Setup Completed Successfully\"" \
	"echo \"===========================================\"" \
	"echo" \
	"echo \"Activate the virtual environment using: source \$${VENV_NAME}/bin/activate\"" \
	"echo" \
	> setup.sh

	@chmod +x setup.sh
	@printf "[OK]   setup.sh created.\n\n"

# ------------------------------------------------------------------
# Gitignore
# ------------------------------------------------------------------
gitignore:
	@printf "[INFO] Generating .gitignore...\n"

	@printf "%s\n" \
	"# Python" \
	"__pycache__/" \
	"*.py[cod]" \
	"" \
	"# Virtual Environment" \
	".venv/" \
	"venv/" \
	"" \
	"# Environment Variables" \
	".env" \
	"" \
	"# macOS" \
	".DS_Store" \
	"" \
	"# IDE" \
	".idea/" \
	".vscode/" \
	"" \
	"# Testing" \
	".pytest_cache/" \
	".mypy_cache/" \
	".ruff_cache/" \
	> .gitignore

	@printf "[OK]   .gitignore created.\n\n"

# ------------------------------------------------------------------
# Readme
# ------------------------------------------------------------------
readme:
	@printf "[INFO] Generating README.md...\n"

	@printf "%s\n" \
	"# FastAPI AI Project Template" \
	"" \
	"Production-ready FastAPI project scaffold generated using the Makefile." \
	> README.md

	@printf "[OK]   README.md created.\n\n"

# ------------------------------------------------------------------
# Sample Code
# ------------------------------------------------------------------
sample_code:
	@printf "[INFO] Generating sample FastAPI code...\n"

	@printf "%s\n" \
	'from enum import StrEnum' \
	'from pydantic import BaseModel' \
	'' \
	'' \
	'# The Slugs enum defines the API endpoint slugs for the chatbot application.' \
	'class Slugs(StrEnum):' \
	'    HEALTH = "/health"' \
	'' \
	'# The RouteInfo dataclass holds metadata for each API route, including the slug, summary, description, and tag.' \
	'class RouteInfo:' \
	'    slug: str' \
	'    summary: str' \
	'    description: str' \
	'    tag: str' \
	'' \
	'' \
	'# Routes dictionary mapping Slugs to RouteInfo' \
	'ROUTES: dict[Slugs, RouteInfo] = {' \
	'    Slugs.HEALTH: RouteInfo(' \
	'        slug=Slugs.HEALTH, summary="Health Check", description="Health check endpoint to verify API status.", tag="Health"' \
	'    ),' \
	'}' \
	> app/api/router.py

	@printf "[OK]   app/api/router.py\n"


	@printf "%s\n" \
	'from fastapi import APIRouter, HTTPException' \
	'from app.core.config import settings' \
	'from app.api.router import ROUTES, Slugs' \
	'' \
	'' \
	'router = APIRouter()' \
	'' \
	'' \
	'@router.post(path=ROUTES[Slugs.HEALTH].slug, tags=[ROUTES[Slugs.HEALTH].tag])' \
	'def health_check():' \
	'    if not settings.OPENROUTER_API_KEY or not settings.OPENROUTER_BASE_URL:' \
	'        raise HTTPException(status_code=500, detail="API key or base URL not configured.")' \
	'' \
	'    return {"status": "ok"}' \
	> app/api/urls.py

	@printf "[OK]   app/api/urls.py\n"


	@printf "%s\n" \
	'from fastapi import FastAPI' \
	'from app.api.router import router' \
	'' \
	'application = FastAPI(title="$(APP_NAME)", version="1.0.0")' \
	'' \
	'application.include_router(router=router)' \
	> app/main.py

	@printf "[OK]   app/main.py\n"


	@printf "%s\n" \
	'import os' \
	'from dotenv import load_dotenv' \
	'from app.core.constants import ENV_VAR_APIKEY, ENV_VAR_BASEURL' \
	'' \
	'' \
	'load_dotenv()' \
	'' \
	'' \
	'class Settings:' \
	'    OPENROUTER_API_KEY: str = os.environ.get(ENV_VAR_APIKEY, "")' \
	'    OPENROUTER_BASE_URL: str = os.environ.get(ENV_VAR_BASEURL, "")' \
	'' \
	'    def validate(self):' \
	'        if not self.OPENROUTER_API_KEY:' \
	'            raise ValueError("OPENROUTER_API_KEY is missing!")' \
	'        if not self.OPENROUTER_BASE_URL:' \
	'            raise ValueError("OPENROUTER_BASE_URL is missing!")' \
	'' \
	'' \
	'settings = Settings()' \
	> app/core/config.py

	@printf "[OK]   app/core/config.py\n"


	@printf "%s\n" \
	'' \
	'' \
	'ENV_VAR_APIKEY = "OPENROUTER_API_KEY"' \
	'ENV_VAR_BASEURL = "OPENROUTER_BASE_URL"' \
	'' \
	> app/core/constants.py

	@printf "[OK]   app/core/config.py\n"


	@printf "%s\n" \
	'import uvicorn' \
	'' \
	'if __name__ == "__main__":' \
	'    uvicorn.run(' \
	'        app="$(APP_NAME).main:application",' \
	'        host="0.0.0.0",' \
	'        port=8000,' \
	'        reload=True,' \
	'        workers=1,' \
	'        log_level="info"' \
	'    )' \
	> run.py

	@printf "[OK]   run.py\n\n"

# ------------------------------------------------------------------
# Clean Up
# ------------------------------------------------------------------
clean:
	@if [ "$(ALLOW_CLEAN)" != "1" ]; then \
		printf "\n======================================================\n"; \
		printf "                * * * BLOCKED * * * \n"; \
		printf "======================================================\n\n"; \
		printf "[SAFETY] The 'clean' target is disabled to prevent accidental deletion.\n"; \
		printf "[SAFETY] If you are absolutely sure, then run:\n\n"; \
		printf "         make clean ALLOW_CLEAN=1\n\n"; \
		exit 1; \
	fi
	@{ \
		printf "\n======================================================\n"; \
		printf "                * * * WARNING * * * \n"; \
		printf "======================================================\n\n"; \
		printf "This will permanently delete the generated project. Continue? [y/N]: "; \
		read answer; \
		if [ "$$answer" = "y" ] || [ "$$answer" = "Y" ]; then \
			printf "\nCleaning project...\n\n"; \
			rm -rf $(APP_NAME); \
			printf "[OK]   Removed $(APP_NAME)\n"; \
			rm -f run.py setup.sh requirements.txt README.md .gitignore .env .python-version; \
			printf "[OK]   Removed project files\n"; \
			rm -rf $(VENV_NAME); \
			printf "[OK]   Removed environment file $(VENV_NAME)\n"; \
			rm -rf .pytest_cache .mypy_cache .ruff_cache; \
			printf "[OK]   Removed cache files\n"; \
			printf "\n[INFO] Cleanup completed successfully.\n\n"; \
		else \
			printf "\nOperation cancelled.\n\n"; \
		fi; \
	}

# ------------------------------------------------------------------
# End of Makefile
# ------------------------------------------------------------------
