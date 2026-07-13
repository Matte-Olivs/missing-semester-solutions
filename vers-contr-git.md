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

p