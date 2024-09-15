# Python Projects Portfolio

A curated set of small-to-medium Python projects (beginner → advanced) ready for GitHub.  
Each project is self-contained with its own README and (when needed) requirements.txt and tests.

## Quick Start

```bash
# (1) Create a repo on GitHub named python-projects-portfolio
# (2) On your machine:
git clone https://github.com/<your-username>/python-projects-portfolio.git
cd python-projects-portfolio

# (3) Copy these files into the repo folder, then:
git add .
git commit -m "Add multi-project Python portfolio"
git push origin main  # or master depending on your default branch
```

> Tip: Install per-project dependencies inside each subfolder:
```bash
cd 03_web_scraper_basic
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scraper.py
```

## Projects

1. 01_hello_cli – Simple CLI greeting with argparse.
2. 02_calculator – CLI calculator with unit tests.
3. 03_web_scraper_basic – Requests + BeautifulSoup scraper.
4. 04_json_api_client – Public API client with retry/backoff.
5. 05_csv_to_json – CSV → JSON converter.
6. 06_file_organizer – Sort files by extension into folders.
7. 07_todo_cli – Local JSON-backed TODO app.
8. 08_password_hasher – Hash + verify passwords (bcrypt).
9. 09_flask_mini_app – Minimal Flask web app.
10. 10_fastapi_mini_api – Minimal FastAPI with versioned routes.
11. 11_sqlite_crud – SQLite CRUD with context managers.
12. 12_pandas_analysis – Small EDA on a sample dataset.
13. 13_matplotlib_plotter – Generates a chart image.
14. 14_oop_bank_account – OOP example with tests.
15. 15_decorators_context – Decorators + context managers demo.
16. 16_logging_config – Structured logging best practices.
17. 17_config_loader – Typed settings via pydantic.
18. 18_image_processing – Basic Pillow operations.
19. 19_pdf_merger – Merge PDFs with pypdf.
20. 20_scheduler_automation – Simple task scheduler (cron-like loop).

All code is MIT-licensed.
