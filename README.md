# Solution: Discarding changes

Before starting to discard unwanted changes, it's useful to get a big picture of what files have been changed since the last commit:

```bash
git status
```

Next, you should take a closer look at the changes and try to identify any unwanted ones.

```bash
git diff
```

You'll notice there are a few changes not related to the rest:

1. A call to the `print` function for debugging
1. A leftover `TODO` comment
1. An extraneous whitespace

At this point, you could open the affected files in a text editor and undo the changes manually, one by one. However, there's a better way:

```bash
git checkout -p
```

The above command will trigger the [_interactive patch mode_][patch_mode] of `git-checkout`:

- To discard a hunk from the working directory, choose `y`
- To keep a hunk in the working directory, choose `n`
- To split a hunk into smaller ones, choose `s`

Once you're done, double-check that the remaining changes match your expectations:

```bash
git diff
```

If they still contain unwanted changes, run `git checkout -p` again until you've discarded all of them. Finally, commit all remaining changes:

```bash
git commit -a -m "Initialise SUT in setUp method"
```

## Exercise

See branch [`exercise/discarding-changes`][exercise].

## Useful commands

Command                       | Description
------------------------------|-----------------------------------------------------
[`git checkout --patch`][gcp] | Selectively discard changes
[`git commit --all`][gca]     | Automatically stage modified files before committing

[patch_mode]: https://git-scm.com/docs/git-checkout#git-checkout--p
[exercise]: https://github.com/alextercete/practical-git/tree/exercise/discarding-changes
[gcp]: https://git-scm.com/docs/git-checkout#git-checkout--p
[gca]: https://git-scm.com/docs/git-commit#git-commit---all