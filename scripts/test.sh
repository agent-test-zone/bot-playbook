#!/bin/sh
# Runs every sample project's tests from the repository root. No dependencies to install.
set -e
cd "$(dirname "$0")/.."
python3 -m unittest discover -s inventory -t . -v
(cd textkit && node --test)
