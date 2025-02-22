#!/bin/bash

bash

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/$1


