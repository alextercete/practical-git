# Solution: Undoing/redoing commits

Before starting to undo the last commit, it's useful to get a big picture of the commit history:

```bash
git log --oneline
```

Next, inspect the commit you intend to undo:

```bash
git show
```

You'll notice there's one hunk that shouldn't be part of the commit:

```diff
+
+    def test_division_resulting_in_floating_point_number(self):
+        self.assertAlmostEqual(2.5, self.calculator.divide(5, 2))
```

In order to address this issue, we'll undo the last commit, but keep the changes introduced by it in the working directory:

```bash
git reset HEAD~1
```

Then, selectively stage the changes, skipping any unrelated hunks (you'll have to do some [manual editing][editing_patches]):

```bash
git add -p
```

Inspect the staging area to confirm it contains the expected changes:

```bash
git diff --staged
```

Commit the changes, reusing the message from the commit that was undone.

```bash
git commit --reuse-message=HEAD@{1}
```

Finally, commit the remaining changes:

```bash
git commit -a -m "Add test for floating-point division result"
```

## Exercise

See branch [`exercise/undoing-commits`][exercise].

## Useful commands

Command                                       | Description
----------------------------------------------|--------------------------------------------
[`git reset HEAD~1`][grH]                     | Undo the last commit, keeping changes
[`git commit --reuse-message=<commit>`][gcrm] | Commit, reusing the message from `<commit>`

[editing_patches]: https://git-scm.com/docs/git-add#_editing_patches
[exercise]: https://github.com/alextercete/practical-git/tree/exercise/undoing-commits
[grH]: https://git-scm.com/docs/git-reset#git-reset---mixed
[gap]: https://git-scm.com/docs/git-add#git-add--p
[gcrm]: https://git-scm.com/docs/git-commit#git-commit---reuse-messageltcommitgt