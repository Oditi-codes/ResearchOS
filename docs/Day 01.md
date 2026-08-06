# ResearchOS – Day 01

**Date:** 06 August 2026

---

# Objective

Today's objective was **not** to build any functionality for ResearchOS.

Instead, today's focus was on:

- Setting up the project structure.
- Learning Git fundamentals.
- Connecting the local repository to GitHub.
- Understanding *why* each Git command exists instead of simply executing it.

---

# Part 1 — Creating the Project

## 1. Move to the parent directory

```powershell
cd <directory path>
```

---

## 2. Create the project folder

```powershell
mkdir ResearchOS
```

---

## 3. Move inside the project

```powershell
cd ResearchOS
```

---

## 4. Verify the Current Working Directory (CWD)

```powershell
pwd
```

Output:

```
D:\Resume_Projects\ResearchOS
```

The Current Working Directory is now:

```
ResearchOS
```

Every command I execute from now on runs relative to this folder.

---

## 5. Create the initial folder structure

```powershell
mkdir frontend
mkdir backend
mkdir assets
mkdir docs
```

---

## 6. Verify the folders

```powershell
dir
```

Displays all folders inside the Current Working Directory.

---

## 7. Open the project in VS Code

```powershell
code .
```

`.` represents the Current Working Directory.

---

## 8. Create the initial files

Created:

- README.md
- .gitignore

Added:

```
.env
```

to `.gitignore` because API keys, secrets and other environment variables should never be uploaded to GitHub.

---

# Part 2 — Initializing Git

---

## 9. Initialize Git

```powershell
git init
```

Result:

Git created the hidden `.git` directory.

This directory stores the complete Git repository.

---

## 10. Check repository status

```powershell
git status
```

Shows the current state of the repository.

Initially the project files appeared as **Untracked**.

---

## 11. Stage all files

```powershell
git add .
```

This copies snapshots of every file into the **Staging Area**.

Nothing is committed yet.

---

## 12. Verify staging

```powershell
git status
```

README.md and .gitignore now appeared under:

```
Changes to be committed
```

confirming they had been successfully staged.

---

## 13. Attempt the first commit

```powershell
git commit -m "Initial project structure"
```

Git refused because my Git identity (username and email) had not yet been configured.

---

## 14. Configure Git identity

```powershell
git config --global user.email "<my_github_email>"
git config --global user.name "Oditi"
```

---

## 15. Create the first commit

```powershell
git commit -m "Initial project structure"
```

Successfully created the **Root Commit** of the repository.

---

# Part 3 — Understanding the Staging Area

Rather than moving ahead immediately, I wanted to understand **what actually happens if a file is modified after staging but before committing.**

---

### Experiment

Added:

```
Line A
```

to README.md

Executed:

```powershell
git add README.md
git status
```

Result:

The current version of README.md was copied into the Staging Area.

---

Next,

I added:

```
Line B
```

to README.md

without running `git add` again.

Executed:

```powershell
git status
```

Result:

README.md appeared as:

```
modified
```

Reason:

The Working Directory now contained:

```
Line A
Line B
```

whereas the Staging Area still contained the earlier snapshot:

```
Line A
```

This helped me understand one of Git's most important concepts:

> Git commits whatever is inside the **Staging Area**, not whatever currently exists inside the Working Directory.

The Staging Area stores a **snapshot**, not a live version of the file.

---

### Restoring the experiment

Removed both experimental lines.

Executed:

```powershell
git add README.md
git status
```

Output:

```
On branch main

nothing to commit, working tree clean
```

Meaning:

The Working Directory, Staging Area and Repository all now contained exactly the same version.

---

# Part 4 — Creating the GitHub Repository

Logged into GitHub.

Created a new repository named:

```
ResearchOS
```

Settings used:

- Public
- No README
- No .gitignore
- No License

### Why?

Because my local repository already contained the initial commit.

If GitHub also created a README, it would create another independent Root Commit, leading to unrelated histories during the first push.

---

GitHub then suggested these commands:

```powershell
git remote add origin https://github.com/Oditi-codes/ResearchOS.git
git branch -M main
git push -u origin main
```

Instead of blindly executing them, I decided to understand each one first.

---

# Part 5 — Connecting GitHub

---

## 16. Add the remote repository

```powershell
git remote add origin https://github.com/Oditi-codes/ResearchOS.git
```

Purpose:

Create a remote reference named:

```
origin
```

that points to my GitHub repository.

This command does **not** upload anything.

Internally it creates an entry inside:

```
.git/config
```

Example:

```ini
[remote "origin"]
url = https://github.com/Oditi-codes/ResearchOS.git
fetch = +refs/heads/*:refs/remotes/origin/*
```

---

## 17. Verify the remote

```powershell
git remote -v
```

Displays the configured Fetch and Push URLs.

