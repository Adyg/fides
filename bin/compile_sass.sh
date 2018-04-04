#!/bin/bash
cd /home/fides/src/static
printf "Compiling SASS ...\n"
bundler
bundler exec compass compile