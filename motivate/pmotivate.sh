#!/bin/bash

# Just some ASCII art for asthetics
printf "				 __  __       _   _            _        \n"
printf "				|  \/  | ___ | |_(_)_   ____ _| |_ ___  \n"
printf '				| |\/| |/ _ \| __| \ \ / / _` | __/ _ \ \n'
printf "				| |  | | (_) | |_| |\ V / (_| | ||  __/ \n"
printf "				|_|  |_|\___/ \__|_| \_/ \__,_|\__\___| \n"
printf "\n"

# The user wants to get motivated atleast once!
motivate
printf "\n"
printf "Hit enter to get more motivated or type 'done' if you're motivated enough!\n"
read INPUT_STRING

# After that, the user can keep asking for more motivation till he is absolutely psyched!
while [ "$INPUT_STRING" != "done" ]
do
  motivate
  printf "\n"
  printf "Hit enter to get more motivated or type 'done' if you're motivated enough!\n"
  read INPUT_STRING 
done

printf "\n"
printf "Now that you're motivated, 'Go get 'em Tiger!'\n"
