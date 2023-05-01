# manifest that kills a process named killnow using puppet
exec { 'killmenow':
    command  => '/usr/bin/pkill killmenow',
    provider => 'shell',
    returns  => [0, 1],
}
