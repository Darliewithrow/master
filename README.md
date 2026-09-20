# Fixing the "Uploads are disabled" Error for Ethereum EIPs

If GitHub shows **"Uploads are disabled. File uploads require push access to this repository."** while you are trying to contribute to [`ethereum/EIPs`](https://github.com/ethereum/EIPs), you are usually attempting to upload files directly to the main EIPs repository.

## Setting Up Your Development Environment

Before contributing to Ethereum EIPs, you may need to set up Node.js for testing and development. Here's how to install Node.js using nvm (Node Version Manager), which allows you to easily manage multiple Node.js versions.

### Installing nvm and Node.js

1. **Download and install nvm:**

   > **Note:** Always verify the installation script from the [official nvm repository](https://github.com/nvm-sh/nvm) before running.

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
```

2. **Activate nvm** (in lieu of restarting the shell):

```bash
. "$HOME/.nvm/nvm.sh"
```

3. **Download and install Node.js:**

```bash
nvm install 24
```

4. **Verify the Node.js version:**

```bash
node -v # Should print "v24.12.0".
```

5. **Verify npm version:**

```bash
npm -v # Should print "11.6.2".
```

This setup ensures you have the correct Node.js and npm versions for Ethereum development tools and testing frameworks.

That repository only allows maintainers to push changes directly. Contributors should work from a **fork** and then open a **pull request**.

## What the Error Means

The message does **not** mean you cannot contribute. It means:

- You do not have direct write access to `ethereum/EIPs`
- GitHub is blocking uploads to the upstream repository
- You need to submit your changes from your own fork instead

## Recommended Workflow

Follow these steps to contribute the standard GitHub way.

### 1. Fork the EIPs Repository

Open the [ethereum/EIPs repository](https://github.com/ethereum/EIPs) and select **Fork**.

Create a fork under your own GitHub account so you have permission to push changes there.

### 2. Clone Your Fork

Clone **your fork**, not the upstream repository:

```bash
git clone https://github.com/YOUR-USERNAME/EIPs.git
cd EIPs
```

Replace `YOUR-USERNAME` with your GitHub username.

### 3. Add the Upstream Remote

Connect your local clone to the official EIPs repository so you can pull future updates:

```bash
git remote add upstream https://github.com/ethereum/EIPs.git
git remote -v
```

After this, `origin` should point to your fork and `upstream` should point to `ethereum/EIPs`.

### 4. Create a Branch for Your Change

Create a separate branch before editing files:

```bash
git checkout -b your-eip-change
```

Use a short, descriptive branch name that matches your work.

### 5. Make Your Changes and Commit Them

Edit the files you need, then commit your work:

```bash
git add .
git commit -m "docs: describe your change"
```

Use a commit message that clearly explains what you changed.

### 6. Push to Your Fork

Push your branch to GitHub:

```bash
git push -u origin your-eip-change
```

Because this push goes to **your fork**, GitHub allows it even though you do not have write access to the upstream repository.

### 7. Open a Pull Request

After the push completes:

1. Open your fork on GitHub
2. Select the prompt to create a pull request
3. Confirm the base repository is `ethereum/EIPs`
4. Submit your pull request for review

## If You Already Cloned the Wrong Repository

If you cloned `https://github.com/ethereum/EIPs.git` directly and started working locally, you can usually fix it without losing your changes:

```bash
git remote rename origin upstream
git remote add origin https://github.com/YOUR-USERNAME/EIPs.git
git push -u origin your-eip-change
```

This keeps the official repository as `upstream` and makes your fork the new `origin`.

## Troubleshooting Checklist

If you still see the upload error, confirm that:

- You are pushing to `https://github.com/YOUR-USERNAME/EIPs.git`
- Your branch exists on your fork
- You are opening a pull request instead of uploading directly to `ethereum/EIPs`
- You are signed in to the GitHub account that owns the fork

## Resources

- [ethereum/EIPs repository](https://github.com/ethereum/EIPs)
- [GitHub Docs: Fork a repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
- [GitHub Docs: Creating a pull request from a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)
- [GitHub Docs: Managing remote repositories](https://docs.github.com/en/get-started/git-basics/managing-remote-repositories)

## Scope of This Repository

This repository is only a guide for the contribution workflow. It is **not** the place to submit actual EIP changes. For real proposals and edits, use the [`ethereum/EIPs`](https://github.com/ethereum/EIPs) repository.
