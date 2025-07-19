A complete all-in-one reference to essential Git commands - perfect for daily use, project col
Git Setup
git config --global user.name "Veena Kuruba"
git config --global user.email "your-email@example.com"
git config --global init.defaultBranch main
Start a Git Project
git init
git clone https://github.com/veenakuruba/your-repo-name.git
Git Basics
git add . # Stage all changes
git commit -m "Initial commit" # Save changes
git status
git diff git diff --staged # View unstaged changes
# View staged changes
Branching
git branch git branch feature-x git checkout feature-x git checkout -b feature-x git checkout main
git merge feature-x
# View all branches
# Create new branch
# Switch to branch
# Create + switch
Working with Remote Repositories
git remote add origin https://github.com/Veenakuruba/your-repo-name.git
git push -u origin main # Push main for the first time
git push # Push changes
git pull origin main # Pull updates
Undoing Changes
git reset filename git reset --soft HEAD~1 git reset --hard HEAD~1 # Unstage a file
# Undo last commit (keep changes)
# Undo last commit (discard changes)
Clean Untracked Files
git clean -fd # Force delete untracked files
View History
git log
git log --oneline --graph
Tags (Release Markers)
git tag v1.0
git tag -a v1.0 -m "Version 1.0 release"
git push origin v1.0
.gitignore Example
Git Commands Cheat Sheet - Veena Kuruba
*.pyc
__pycache__/
*.log
.DS_Store
node_modules/
Git Best Practices
- Commit small, meaningful changes.
- Pull often before pushing.
- Use feature branches, avoid pushing directly to main.
- Use .gitignore to keep the repo clean.
- Never commit secrets (API keys, passwords).
- Handle merge conflicts carefully.
Recommended Learning Resources
- GitHub Docs: https://docs.github.com/
- Git Book: https://git-scm.com/book/en/v2
- Git Cheatsheet: https://education.github.com/git-cheat-sheet-education.pdf
- Oh My Git! Game: https://ohmygit.org/
