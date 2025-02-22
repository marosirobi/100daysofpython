#!/bin/bash

start "C:\Program Files\Git\bin\sh.exe"

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/$1