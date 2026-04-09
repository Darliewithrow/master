# Contributing to Ethereum EIPs

> **TL;DR** — Direct file uploads to the ethereum/EIPs repository are disabled for users without write access. To contribute, you must fork the repository, make your changes locally, and open a pull request.

This guide walks you through the standard GitHub contribution workflow for the [Ethereum EIPs repository](https://github.com/ethereum/EIPs).

---

## Why You're Seeing the "Uploads are disabled" Error

When you try to upload files directly to `ethereum/EIPs`, you see:

> **Uploads are disabled.**
> File uploads require push access to this repository.

This is expected. The ethereum/EIPs repository requires all contributions to go through pull requests — direct uploads are not permitted without write access.

---

## How to Contribute: Step-by-Step

### Step 1 — Fork the Repository

1. Go to [https://github.com/ethereum/EIPs](https://github.com/ethereum/EIPs)
2. Click the **Fork** button in the top-right corner
3. GitHub will create a copy of the repository under your account

### Step 2 — Clone Your Fork

```bash
git clone https://github.com/YOUR-USERNAME/EIPs.git
cd EIPs
```

> Replace `YOUR-USERNAME` with your GitHub username.

### Step 3 — Create a New Branch

```bash
git checkout -b your-feature-branch
```

Use a descriptive branch name, for example: `add-eip-1234` or `fix-eip-20-typo`.

### Step 4 — Add or Modify Files

Make your changes locally, then stage them:

```bash
# Stage a new file
git add your-file.md

# Stage a modified file
git add modified-file.md
```

### Step 5 — Commit Your Changes

```bash
git commit -m "Add/Update: Brief description of your changes"
```

### Step 6 — Push to Your Fork

```bash
git push origin your-feature-branch
```

### Step 7 — Open a Pull Request

1. Go to your fork on GitHub: `https://github.com/YOUR-USERNAME/EIPs`
2. Click **Compare & pull request**
3. Fill in the pull request details:
   - **Title**: Clear and concise (e.g., `Add EIP-1234: Token Standard`)
   - **Description**: Explain what you changed and why
4. Click **Create pull request**

### Step 8 — Respond to Review Feedback

The ethereum/EIPs maintainers will review your pull request. Be prepared to:
- Address requested changes
- Answer questions in the review comments
- Update your branch if needed (just push new commits to the same branch)

---

## EIP Contribution Guidelines

Before submitting an EIP (Ethereum Improvement Proposal), ensure you have:

1. Read the [EIP-1](https://eips.ethereum.org/EIPS/eip-1) process document — this defines the EIP lifecycle and requirements
2. Used the official EIP template format
3. Written a complete, well-documented proposal
4. Discussed your idea with the Ethereum community first (see forums and Discord below)

---

## Common File Types in EIPs

| File Type | Purpose |
|-----------|---------|
| `.md` (Markdown) | The EIP document itself |
| Assets (images, diagrams) | Supporting visuals, placed in an `assets/eip-XXXX/` folder |
| Code examples | Reference implementations or test cases for your proposal |

---

## Resources

| Resource | Link |
|----------|------|
| EIPs Website | https://eips.ethereum.org/ |
| EIPs Repository | https://github.com/ethereum/EIPs |
| EIP-1 (Process) | https://eips.ethereum.org/EIPS/eip-1 |
| GitHub: Forking a repo | https://docs.github.com/en/get-started/quickstart/fork-a-repo |
| GitHub: Creating a pull request | https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request |

---

## Need Help?

- 💬 [Ethereum Magicians forum](https://ethereum-magicians.org/) — best place for EIP discussions
- 🗨️ [Ethereum Discord](https://discord.gg/ethereum-org) — real-time community chat
- 📋 [EIPs repository discussions](https://github.com/ethereum/EIPs/discussions) — ask questions directly

---

> **Note**: This repository (`Darliewithrow/master`) is a guide repository. The actual EIPs should be submitted to [https://github.com/ethereum/EIPs](https://github.com/ethereum/EIPs) following the process described above.
