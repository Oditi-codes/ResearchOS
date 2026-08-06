# Interview Questions

> This document contains every interview question encountered throughout the ResearchOS project.
>
> Questions are grouped by topic and continuously expanded.

---

# Table of Contents

- Git
- Software Engineering
- Backend
- Frontend
- Databases
- AI / ML
- RAG
- AWS
- DSA
- System Design

---

# Git

---

## Q1. What is Git?

### Beginner Answer

Git is a version control system used to track changes in files.

### Strong Candidate Answer

Git is a Distributed Version Control System (DVCS) that tracks project history by storing snapshots of files. It enables collaboration, branching, merging, rollback, and distributed development while allowing every developer to maintain a complete copy of the repository.

---

## Q2. What is the difference between Git and GitHub?

### Beginner Answer

Git is installed locally.

GitHub stores projects online.

### Strong Candidate Answer

Git is a distributed version control system responsible for tracking changes and managing history. GitHub is a cloud platform that hosts Git repositories and provides collaboration features such as Pull Requests, Issues, Actions, Code Reviews, and access control.

---

## Q3. What is the Staging Area?

### Beginner Answer

It stores files before committing.

### Strong Candidate Answer

The Staging Area (Index) stores snapshots of selected changes that will become the next commit. It enables developers to create atomic and meaningful commits instead of committing every modification made in the Working Directory.

---

## Q4. Why does Git have a Staging Area?

### Beginner Answer

To choose which files to commit.

### Strong Candidate Answer

The Staging Area provides fine-grained control over commits. It allows developers to stage only selected changes, improving commit quality, collaboration, debugging, and code review.

---

## Q5. Why didn't we need to run `git add` again after the failed commit?

### Beginner Answer

Because the files were already staged.

### Strong Candidate Answer

A failed commit due to missing author identity does not modify the Staging Area. The staged snapshots remain unchanged, so after configuring the Git identity, the same staged content can be committed directly.

---

## Q6. What is a Remote Repository?

### Beginner Answer

Another Git repository.

### Strong Candidate Answer

A remote repository is another Git repository that the local repository communicates with for synchronization. It can be hosted on GitHub, GitLab, Bitbucket, a company server, or another developer's machine.

---

## Q7. Is `origin` a Git keyword?

### Beginner Answer

No.

### Strong Candidate Answer

No. `origin` is simply the conventional alias assigned to the primary remote repository. Any valid alias can be used.

---

## Q8. Where does Git store remote information?

### Beginner Answer

Inside the `.git/config` file.

### Strong Candidate Answer

Git stores remote configuration inside the `.git/config` file, including fetch and push URLs, allowing commands such as `git push origin main` to resolve the correct remote repository.

---

## Q9. Why shouldn't we initialize a new GitHub repository with a README if the local repository already contains one?

### Beginner Answer

Because it creates conflicts.

### Strong Candidate Answer

Initializing the GitHub repository with a README creates an independent root commit, resulting in unrelated commit histories between the local and remote repositories. Creating an empty remote avoids this issue.

---

## Q10. What does `git push -u origin main` do?

### Beginner Answer

Uploads the project to GitHub.

### Strong Candidate Answer

It pushes the local `main` branch to the `origin` remote and establishes `origin/main` as the upstream tracking branch. This enables future `git push` and `git pull` commands to work without explicitly specifying the remote and branch.

---

# Last Updated

Day 01