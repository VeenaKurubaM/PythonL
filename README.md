# This script installs Homebrew on macOS and sets up a basic environment.
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# install git
brew install git
# git version
git --version
# First commit
git remote add origin https://github.com/VeenaKurubaM/PythonL.git && git push -u origin main
# Update remote URL to the new repo name on GitHub
git remote set-url origin https://github.com/VeenaKurubaM/NEW-REPO-NAME.git


