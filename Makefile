.PHONY: help install build start clean serve convert-figures

BOOK_DIR = book
BUILD_DIR = $(BOOK_DIR)/_build

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Create mamba environment from environment.yml
	mamba env create -f environment.yml --yes
	@echo ""
	@echo "Environment created. Activate with:"
	@echo "  mamba activate ess-jbook"

build: ## Build the book (static HTML)
	cd $(BOOK_DIR) && jupyter book build

build-execute: ## Build the book with notebook execution
	cd $(BOOK_DIR) && jupyter book build --execute

start: ## Start local dev server with live reload and notebook execution
	cd $(BOOK_DIR) && jupyter book start --execute

clean: ## Remove build artifacts
	cd $(BOOK_DIR) && jupyter book clean
	rm -rf $(BUILD_DIR)

serve: build ## Build then serve with Python HTTP server
	@echo "Serving at http://localhost:8000"
	@echo "Press Ctrl+C to stop"
	python -m http.server 8000 --directory $(BUILD_DIR)/site

convert-figures: ## Convert EPS figures to PNG/SVG
	python scripts/convert_figures.py
