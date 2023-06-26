# 0x0C. Web server
### Concepts
### What is a Child Process?
Although it may sound like something out of a parenting handbook or a psychological journal, the term child process actually has nothing to do with human development. If you run a Unix or Linux dedicated server, you have likely encountered child processes without even knowing it. Therefore, it is good to know what child processes are and how they work.

A child process is a process created by another process. The creator process is properly called the “parent process”. The benefit of a child process is that it can start or stop at will without affecting the parent process. The child process is, however, is typically dependent on the parent process. If the parent process dies, the child process becomes an orphan process.

In normal server operations, the kernel may initiate child processes, and other programs, such as Apache, may have them as well. Apache creates child processes (or children, if you prefer) whenever the number of requests (web page accesses from users) exceeds the maximum allowed number of requests. When the maximum number of child process requests is exceeded, another child process spawns.

To view all running processes along with their child processes in a “tree” format, use the following command:

$ ps axf

For more information about child processes, see this [documentation](https://www.gnu.org/software/libc/manual/html_node/Processes.html#Processes).
## Resources
### Read or watch:

[* How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)

[* Nginx](https://en.wikipedia.org/wiki/Nginx)
[* How to Configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)

[* Root and sub domain](https://landingi.com/help/domains-vs-subdomains/)

[* HTTP requests](https://www.tutorialspoint.com/http/http_methods.htm)

[* HTTP redirection](https://moz.com/learn/seo/redirection)

[* Not found HTTP response code](https://en.wikipedia.org/wiki/HTTP_404)

[* Logs files on Linux](https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/)
### For reference:

[* RFC 7231 (HTTP/1.1)](https://datatracker.ietf.org/doc/html/rfc7231)

[* RFC 7540 (HTTP/2)](https://datatracker.ietf.org/doc/html/rfc7540)
### man or help:

* scp

* curl
### General
What is the main role of a web server

What is a child process

Why web servers usually have a parent process and child processes

What are the main HTTP requests
### DNS
What DNS stands for

What is DNS main role

### DNS Record Types
A

CNAME

TXT

MX
## Requirements
### General
Allowed editors: vi, vim, emacs

All your files will be interpreted on Ubuntu 16.04 LTS

All your files should end with a new line

A README.md file, at the root of the folder of the project, is mandatory

All your Bash script files must be executable

Your Bash script must pass Shellcheck (version 0.3.7) without any error

The first line of all your Bash scripts should be exactly #!/usr/bin/env bash

The second line of all your Bash scripts should be a comment explaining what is the script doing

You can’t use systemctl for restarting a process