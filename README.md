# Workshop: Crafting commits

## Set-up

1. [Install Git][install_git]
1. Clone this repository
1. [Recommended] [Install VS Code][install_vscode]
1. [Recommended] [Configure Git to use VS Code][vscode_as_git_editor] (or your [favourite editor][git_editor])

### Useful aliases

```
git config alias.graph 'log --oneline --graph --decorate'
```

```
git config alias.amend 'commit --amend --no-edit'
```

## Exercises

Choose an exercise and switch to the correspondent branch to get started:

- Discarding changes ([`exercise/discarding-changes`][discarding_changes])
- Splitting changes into multiple commits ([`exercise/splitting-changes`][splitting_changes])
- Ameding previous commits ([`exercise/amending-commits`][amending_commits])
- Undoing/redoing commits ([`exercise/undoing-commits`][undoing_commits])

## Slides

<https://docs.google.com/presentation/d/1LJ5YAUaFR89CZiR6vWy3Y_PJJm_igWWy-_j6LpcZ7Js/edit>

## References

- [A Note About Git Commit Messages][commit_messages]
- [Pro Git][pro_git]
  - [Interactive Staging][interactive_staging]
  - [Reset Demystified][reset]
- [Deep Dive into Git][deep_dive_into_git]

[install_git]: https://www.atlassian.com/git/tutorials/install-git
[install_vscode]: https://code.visualstudio.com/
[vscode_as_git_editor]: https://code.visualstudio.com/docs/editor/versioncontrol#_vs-code-as-git-editor
[git_editor]: https://help.github.com/articles/associating-text-editors-with-git/
[discarding_changes]: https://github.com/alextercete/practical-git/tree/exercise/discarding-changes
[splitting_changes]: https://github.com/alextercete/practical-git/tree/exercise/splitting-changes
[amending_commits]: https://github.com/alextercete/practical-git/tree/exercise/amending-commits
[undoing_commits]: https://github.com/alextercete/practical-git/tree/exercise/undoing-commits
[commit_messages]: https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html
[pro_git]: https://git-scm.com/book/en/v2
[interactive_staging]: https://git-scm.com/book/en/v2/Git-Tools-Interactive-Staging
[reset]: https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified
[deep_dive_into_git]: https://youtu.be/fBP18-taaNw