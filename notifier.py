#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import html
import pickle
import notify2
import argparse

notify2.init("mocp-notifier")


def show_message(subj, body, icon='audio-speakers', timeout=3000,
                 dump_id_file='/tmp/pymocp.id'):
    wn = None
    try:
        wn = pickle.load(open(dump_id_file, "rb"))
    except:
        wn = notify2.Notification('')

    wn.set_timeout(timeout)
    wn.update(subj, body, icon)
    wn.show()
    pickle.dump(wn, open(dump_id_file, "wb"))


if __name__ == '__main__':
    def parse_args():
        def escape_str(s):
            return html.escape(s)
        parser = argparse.ArgumentParser()
        parser.add_argument('-a', '--artist', type=escape_str)
        parser.add_argument('-s', '--song', type=escape_str)
        parser.add_argument('-r', '--album', type=escape_str)
        parser.add_argument('-f', '--file', type=escape_str, required=True)
        parser.add_argument('-i', '--icon', type=escape_str, default='audio-x-generic')
        parser.add_argument('-t', '--timeout', type=int, default=5000)
        return parser, parser.parse_args()

    parser, args = parse_args()

    title = "Сейчас играет:"
    wn_obj = os.path.abspath(os.path.join(__file__, os.pardir, 'notify.id'))

    if not (args.artist and args.song):
        filename = os.path.splitext(args.file)[0]
        filename = os.path.basename(filename)
        show_message(title, filename, args.icon, args.timeout, wn_obj)
    else:
        album = ''
        if args.album:
            album = '(%s)' % args.album
        song = "<b>Артист:</b> <i>%s</i>\n<b>Трек:</b> <i>%s</i> %s" % (
            args.artist, args.song, album)
        show_message(title, song, args.icon, args.timeout, wn_obj)
    sys.exit(0)
