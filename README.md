# Exercise: Discarding changes

When working on a task, it will usually take a few attempts before you get to a checkpoint that's worthy of a commit. More often than not, unwanted changes get left behind in the process (such as comments, logging/debugging code or unnecessary whitespace) and end up making their way into a commit. In this exercise, you'll learn how to identify and discard such changes before committing.

## Start

```
git checkout exercise/discarding-changes
git reset HEAD~1
```

## Restart

If you get stuck or want to restart at any point, run the following command:

```
git reset --hard origin/exercise/discarding-changes
```

## Solution

See branch [`solution/discarding-changes`][solution].

[solution]: https://github.com/alextercete/practical-git/tree/solution/discarding-changes