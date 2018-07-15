# Solution: Amending commits

Before starting to amend the last commit, it's useful to get a big picture of the changes in the working directory:

```bash
git diff
```

Next, selectively amend modifications into the last commit:

```bash
git commit -p --amend
```

Then, verify the commit has been amended correctly:

```bash
git show
```

The command above should output something like this:

```diff
--- a/calculator.py
+++ b/calculator.py
@@ -7,3 +7,8 @@ class Calculator:

     def multiply(self, operand1, operand2):
         return operand1 * operand2
+
+    def divide(self, operand1, operand2):
+        if operand2 == 0:
+            raise ValueError('Cannot divide by zero!')
+        return operand1 / operand2
--- a/test_calculator.py
+++ b/test_calculator.py
@@ -14,5 +14,14 @@ class CalculatorTests(unittest.TestCase):
         calculator = Calculator()
         self.assertEqual(6, calculator.multiply(3, 2))

+    def test_division(self):
+        calculator = Calculator()
+        self.assertEqual(6, calculator.divide(12, 2))
+
+    def test_division_by_zero(self):
+        calculator = Calculator()
+        with self.assertRaises(ValueError):
+            calculator.divide(12, 0)
+
 if __name__ == '__main__':
     unittest.main()
```

Alternatively, if all you want is to change the message of the last commit, run `git commit --amend` with no changes in the staging area. If the commit you want to change isn't the last one, it's still easy to change its message using `git-rebase`:

```bash
git rebase -i HEAD~4
```

In this example, we'll change the message from `Rename parameters` to `Rename parameters for clarity`. To do this, change the appropriate command from `pick` to `reword`, then save and close the file to trigger the rebase. A text editor will open with the message; change it, then save and close the file to continue the rebase.

When you finish, you should have something like this:

```bash
$ git log --pretty=%s HEAD~4..
Implement division
Implement multiplication
Rename sum to add
Rename parameters for clarity
```

## Exercise

See branch [`exercise/amending-commits`][exercise].

## Useful commands

Command                                    | Description
-------------------------------------------|----------------------------
[`git commit --amend`][gca]                | Amend the last commit
[`git rebase --interactive <commit>`][gri] | Start an interactive rebase

[exercise]: https://github.com/alextercete/practical-git/tree/exercise/amending-commits
[gca]: https://git-scm.com/docs/git-commit#git-commit---amend
[gri]: https://git-scm.com/docs/git-rebase#git-rebase--i