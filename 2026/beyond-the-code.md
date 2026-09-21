## Beyond the Code

Browse the source code of a well-known project (e.g., Redis or curl). Find examples of some of the comment types mentioned in the lecture: a useful TODO, a reference to external documentation, a “why not” comment explaining an avoided approach, or a hard-learned lesson. What would be lost if that comment was not there?

- From the official Mozilla FireFox GitHub repository:

```
else:
                 try:
                     names.append(x509.IPAddress(ipaddress.ip_address(name)))
-                # TODO: specify specific exceptions here
-                except:  # noqa: E722
+                except ValueError:
                     names.append(x509.DNSName(name))
```
hello world! Another test