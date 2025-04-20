#!/bin/bash

# Start SSH service
/usr/sbin/sshd

# Keep container running indefinitely
tail -f /dev/null