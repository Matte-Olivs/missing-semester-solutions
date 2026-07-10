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

git blame -l _config.yml | awk '{print $4, $5, $1}' | sort -V
a2b53b74de299dcecfd04513525d35e5dc1a0a2c

git show a2b53b74de299dcecfd04513525d35e5dc1a0a2c 

Author: Anish Athalye <me@anishathalye.com>
Date:   Fri Jan 23 16:39:39 2026 -0500

    Update list of files excluded from build
```