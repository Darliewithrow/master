# How to Fix “Uploads are disabled” When Contributing to Ethereum EIPs

If GitHub shows **“Uploads are disabled”** when you try to contribute to the [ethereum/EIPs](https://github.com/ethereum/EIPs) repository, you are likely trying to push from a repository clone you do not have write access to.

The fix is to work from **your fork** instead of directly from `ethereum/EIPs`.

## Quick Workflow

1. **Fork the EIPs repository**
   - Open <https://github.com/ethereum/EIPs>
   - Select **Fork** and create a copy under your account

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/EIPs.git
   cd EIPs
   ```

3. **Create a branch for your changes**
   ```bash
   git checkout -b your-change-name
   ```

4. **Make and commit your changes**
   ```bash
   git add .
   git commit -m "Describe your change"
   ```

5. **Push to your fork**
   ```bash
   git push origin your-change-name
   ```

6. **Open a pull request**
   - Go to your fork on GitHub
   - Select **Compare & pull request**
   - Target base repository: `ethereum/EIPs`

## Why This Happens

You cannot push directly to most upstream repositories unless you are a maintainer. Forking gives you a writable remote under your own account so you can push branches and open pull requests.

## Troubleshooting

- If `origin` points to `ethereum/EIPs`, update it:
  ```bash
  git remote set-url origin https://github.com/YOUR-USERNAME/EIPs.git
  ```
- Confirm remotes:
  ```bash
  git remote -v
  ```
- Add upstream for syncing later:
  ```bash
  git remote add upstream https://github.com/ethereum/EIPs.git
  ```

## Resources

- EIPs repository: <https://github.com/ethereum/EIPs>
- Forking docs: <https://docs.github.com/en/get-started/quickstart/fork-a-repo>
- Pull request docs: <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests>