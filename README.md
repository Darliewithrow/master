# Fixing the "Uploads are disabled" Error for ethereum/EIPs Contributions

If GitHub shows **"Uploads are disabled"** when you try to add or edit files in [`ethereum/EIPs`](https://github.com/ethereum/EIPs), the usual cause is simple: you do not have permission to push directly to that repository.

The fix is to use the standard open-source workflow:

1. **Fork** the repository to your own GitHub account
2. **Clone** your fork locally
3. **Create a branch** for your change
4. **Commit and push** the branch to your fork
5. **Open a pull request** back to `ethereum/EIPs`

This guide walks through that process step by step.

---

## Why this error happens

The `ethereum/EIPs` repository is a shared project. Most contributors do **not** have direct write access, so GitHub blocks direct uploads and edits on the upstream repository.

That is expected behavior. Instead of uploading files directly to `ethereum/EIPs`, you should:

- work in **your own fork**
- push changes to **your forked branch**
- submit a **pull request** for review

---

## Before you start

You should have:

- a GitHub account
- Git installed locally
- basic familiarity with running terminal commands

If you need Git installation instructions, see the [official Git documentation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

---

## Step 1: Fork the repository

1. Open [`https://github.com/ethereum/EIPs`](https://github.com/ethereum/EIPs)
2. Click **Fork**
3. Create the fork under your own GitHub account

After this step, you will have a copy of the repository at:

```text
https://github.com/YOUR-USERNAME/EIPs
```

---

## Step 2: Clone your fork

Clone **your fork**, not the upstream repository:

```bash
git clone https://github.com/YOUR-USERNAME/EIPs.git
cd EIPs
```

If you prefer SSH:

```bash
git clone git@github.com:YOUR-USERNAME/EIPs.git
cd EIPs
```

---

## Step 3: Add the upstream remote

This step is optional but recommended. It makes it easier to keep your fork up to date.

```bash
git remote add upstream https://github.com/ethereum/EIPs.git
git remote -v
```

You should now see both:

- `origin` → your fork
- `upstream` → `ethereum/EIPs`

---

## Step 4: Create a branch for your change

Do not work directly on your default branch. Create a dedicated branch first:

```bash
git checkout -b your-change-name
```

Use a short, descriptive branch name that reflects your change.

---

## Step 5: Make your changes

Edit the files you need to update in your local clone.

When you are done, review your changes:

```bash
git status
git diff
```

---

## Step 6: Commit your work

Stage and commit your changes:

```bash
git add .
git commit -m "Describe your change clearly"
```

Write a commit message that explains what you changed.

---

## Step 7: Push to your fork

Push your branch to **your fork**, not to `ethereum/EIPs`:

```bash
git push -u origin your-change-name
```

Because `origin` points to your fork, this push should succeed if you have permission to your own repository.

---

## Step 8: Open a pull request

After pushing:

1. Go to your fork on GitHub
2. GitHub will usually show a **Compare & pull request** button
3. Open the pull request from:
   - **head branch:** `YOUR-USERNAME:your-change-name`
   - **base repository:** `ethereum/EIPs`
4. Fill in the pull request title and description
5. Submit the pull request

This is the correct way to propose changes to the upstream repository.

---

## If you already cloned the upstream repository

If you cloned `ethereum/EIPs` before creating a fork, you do **not** need to start over.

You can create a fork on GitHub, then update your local `origin` remote:

```bash
git remote rename origin upstream
git remote add origin https://github.com/YOUR-USERNAME/EIPs.git
git remote -v
```

After that, push your branch to your fork:

```bash
git push -u origin your-change-name
```

---

## Common mistakes

### Trying to upload directly to `ethereum/EIPs`

If you do not have write access, GitHub will block direct uploads and web edits. Use a fork instead.

### Cloning the upstream repository and pushing to it

You can clone the upstream repository for reference, but your branch must be pushed to your own fork.

### Working on the default branch

Creating a separate branch keeps your work isolated and makes pull requests easier to review.

---

## Troubleshooting

### I forked the repository, but Git still pushes to the wrong remote

Check your remotes:

```bash
git remote -v
```

If `origin` is not your fork, update it:

```bash
git remote set-url origin https://github.com/YOUR-USERNAME/EIPs.git
```

### I do not see the pull request button

Try opening:

```text
https://github.com/ethereum/EIPs/compare
```

Then choose your fork and branch manually.

### I accidentally committed to the wrong branch

Create a new branch from your current state and push that branch to your fork:

```bash
git checkout -b your-change-name
git push -u origin your-change-name
```

---

## Resources

- [ethereum/EIPs repository](https://github.com/ethereum/EIPs)
- [GitHub documentation: Fork a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
- [GitHub documentation: Creating a pull request from a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/creating-a-pull-request-from-a-fork)
- [Git documentation](https://git-scm.com/doc)

---

## Summary

The **"Uploads are disabled"** message usually means you are trying to change a repository where you do not have direct write access. For `ethereum/EIPs`, the correct workflow is:

1. fork the repository
2. clone your fork
3. create a branch
4. push to your fork
5. open a pull request

Once you follow that workflow, you should no longer need direct uploads to the upstream repository.