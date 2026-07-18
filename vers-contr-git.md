## Version Control and Git


If you don’t have any past experience with Git, either try reading the first couple chapters of Pro Git or go through a tutorial like Learn Git Branching. As you’re working through it, relate Git commands to the data model. As you’re working through it, relate Git commands to the data model.
- I've learned Git thanks to professor Brian Yu's introduction to Git and GitHub: https://www.youtube.com/watch?v=MJUJ4wbFm_A.
I was able to test my knowledge of Git by using it during the creation of my final project for CS50x.


Clone the repository for the class website.
Explore the version history by visualizing it as a graph.
- git log --all --graph --decorate

Who was the last person to modify README.md? (Hint: use git log with an argument).
- The latest commit was from Anish Athalye:

```
commit 49f676cc3a754529ceff846dc68d529feb747cc6
Author: Anish Athalye <me@anishathalye.com>
Date:   Sat Apr 25 11:01:42 2026 -0700

    Tweak text about license
```

What was the commit message associated with the last modification to the collections: line of _config.yml? (Hint: use git blame and git show).

```
Get the hash of the latest modification:

git blame -l _config.yml | awk '{print $4, $5, $1}' | sort
a2b53b74de299dcecfd04513525d35e5dc1a0a2c

git show a2b53b74de299dcecfd04513525d35e5dc1a0a2c

Author: Anish Athalye <me@anishathalye.com>
Date:   Fri Jan 23 16:39:39 2026 -0500

    Update list of files excluded from build
```


One common mistake when learning Git is to commit large files that should not be managed by Git or adding sensitive information. Try adding a file to a repository, making some commits and then deleting that file from history (not just the latest commit). You may want to look at this.

- First, let's add a sensitive file:

```
vim super-secret-file.text

git add .

git commit -m "Addded some secret info, by mistake"

git push
```

- Now, we'll have to remove it and the associated commit:

```
git-filter-repo --sensitive-data-removal --invert-paths --path super-secret-file.txt

git push --force --mirror origin
```

- The file and the commit will be removed, but the hashes of the previous commits will also be modified.


Clone some repository from GitHub, and modify one of its existing files. What happens when you do git stash? What do you see when running git log --all --oneline? Run git stash pop to undo what you did with git stash. In what scenario might this be useful?

- git stash saves the current local modifications and index and returns the current working directory to the state previous to the changes. When running git log --all --oneline I get:

```
a0d81d6 (refs/stash) WIP on main: f176e92 Added new exercises for vers-contr-git.md
061332c index on main: f176e92 Added new exercises for vers-contr-git.md
f176e92 (HEAD -> main, origin/main, origin/HEAD) Added new exercises for vers-contr-git.md
```

- git stash might be useful when checking for bugs in a newly implemented piece of code; we can save our work, and see if the bug comes from the latter.


Like many command line tools, Git provides a configuration file (or dotfile) called ~/.gitconfig. Create an alias in ~/.gitconfig so that when you run git graph, you get the output of git log --all --graph --decorate --oneline. You can do this by directly editing the ~/.gitconfig file, or you can use the git config command to add the alias. Information about git aliases can be found here.

- ```git config --global alias.graph 'log --all --graph --decorate --oneline'```


You can define global ignore patterns in ~/.gitignore_global after running git config --global core.excludesfile ~/.gitignore_global. This sets the location of the global ignore file that Git will use, but you still need to manually create the file at that path. Set up your global gitignore file to ignore OS-specific or editor-specific temporary files, like .DS_Store.

- Some examples: ```/.DS_store```, ```/__pycache__```, ```.pyc```


Practice resolving merge conflicts by simulating a collaborative scenario:

1. Create a new repository with git init and create a file called recipe.txt with a few lines (e.g., a simple recipe).


2. Commit it, then create two branches: git branch salty and git branch sweet.
    

3. In the salty branch, modify a line (e.g., change “1 cup sugar” to “1 cup salt”) and commit.


4. In the sweet branch, modify the same line differently (e.g., change “1 cup sugar” to “2 cups sugar”). and commit.
    

5. Now switch to master and try git merge salty, then git merge sweet. What happens? Look at the contents of recipe.txt - what do the <<<<<<<, =======, and >>>>>>> markers mean?

```
$ git merge salty
Updating c7457b3..f5f5e0f
Fast-forward
 recipe.txt | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

$ git merge sweet
Auto-merging recipe.txt
CONFLICT (content): Merge conflict in recipe.txt
Automatic merge failed; fix conflicts and then commit the result.
```

- ```<<<<<<<``` indicates the head branch
- ```=======``` separates the two conflicting branches
- ```>>>>>>>``` indicates the branch which is causing the conflict


6. Resolve the conflict by editing the file to keep the content you want, removing the conflict markers, and completing the merge with git add and git commit (or git merge --continue). Alternatively, try using git mergetool to resolve the conflict with a graphical or terminal-based merge tool.


7. Use git log --graph --oneline to visualize the merge history you just created.

```
$ git log --graph --oneline
*   60c33a2 (HEAD -> master) Merge branch 'sweet'
|\  
| * b42d2be (sweet) New instructions for sugar
* | f5f5e0f (salty) Add salt in the recipe(for brownies? Hm, ok)
|/  
* c7457b3 Added the recipe for brownies
```