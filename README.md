# Solution: Splitting changes

Before starting to split changes, it's useful to get a big picture of what files have changed since the last commit:

```bash
git status
```

Next, you should take a closer look at the changes and try to identify how many commits they should be split into:

```bash
git diff
```

Once you have an idea, trigger the [_interactive mode_][interactive_mode] of `git-add`:

```bash
git add -p
```

The following options are available:

- To add a hunk to the staging area, choose `y`
- To skip a hunk, choose `n`
- To split a hunk into smaller ones, choose `s`
- To [manually edit a hunk][editing_patches], choose `e`

When you're done adding one set of changes, review what's about to be committed:

```bash
git diff --staged
```

Finally, commit the changes:

```bash
git commit
```

Repeat the process until there are no changes left to commit. When you finish, you should have something like this:

```bash
$ git log --pretty=%s HEAD~4..
Implement division
Implement multiplication
Rename sum to add
Rename parameters
```

## Exercise

See branch [`exercise/splitting-changes`][exercise].

## Useful commands

Command                                  | Description
-----------------------------------------|------------------------------------------
[`git add --patch`][gap]                 | Selectively stage changes
[`git diff --staged`][gds]               | Show staged changes

[interactive_mode]: https://git-scm.com/docs/git-add#git-add-patch
[editing_patches]: https://git-scm.com/docs/git-add#_editing_patches
[exercise]: https://github.com/alextercete/practical-git/tree/exercise/splitting-changes
[gap]: https://git-scm.com/docs/git-add#git-add---patch
[gds]: https://git-scm.com/docs/git-diff#git-diff-emgitdiffemltoptionsgt--cachedltcommitgt--ltpathgt82308203