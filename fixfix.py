#!/usr/bin/env bash

set -e

# === CONFIG ===

# All your desired SHAs (original ones, for labels only)
SHAS=(
  "bbe5a0c1e99c6d3b6317f62306dfb486bb4a6156"
  "3a5cd0690125f0c240de19e845ecbbfb864779b8"
  "a89134439caae6e765914273b488fe47efc0dfe5"
  "c980684c7e0b0ddaa3486528c03450dbc2645380"
  "d0137ce3b1eaca1d374921b60e222551a747b35b"
  "8f9f21fc68abf4b5c7c8985088000beed6e0b83f"
  "44baa8cd17bb81719d4144e549305d88b27a44a0"
  "9c2e71f9f9c748bfeefb56c50ce901e32e9fd642"
  "56edf7fdc4c0fcae630b2d4dfc2fab0a2b29e460"
  "d98c3f7be167b8ec2d35bdd2144cd04b27d2689f"
  "dbaaeeab50c0cf7f2493e1cccbe083d497da1289"
  "b3d963b4a13105f49778731ea85004a262523f5a"
  "43c8ed02436d81437923ffa7a3e32ad25b8602ae"
  "e6eaf3b0c880e325150a26fb51306e711b1daf75"
  "dcd24ac312e5f832b76bb342c91a8d50dc8d172c"
  "647dcf992e488076ccb7b5f002693aa9ebec4bde"
  "4323eed39bd5c2b1dfd2725727a684f4c684b144"
  "2afa3ab58cb60f409e75d605f8b0fb110a64dbf0"
)

# Corresponding desired dates
DATES=(
  "2023-09-18 07:12:00 +0530"
  "2023-09-19 13:54:00 +0530"
  "2023-09-20 10:01:00 +0530"
  "2023-09-20 14:30:40 +0530"
  "2023-09-20 21:48:10 +0530"
  "2023-09-21 09:30:00 +0530"
  "2023-09-21 10:45:18 +0530"
  "2023-09-21 17:10:10 +0530"
  "2023-09-21 18:12:00 +0530"
  "2023-09-21 20:38:10 +0530"
  "2023-09-22 11:15:17 +0530"
  "2023-09-22 12:10:00 +0530"
  "2023-09-22 20:15:00 +0530"
  "2023-09-24 23:15:17 +0530"
  "2023-09-24 11:37:00 +0530"
  "2023-09-25 10:51:30 +0530"
  "2023-09-26 10:10:10 +0530"
  "2023-09-28 14:30:12 +0530"
)

# === START ===

echo ">>> Creating new branch 'main-rewritten'"
git checkout --orphan main-rewritten

# Clean any existing files (in case orphan still has old working dir)
git rm -rf . > /dev/null 2>&1 || true

# === Apply each snapshot ===

for i in "${!SHAS[@]}"; do
  SHA="${SHAS[$i]}"
  DATE="${DATES[$i]}"

  echo
  echo ">>> Replaying $SHA at $DATE"

  # Force clean state to ensure exact snapshot
  git rm -rf . > /dev/null 2>&1 || true
  git checkout "$SHA" -- .
  git add .

  # Commit with rewritten author + committer date
  GIT_AUTHOR_DATE="$DATE" GIT_COMMITTER_DATE="$DATE" git commit -m "$SHA"
done

echo
echo "✅ All commits rewritten on branch 'main-rewritten'."
echo "👉 To replace remote 'main':"
echo "   git branch -M main"
echo "   git push --force origin main"
