## Code Quality


Try writing a regex pattern and use the grep command-line tool to find occurrences of subprocess.Popen(..., shell=True) in your code. Now, try to “break” the regex pattern. Does semgrep still successfully match the dangerous code that trips up your grep invocation?

``` grep -E 'subprocess\.Popen\(.*, shell\s*=\s*True(, .*)?\)' ```
- semgrep is always successful at finding the dangerous code.


Practice regex search-and-replace in your IDE or text editor by replacing the - Markdown bullet markers with * bullet markers in these lecture notes. Note that just replacing all the “-“ characters in the file would be incorrect, as there are many uses of that character that are not bullet markers.

- ``` sed 's/^- /* /g' file.txt ``` 


Write a regex to capture from JSON structures of the form {"name": "Alyssa P. Hacker", "college": "MIT"} the name (e.g., Alyssa P. Hacker, in this example). Hint: in your first attempt, you might end up writing a regex that extracts Alyssa P. Hacker", "college": "MIT; read about greedy quantifiers in the Python regex docs to figure out how to fix it.

1) Make the regex pattern work even in situations where the name has a " character in it (double quotes can be escaped in JSON with \").

2) We do not recommend using regular expressions for sophisticated parsing problems in practice. Figure out how to use your programming language’s JSON parser for this task. Write a command-line program that takes as input, on stdin, a JSON structure of the form described above, and output, on stdout, the name. You should only need a couple lines of code to do this. In Python, you can do it easily in one line of code beyond import json.

- ``` sed -En 's/\{"name": "(([^"\\]|\\.)*)".*/\1/p' names.txt ```

- In python we only need: 
```
import json

data = json.loads('{"name": "Alyssa P. Hacker", "college": "MIT"}')
print(data["name"])
```