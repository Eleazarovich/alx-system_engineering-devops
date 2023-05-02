# this script uses puppet to make changes to the config file
# to set up client ssh config file so that you can connect to
# a server without typing a password

include stdlib
file_line { 'Declare identity file':
    path    => '/etc/ssh/ssh_config',
    line    => '    IdentityFile ~/.ssh/school',
    replace => true,
}

file_line { 'Turn off passwd auth':
    path    => '/etc/ssh/ssh_config',
    line    => '    PasswordAuthentication no',
    replace => true,
}