---

## 18. Verify Git's metadata directory

```powershell
git rev-parse --git-dir
```

Output:

```
.git
```

This command tells Git to print the location of its metadata directory.

It does **not** reveal hidden folders.

Think of it as Git answering:

> "Where is your repository database?"

---

## 19. Display hidden folders

```powershell
dir -Force
```

Confirmed that:

```
.git
```

exists inside the project.

---

## 20. Verify the current branch

```powershell
git branch
```

Output:

```
* main
```

Since my current branch was already named `main`, I **did not** execute:

```powershell
git branch -M main
```

### Note to self

`-m`

Rename a branch.

`-M`

Force rename a branch, even if Git would normally prevent it.

---

## 21. Push the project to GitHub

```powershell
git push -u origin main
```

Meaning:

- `-u` → Creates an upstream tracking relationship.
- `origin` → Name of the remote GitHub repository.
- `main` → Local branch being pushed.

Result:

The project was successfully uploaded to GitHub.

---

# Today's Biggest Learnings

- Git is not GitHub.
- Git commits the **Staging Area**, not the Working Directory.
- `git add` creates snapshots.
- The Staging Area does not update automatically after editing a file.
- `origin` is simply an alias.
- A Remote is just another Git repository.
- `.git` stores the repository database.
- `git remote add` only creates a connection; it does not upload files.
- Professional engineers understand commands before executing them.

---

# Personal Reflection

Although I did not write any application code today, I laid the foundation for the entire ResearchOS project.

More importantly, instead of memorizing Git commands, I focused on understanding what each command does internally, why it exists, and what problem it solves. This approach should make future Git concepts easier to learn and help me explain them confidently during interviews.

---

# Questions I Asked Today

These are questions that came up naturally during today's learning. They reflect my thought process and will serve as quick revision prompts in the future.

1. Why didn't we have to run `git add` again after the failed `git commit`?
2. Why is `origin` just a conventional alias? Can it be named anything else?
3. Where does Git store the remote repository information?
4. Why couldn't I see the `.git` folder inside VS Code?
5. What does `git rev-parse --git-dir` actually do?
6. Why did GitHub ask me to sign in after running `git remote add origin ...`?
7. After signing into GitHub, should I run `git remote add origin ...` again?
8. Why was `git branch -M main` unnecessary in my case?
9. What exactly does `git push -u origin main` do internally?
10. Why did GitHub recommend creating the repository **without** a README, `.gitignore`, or License?

---

# Common Misconceptions Corrected Today

These are concepts I initially misunderstood or partially understood. Recording them will help avoid repeating the same mistakes.

### 1. Staging Area vs Working Directory

**Initial Thought**

Once a file is staged, Git keeps tracking every new modification automatically.

**Correct Understanding**

`git add` copies a **snapshot** of the file into the Staging Area. Any edits made afterward remain only in the Working Directory until `git add` is executed again.

---

### 2. Meaning of `origin`

**Initial Thought**

`origin` seemed like a special Git keyword.

**Correct Understanding**

`origin` is simply the conventional alias for a remote repository. It can be replaced with any valid name.

---

### 3. `git remote add`

**Initial Thought**

This command might upload the project to GitHub.

**Correct Understanding**

`git remote add` only creates a reference to another Git repository by adding an entry to `.git/config`. No files are uploaded.

---

### 4. `git rev-parse --git-dir`

**Initial Thought**

This command displays hidden Git folders.

**Correct Understanding**

It simply tells Git to print the path of its metadata directory (usually `.git`). It does **not** reveal hidden folders.

---

### 5. GitHub Authentication

**Initial Thought**

After signing into GitHub through VS Code, I might need to run `git remote add origin` again.

**Correct Understanding**

Authentication and remote configuration are two separate things. The remote had already been configured successfully; signing in only authorized future communication with GitHub.

---

### 6. `git branch -M main`

**Initial Thought**

GitHub suggested the command, so I should always execute it.

**Correct Understanding**

My current branch was already named `main`, so renaming was unnecessary. It is always better to inspect the current state before executing commands.

---

### 7. Meaning of `-u` in `git push -u origin main`

**Initial Thought**

I thought `-u` meant "upperstate".

**Correct Understanding**

`-u` stands for `--set-upstream`. It establishes an upstream tracking relationship between the local branch (`main`) and the remote branch (`origin/main`), allowing future `git push` and `git pull` commands to omit the remote and branch names.

---

# Key Takeaways

Today's biggest lesson was not learning Git commands—it was learning how Git **thinks**.

Instead of memorizing commands, I now understand:
- the difference between the Working Directory, Staging Area, and Repository,
- why Git uses snapshots,
- how a local repository connects to a remote repository,
- and why experienced engineers inspect the current state before executing commands instead of blindly following documentation.