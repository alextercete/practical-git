# Exercise: Splitting changes

When working on a task, you'll often spot things that need changing which aren't directly related to it. On the one hand, if you resist the temptation to make the changes, you run the risk of forgetting about them (or having to write them down somewhere for later); on the other hand, if you go ahead and make the changes, they'll likely become part of (and pollute) the upcoming commit. Luckily, Git can help you get the best of both worlds!

In this exercise, you'll learn how to split changes in your working directory into multiple commits.

## Start

### Basic

```
git checkout exercise/splitting-changes
git reset HEAD~1
```

### Advanced

If you started with _Basic_, make sure to [restart](#restart) before starting _Advanced_.

```
git checkout exercise/splitting-changes
git reset HEAD~2
```

## Restart

If you get stuck or want to restart at any point, run the following command:

```
git reset --hard origin/exercise/splitting-changes
```

## Solution

See branch [`solution/splitting-changes`][solution].

[solution]: https://github.com/alextercete/practical-git/tree/solution/splitting-changes