#!/usr/bin/env python

import json

if __name__ == '__main__':
    with open("Bookmarks_ubuntu", 'r') as f_ubuntu, \
            open("Bookmarks_win10", 'r') as f_win:
        bookmark_ubuntu = f_ubuntu.read()
        bookmark_win = f_win.read()

    bookmark_ubuntu = json.loads(bookmark_ubuntu)
    bookmark_win = json.loads(bookmark_win)

    """
    |-- bookmark_bar
    |   |-- children
    |   |   |-- data_added  # no folder
    |   |   |-- guid
    |   |   |-- id
    |   |   |-- meta_info
    |   |       |-- last_visited_desktop
    |   |   |-- name
    |   |   |-- sync_transaction_version
    |   |   |-- type
    |   |   |__ url
    |   |-- date_added
    |   |-- date_modified
    |   |-- guid
    |   |-- id
    |   |-- name
    |   |-- sync_transaction
    |   |__ type
    |-- other
    |-- sync_transaction_version
    |__ synced
    """

    for i in bookmark_win["roots"]:
        print(i)
