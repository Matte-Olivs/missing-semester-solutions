## Beyond the Code


Browse the source code of a well-known project (e.g., Redis or curl). Find examples of some of the comment types mentioned in the lecture: a useful TODO, a reference to external documentation, a “why not” comment explaining an avoided approach, or a hard-learned lesson. What would be lost if that comment was not there?
- From the official Mozilla FireFox GitHub repository:

```
    /**
     * Request a screenshot of the full (scrollable) web page currently being rendered, including content outside the
     * currently visible viewport.
     *
     * @param onFinish A callback invoked with the captured [Bitmap], or `null` if the capture failed. Important for
     *   engine-gecko: Make sure not to reference the context or view in this callback to prevent memory leaks:
     *   https://bugzilla.mozilla.org/show_bug.cgi?id=1678364
     */
    fun captureFullPage(onFinish: (Bitmap?) -> Unit) = Unit
```
- Without this comment, a developer might inadvertently introduce a memory leak by referencing the context or view inside the callback, repeating a past mistake tracked in the linked Bugzilla issue.


Pick an open-source project you’re interested in and look at its recent commit history (git log). Find one commit with a good message that explains why the change was made, and one with a weak message that only describes what changed. For the weak one, look at the diff (git show <hash>) and try to write a better commit message following the Problem → Solution → Implications structure. Notice how much work is required to reassemble the necessary context after the fact!
- From the official curl GitHub repository:

```
Commit 198012e
committed on Mar 5, 2013
imap: Added support for list command
```

- A better commit message:
not have an "active only" connection or custom command 
```
imap: add support for list command

Now requires an imap.uid flag or data upload.
Execute only if an inbox has been selected and the user is pointing at
a specific message via UID.
Finally, if a UID is selected, enter the inbox and point at the message. 
Otherwise, list the whole inbox.
```


Compare the READMEs of three GitHub projects with 1000+ stars. Are all of them equally useful? Look for things that come across mostly as noise to you as a lesson for future READMEs you write yourself.
- Redis has a very detailed and descriptive README, while curl and Mozilla FireFox both kept it concise with external links for their manual pages. 


Find an open issue on a project you use (check the “good first issue” or “help wanted” labels if they have it). Evaluate the issue against the criteria from the lecture: does it seem like it values the maintainer’s time and contains all the information necessary to debug it, or do you expect that the maintainer may need to go multiple rounds of questions with the submitter to get to the root problem?
- I've found this neat example, from the Redis GitHub issues page. It's definitely well-written, but as a maintainer pointed out, it's missing:

→ Steps to reproduce

→ Expected vs actual behavior

→ Environment details

More details at: https://github.com/redis/redis/issues/15826