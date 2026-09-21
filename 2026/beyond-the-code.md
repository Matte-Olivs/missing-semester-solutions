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