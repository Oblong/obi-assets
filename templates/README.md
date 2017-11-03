# {{project_name}}

**Clone this repository with `git lfs clone`**

This repository uses Git LFS to track large assets. You can install Git LFS on your macbook with `brew install git-lfs`. If you are unfamiliar with Git LFS, please read the documentation on their website: <https://git-lfs.github.com/>

## How to add assets to this repository

With Git LFS installed, you can `git add` your asset, commit and push.

## File types

By default, this repository is configured to track all files with extensions of png, jpg, mp3, flac, mp4, mov, mkv, and more. Check `.gitattributes` for your complete listing.

## Deploying assets for development

Use `obi go` to deploy this directory into `/data1/dev/{{project_name}}` on every machine in the room.

At the warehouse (hex):

```
obi go hex
```

At Austin (hex):

```
obi go hex
```

Add more rooms to project.yaml as you need them!

## Directory structure

The `{{project_name}}` directory contains assets that will be installed by the debian package produced by this repo.
