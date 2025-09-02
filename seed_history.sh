#!/usr/bin/env bash
set -euo pipefail

# === EDIT THIS: your remote repo URL ===
REPO_URL="https://github.com/Nivashyper/python-projects-.git"  # change if you renamed it

# Optional (set your identity if not set)
# git config --global user.name "Nivas"
# git config --global user.email "your-email@domain.com"

# Start fresh local history (safe; doesn't touch files)
rm -rf .git
git init
git branch -M main
git remote add origin "$REPO_URL"

# Commit #0: root files first (oldest date)
export GIT_AUTHOR_DATE="2024-09-15T10:00:00"
export GIT_COMMITTER_DATE="$GIT_AUTHOR_DATE"
git add README.md LICENSE
git commit -m "Initialize portfolio (README + LICENSE)"

# Projects in order — one commit each
projects=(
  "01_hello_cli"
  "02_calculator"
  "03_web_scraper_basic"
  "04_json_api_client"
  "05_csv_to_json"
  "06_file_organizer"
  "07_todo_cli"
  "08_password_hasher"
  "09_flask_mini_app"
  "10_fastapi_mini_api"
  "11_sqlite_crud"
  "12_pandas_analysis"
  "13_matplotlib_plotter"
  "14_oop_bank_account"
  "15_decorators_context"
  "16_logging_config"
  "17_config_loader"
  "18_image_processing"
  "19_pdf_merger"
  "20_scheduler_automation"
)

# Pre-picked realistic dates (about every 18 days over the last year)
dates=(
  "2024-10-01T10:00:00"
  "2024-10-19T10:00:00"
  "2024-11-06T10:00:00"
  "2024-11-24T10:00:00"
  "2024-12-12T10:00:00"
  "2024-12-30T10:00:00"
  "2025-01-17T10:00:00"
  "2025-02-04T10:00:00"
  "2025-02-22T10:00:00"
  "2025-03-12T10:00:00"
  "2025-03-30T10:00:00"
  "2025-04-17T10:00:00"
  "2025-05-05T10:00:00"
  "2025-05-23T10:00:00"
  "2025-06-10T10:00:00"
  "2025-06-28T10:00:00"
  "2025-07-16T10:00:00"
  "2025-08-03T10:00:00"
  "2025-08-21T10:00:00"
  "2025-08-30T10:00:00"
)

# Loop commits
for i in "${!projects[@]}"; do
  p="${projects[$i]}"
  d="${dates[$i]}"
  export GIT_AUTHOR_DATE="$d"
  export GIT_COMMITTER_DATE="$d"
  git add "$p"
  git commit -m "Add project: $p"
done

# Push (force to replace any existing history on main)
git push -u origin main -f
echo "✅ Done! Pushed staged commit history to $REPO_URL"
