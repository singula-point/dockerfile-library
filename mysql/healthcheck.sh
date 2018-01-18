#!/bin/bash

if [ -f /mysql-init-complete ];
then
  mysqladmin --defaults-extra-file=/healthcheck.cnf ping
else
  exit 1
fi
