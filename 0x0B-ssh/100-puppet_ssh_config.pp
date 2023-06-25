# set up your client SSH configuration file so that you can connect to a server without typing a password

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "\n\
             IdentityFile ~/.ssh/school\n\
             PasswordAuthentication no\n",
  }