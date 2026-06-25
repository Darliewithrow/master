# Contributing to Ethereum EIPs: Fixing "Uploads are disabled"

If you've tried to contribute to the [Ethereum EIPs repository](https://github.com/ethereum/EIPs) and encountered the error **"Uploads are disabled"**, this guide explains why it happens and how to contribute correctly using the standard GitHub fork-and-pull-request workflow.

---

## Why Does This Error Occur?

The Ethereum EIPs repository disables direct file uploads through the GitHub web UI to encourage contributors to use the proper Git workflow. This ensures changes go through code review and maintain repository quality.

---

## The Correct Contribution Workflow

### Step 1 — Fork the Repository

1. Go to [https://github.com/ethereum/EIPs](https://github.com/ethereum/EIPs)
2. Click the **Fork** button in the top-right corner
3. Select your account as the destination — this creates your own copy at `https://github.com/YOUR-USERNAME/EIPs`

### Step 2 — Clone Your Fork Locally

```bash
git clone https://github.com/YOUR-USERNAME/EIPs.git
cd EIPs
```

Replace `YOUR-USERNAME` with your GitHub username.

### Step 3 — Create a Feature Branch

Always create a new branch for your changes instead of working directly on `main`:

```bash
git checkout -b my-eip-contribution
```

### Step 4 — Make Your Changes

Add or edit files in your local copy. For example, to add a new EIP draft:

```bash
# Create your EIP file following the EIP template
cp EIPS/eip-1.md EIPS/eip-XXXX.md
# Edit the file with your content
```

### Step 5 — Commit Your Changes

```bash
git add .
git commit -m "Add EIP-XXXX: Brief description of your proposal"
```

### Step 6 — Push Your Branch to GitHub

```bash
git push origin my-eip-contribution
```

### Step 7 — Open a Pull Request

1. Go to your fork at `https://github.com/YOUR-USERNAME/EIPs`
2. Click the **Compare & pull request** button that appears after pushing
3. Fill in a clear title and description for your pull request
4. Click **Create pull request**

Your contribution will now go through the review process by EIP editors.

---

## Keeping Your Fork Up to Date

Before making new changes, sync your fork with the upstream repository to avoid conflicts:

```bash
# Add the upstream remote (only needed once)
git remote add upstream https://github.com/ethereum/EIPs.git

# Fetch and merge the latest changes
git fetch upstream
git checkout main
git merge upstream/main

# Push the updated main to your fork
git push origin main
```

---

## Troubleshooting

| Problem | Solution |
|---|---|
| "Uploads are disabled" error | Use the fork + clone + PR workflow described above |
| Merge conflicts | Run `git fetch upstream && git merge upstream/main` on your branch |
| Push rejected | Ensure you're pushing to your fork (`origin`), not `upstream` |
| PR not showing up | Make sure you pushed your feature branch, not `main` |

---

## Resources

- [Ethereum EIPs Repository](https://github.com/ethereum/EIPs)
- [EIP-1: EIP Purpose and Guidelines](https://eips.ethereum.org/EIPS/eip-1)
- [GitHub Docs: Forking a repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
- [GitHub Docs: Creating a pull request from a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)
- [Ethereum Community Forum](https://ethereum-magicians.org/)

---

## Contributing to This Guide

Found something unclear or out of date? See [CONTRIBUTING.md](CONTRIBUTING.md) for how to improve this guide.
