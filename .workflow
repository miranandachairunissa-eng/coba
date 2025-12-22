name: Preprocessing Automation

on:
  push:
    branches: [ main ] # Berjalan saat ada push ke branch main

jobs:
  run-preprocessing:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: pip install pandas
      - name: Run automate script
        run: python preprocessing/automate_mirananda.py
      - name: Commit and Push
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
          git add .
          git commit -m "Automated update: Preprocessed data" || echo "No changes"
          git push
