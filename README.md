# python-poetry-ci-example

## Overview 

The overall goal of semantic versioning is to calculate version 
numbers for releases based on commit messages. Tools like `python-semantic-release`
can be used to perform this computation, set the version number in your
repo, tag the code correspondingly and create a release in GitHub or in PyPi.

## Useful commands

### Version Command

The version command calculates the next version based on the commit messages since the last release and updates the version in your project files.

```bash
semantic-release --noop version
```

* Description: Shows the changes that will trigger a version bump without actually changing anything.
* Usage: Use this command to see the expected version increment and the changes that will be included in the release.

```bash
semantic-release --noop version # Dry run version of the version command: shows pending changes due version bump
```

### Publish Command

The publish command performs the entire release process, including creating a new version, generating changelogs, 
and publishing the package.

```bash
semantic-release --noop publish
```

* Description: Executes a full release simulation without publishing any changes. This includes version bump, changelog generation, and publishing steps.
* Usage: Use this command to simulate the entire release process and verify that all steps will execute correctly before running the actual release.

## Gotchas

* You must tag the first version by hand so that `semantic-release` can determine the next version
* The release workflow needs permissions to write packages. This can be achieved either via
  * Settings > Actions > General > Workflow Permissions > Choose: Read and write permissions
  * Or by adding write permissions to the workflow as shown in the following snippet:

```bash
jobs:
  release:
    permissions:
      contents: write
```

## Sources and References

This project uses the Python implementation of semantic release:
* GitHub repo: https://github.com/python-semantic-release/python-semantic-release
* Documentation: https://python-semantic-release.readthedocs.io/en/latest/

This blog post and the corresponding GH repo served as baseline:
* https://guicommits.com/semantic-release-to-automate-versioning-and-publishing-to-pypi-with-github-actions/
* https://github.com/guilatrova/tryceratops/tree/main/.github/workflows

A further source is this blog post:
* https://mestrak.com/blog/semantic-release-with-python-poetry-github-actions-20nn
* https://raw.githubusercontent.com/MeStrak/dr-sven/main/.github/workflows/ci.yml

This GitHub bot is used to enforce semantic PRs:
* https://github.com/marketplace/semantic-prs

Useful for debugging:
https://python-semantic-release.readthedocs.io/en/latest/troubleshooting.html#increasing-verbosity
