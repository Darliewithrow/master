# Contributing to Ethereum EIPs

This guide explains how to contribute to the [Ethereum EIPs repository](https://github.com/ethereum/EIPs) when you encounter the "Uploads are disabled" error.

## Setting Up Your Development Environment

Before contributing to Ethereum EIPs, you may need to set up Node.js for testing and development. Here's how to install Node.js using nvm (Node Version Manager), which allows you to easily manage multiple Node.js versions.

### Installing nvm and Node.js

1. **Download and install nvm:**

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

## Why You're Seeing the Upload Error

When you try to upload files directly to the ethereum/EIPs repository, you see this error:

> **Uploads are disabled.**
> File uploads require push access to this repository.

This is expected behavior. The ethereum/EIPs repository doesn't allow direct file uploads from users who don't have write access to the repository.

## How to Contribute to the EIPs Repository

Instead of uploading files directly, you need to follow the standard GitHub contribution workflow:

### 1. Fork the Repository

1. Go to https://github.com/ethereum/EIPs
2. Click the "Fork" button in the top-right corner
3. This creates a copy of the repository under your GitHub account

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR-USERNAME/EIPs.git
cd EIPs
```

### 3. Create a New Branch

```bash
git checkout -b your-feature-branch
```

### 4. Add Your Files

You can now add, modify, or create files locally on your computer:

```bash
# Add your new files
git add your-file.md

# Or modify existing files and add them
git add modified-file.md
```

### 5. Commit Your Changes

```bash
git commit -m "Add/Update: Brief description of your changes"
```

### 6. Push to Your Fork

```bash
git push origin your-feature-branch
```

### 7. Create a Pull Request

1. Go to your fork on GitHub (https://github.com/YOUR-USERNAME/EIPs)
2. Click "Compare & pull request"
3. Fill in the pull request details:
   - Title: Clear, concise description
   - Description: Explain your changes and why they're needed
4. Click "Create pull request"

### 8. Wait for Review

The ethereum/EIPs maintainers will review your pull request and may:
- Approve and merge it
- Request changes
- Provide feedback

## EIP Contribution Guidelines

Before contributing an EIP (Ethereum Improvement Proposal), make sure to:

1. Read the [EIP-1](https://eips.ethereum.org/EIPS/eip-1) process document
2. Follow the EIP template format
3. Ensure your EIP is complete and well-documented
4. Discuss your idea in the Ethereum community first (forums, Discord, etc.)

## Common File Types in EIPs

- **Markdown files (.md)**: EIP documents themselves
- **Asset files**: Images, diagrams, etc. (usually placed in an `assets` folder)
- **Code examples**: Supporting code for your proposal

## Resources

- **EIPs Website**: https://eips.ethereum.org/
- **EIPs Repository**: https://github.com/ethereum/EIPs
- **EIP-1 (Process)**: https://eips.ethereum.org/EIPS/eip-1
- **GitHub Docs on Forking**: https://docs.github.com/en/get-started/quickstart/fork-a-repo
- **GitHub Docs on Pull Requests**: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request

## Need Help?

- Join the [Ethereum Magicians forum](https://ethereum-magicians.org/)
- Visit the [Ethereum Discord](https://discord.gg/ethereum-org)
- Ask questions in the EIPs repository discussions

---

**Note**: This repository (Darliewithrow/master) is a guide repository. The actual EIPs should be submitted to https://github.com/ethereum/EIPs following the process described above.
