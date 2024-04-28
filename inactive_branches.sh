#!/bin/bash

# Deletes all remote branches that have been merged, and the last activity
# was more than 1 month prior

git fetch --all --prune

for k in $(git branch -r | grep -v "\->" | sed /\*/d); do
	if [ -z "$(git log -1 --since='1 month ago' -s $k)" ]; then
		echo "Deleting branch: $k"
	fi
done

