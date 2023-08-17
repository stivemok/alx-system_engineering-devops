# Fix web stack debuggig 4
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  notify  => Exec['nginx-restart'],
}

exec { 'nginx-restart':
  command     => 'nginx restart',
  path        => '/etc/init.d/',
  refreshonly => true,
}