# Git Handbook

> A concise Git reference handbook built throughout the ResearchOS project.
>
> Purpose:
> - Quick revision
> - Understand Git instead of memorizing commands
> - Record concepts learned during the project

---

# Table of Contents

1. Git
2. Git vs GitHub
3. Repository
4. Current Working Directory (CWD)
5. Git Three-Tree Architecture
6. Working Directory
7. Staging Area
8. Root Commit
9. Remote Repository
10. origin
11. Branch
12. Upstream Tracking
13. Git Commands

---

# Git

## What is Git?

Git is a **Distributed Version Control System (DVCS)**.

It tracks changes by storing **snapshots** of files instead of overwriting previous versions.

---

## Why do we use Git?

- Maintain project history
- Undo mistakes
- Collaborate safely
- Work on multiple features simultaneously
- Manage different versions of the same project

---

# Git vs GitHub

| Git | GitHub |
|------|---------|
| Version Control System | Cloud platform for Git repositories |
| Installed locally | Runs on the cloud |
| Works offline | Requires internet |
| Tracks history | Collaboration platform |

> Git ≠ GitHub

---

# Repository

A repository is Git's database.

It stores:

- commits
- branches
- tags
- configuration
- Git objects
- complete project history

The repository is stored inside:

```
.git/
```

---

# Current Working Directory (CWD)

The directory where terminal commands are currently execute.

Useful command:

```powershell
pwd
```

Example Output

```
D:\Resume_Projects\ResearchOS
```

---

# Git Three-Tree Architecture

```
Working Directory
        │
        │ git add
        ▼
Staging Area
        │
        │ git commit
        ▼
Repository
```

**Remember**

Git commits the **Staging Area**, not the Working Directory.

---

# Working Directory

Contains the files currently being edited.

Changes here are not yet part of Git history.

---

# Staging Area

A temporary area that stores snapshots that will become the next commit.

### Why does it exist?

Allows developers to decide exactly which changes should be committed.

### Important

Running

```powershell
git add README.md
```

copies the current snapshot.

Future edits are **not** automatically staged.

---

# Root Commit

The first commit in a repository.

Every future commit ultimately traces back to the Root Commit.

---

# Remote Repository

A remote is another Git repository that the local repository knows how to communicate with.

Examples:

- GitHub
- GitLab
- Bitbucket
- Company Git Server

---

# origin

`origin` is **not** a Git keyword.

It is simply the conventional alias given to the primary remote repository.

Any valid name can be used.

---

# Branch

A branch is a movable pointer to a commit.

Example:

```
A → B → C
        ▲
        │
      main
```

A branch is **not** a copy of the project.

---

# Upstream Tracking

An upstream relationship tells Git which remote branch should be used by default.

Example:

```
Local main
      │
      ▼
origin/main
```

Once configured:

```powershell
git push
git pull
```

are sufficient.

---

# Git Commands

---

## git init

### Purpose

Initializes a Git repository.

### Syntax

```powershell
git init
```

### Internal Working

Creates the hidden `.git` directory.

### Expected Output

```
Initialized empty Git repository...
```

---

## git status

### Purpose

Displays the current repository status.

### Syntax

```powershell
git status
```

### Shows

- Current branch
- Staged files
- Modified files
- Untracked files

### Common Outputs

```
Changes to be committed
```

```
Changes not staged for commit
```

```
nothing to commit, working tree clean
```

---

## git add

### Purpose

Copies snapshots into the Staging Area.

### Syntax

```powershell
git add .
```

or

```powershell
git add <filename>
```

### Important

Git stages snapshots, not differences.

---

## git commit

### Purpose

Creates a commit from the Staging Area.

### Syntax

```powershell
git commit -m "Commit Message"
```

### Stores

- Snapshot
- Author
- Email
- Timestamp
- Commit Message

---

## git config

### Purpose

Configures Git settings.

### Syntax

```powershell
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

---

## git remote add

### Purpose

Adds a remote repository.

### Syntax

```powershell
git remote add origin <repository-url>
```

### Internal Working

Updates

```
.git/config
```

### Important

Does **not** upload anything.

---

## git remote -v

### Purpose

Displays configured remotes.

### Syntax

```powershell
git remote -v
```

### Expected Output

```
origin ...(fetch)
origin ...(push)
```

---

## git rev-parse --git-dir

### Purpose

Returns the location of Git's metadata directory.

### Syntax

```powershell
git rev-parse --git-dir
```

### Expected Output

```
.git
```

This command does **not** display hidden folders.

---

## git branch

### Purpose

Displays all local branches.

### Syntax

```powershell
git branch
```

### Expected Output

```
* main
```

`*` indicates the current branch.

---

## git push

### Purpose

Uploads commits to a remote repository.

### Syntax

```powershell
git push origin main
```

### Internal Working

- Contacts the remote repository
- Determines missing Git objects
- Compresses objects
- Transfers only the required objects
- Updates the remote branch

Git transfers Git objects—not simply project files.

---

## git push -u

### Purpose

Pushes the branch and creates an upstream tracking relationship.

### Syntax

```powershell
git push -u origin main
```

After the first push:

```powershell
git push
```

is sufficient.

---

# Common Mistakes

- Forgetting to stage files before committing.
- Thinking Git commits the Working Directory.
- Assuming `origin` is a Git keyword.
- Confusing Git with GitHub.
- Assuming `git remote add` uploads the project.
- Thinking staged files automatically update after editing.

---

# Last Updated

Day 01