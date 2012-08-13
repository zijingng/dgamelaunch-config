import logging
try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

dgl_mode = True

bind_nonsecure = True # Set to false to only use SSL
bind_address = "209.222.93.171"
bind_port = 80

logging_config = {
    "filename": "/crawl-master/webserver/run/webtiles.log",
    "level": logging.INFO,
    "format": "%(asctime)s %(levelname)s: %(message)s"
}

password_db = "/dgldir/dgamelaunch.db"

static_path = "/crawl-master/webserver/static"
template_path = "/crawl-master/webserver/templates/"

# Path for server-side unix sockets (to be used to communicate with crawl)
server_socket_path = None # Uses global temp dir

# Server name, so far only used in the ttyrec metadata
server_id = "cszo"

# Disable caching of game data files
game_data_no_cache = True

# Watch socket dirs for games not started by the server
watch_socket_dirs = True

# Game configs
# %n in paths is replaced by the current username
games = OrderedDict([
    ("dcss-git", dict(
        name = "DCSS trunk",
        crawl_binary = "/bin/crawl-git-launcher.sh",
        rcfile_path = "/dgldir/rcfiles/crawl-git/",
        macro_path = "/dgldir/rcfiles/crawl-git/",
        morgue_path = "/dgldir/morgue/%n/",
        inprogress_path = "/dgldir/inprogress/crawl-git/",
        ttyrec_path = "/dgldir/ttyrec/%n/",
        socket_path = "/crawl-master/webserver/sockets",
        client_path = "/crawl-master/crawl-latest/data/web/")),
    ("spr-git", dict(
        name = "Sprint trunk",
        crawl_binary = "/bin/crawl-git-launcher.sh",
        rcfile_path = "/dgldir/rcfiles/crawl-git/",
        macro_path = "/dgldir/rcfiles/crawl-git/",
        morgue_path = "/dgldir/morgue/%n/",
        inprogress_path = "/dgldir/inprogress/crawl-git-sprint/",
        ttyrec_path = "/dgldir/ttyrec/%n/",
        socket_path = "/crawl-master/webserver/sockets",
        client_path = "/crawl-master/crawl-latest/data/web/",
        options = ["-sprint"])),
    ("zd-git", dict(
        name = "Zot Defence trunk",
        crawl_binary = "/bin/crawl-git-launcher.sh",
        rcfile_path = "/dgldir/rcfiles/crawl-git/",
        macro_path = "/dgldir/rcfiles/crawl-git/",
        morgue_path = "/dgldir/morgue/%n/",
        inprogress_path = "/dgldir/inprogress/crawl-git-zotdef/",
        ttyrec_path = "/dgldir/ttyrec/%n/",
        socket_path = "/crawl-master/webserver/sockets",
        client_path = "/crawl-master/crawl-latest/data/web/",
        options = ["-zotdef"])),
    ("tut-git", dict(
        name = "Tutorial trunk",
        crawl_binary = "/bin/crawl-git-launcher.sh",
        rcfile_path = "/dgldir/rcfiles/crawl-git/",
        macro_path = "/dgldir/rcfiles/crawl-git/",
        morgue_path = "/dgldir/morgue/%n/",
        inprogress_path = "/dgldir/inprogress/crawl-git-tut/",
        ttyrec_path = "/dgldir/ttyrec/%n/",
        socket_path = "/crawl-master/webserver/sockets",
        client_path = "/crawl-master/crawl-latest/data/web/",
        options = ["-tutorial"])),

    ("dcss-0.11", dict(
        name = "DCSS 0.11",
        crawl_binary = "/usr/games/crawl-0.11",
        rcfile_path = "/dgldir/rcfiles/crawl-0.11/",
        macro_path = "/dgldir/rcfiles/crawl-0.11/",
        morgue_path = "/dgldir/morgue/%n/",
        inprogress_path = "/dgldir/inprogress/crawl-11/",
        ttyrec_path = "/dgldir/ttyrec/%n/",
        socket_path = "/crawl-master/webserver/sockets",
        client_path = "/crawl-master/crawl-0.11/data/web/")),
    ("spr-0.11", dict(
        name = "Sprint 0.11",
        crawl_binary = "/usr/games/crawl-0.11",
        rcfile_path = "/dgldir/rcfiles/crawl-0.11/",
        macro_path = "/dgldir/rcfiles/crawl-0.11/",
        morgue_path = "/dgldir/morgue/%n/",
        inprogress_path = "/dgldir/inprogress/crawl-11-sprint/",
        ttyrec_path = "/dgldir/ttyrec/%n/",
        socket_path = "/crawl-master/webserver/sockets",
        client_path = "/crawl-master/crawl-0.11/data/web/",
        options = ["-sprint"])),
    ("zd-0.11", dict(
        name = "Zot Defence 0.11",
        crawl_binary = "/usr/games/crawl-0.11",
        rcfile_path = "/dgldir/rcfiles/crawl-0.11/",
        macro_path = "/dgldir/rcfiles/crawl-0.11/",
        morgue_path = "/dgldir/morgue/%n/",
        inprogress_path = "/dgldir/inprogress/crawl-11-zotdef/",
        ttyrec_path = "/dgldir/ttyrec/%n/",
        socket_path = "/crawl-master/webserver/sockets",
        client_path = "/crawl-master/crawl-0.11/data/web/",
        options = ["-zotdef"])),
    ("tut-0.11", dict(
        name = "Tutorial 0.11",
        crawl_binary = "/usr/games/crawl-0.11",
        rcfile_path = "/dgldir/rcfiles/crawl-0.11/",
        macro_path = "/dgldir/rcfiles/crawl-0.11/",
        morgue_path = "/dgldir/morgue/%n/",
        inprogress_path = "/dgldir/inprogress/crawl-11-tut/",
        ttyrec_path = "/dgldir/ttyrec/%n/",
        socket_path = "/crawl-master/webserver/sockets",
        client_path = "/crawl-master/crawl-0.11/data/web/",
        options = ["-tutorial"])),

    ("dcss-0.10", dict(
        name = "DCSS 0.10",
        crawl_binary = "/usr/games/crawl-0.10",
        rcfile_path = "/dgldir/rcfiles/crawl-0.10/",
        macro_path = "/dgldir/rcfiles/crawl-0.10/",
        morgue_path = "/dgldir/morgue/%n/",
        inprogress_path = "/dgldir/inprogress/crawl-10/",
        ttyrec_path = "/dgldir/ttyrec/%n/",
        socket_path = "/crawl-master/webserver/sockets",
        client_path = "/crawl-master/crawl-0.10/data/web/")),
    ("spr-0.10", dict(
        name = "Sprint 0.10",
        crawl_binary = "/usr/games/crawl-0.10",
        rcfile_path = "/dgldir/rcfiles/crawl-0.10/",
        macro_path = "/dgldir/rcfiles/crawl-0.10/",
        morgue_path = "/dgldir/morgue/%n/",
        inprogress_path = "/dgldir/inprogress/crawl-10-sprint/",
        ttyrec_path = "/dgldir/ttyrec/%n/",
        socket_path = "/crawl-master/webserver/sockets",
        client_path = "/crawl-master/crawl-0.10/data/web/",
        options = ["-sprint"])),
    ("zd-0.10", dict(
        name = "Zot Defence 0.10",
        crawl_binary = "/usr/games/crawl-0.10",
        rcfile_path = "/dgldir/rcfiles/crawl-0.10/",
        macro_path = "/dgldir/rcfiles/crawl-0.10/",
        morgue_path = "/dgldir/morgue/%n/",
        inprogress_path = "/dgldir/inprogress/crawl-10-zotdef/",
        ttyrec_path = "/dgldir/ttyrec/%n/",
        socket_path = "/crawl-master/webserver/sockets",
        client_path = "/crawl-master/crawl-0.10/data/web/",
        options = ["-zotdef"])),
    ("tut-0.10", dict(
        name = "Tutorial 0.10",
        crawl_binary = "/usr/games/crawl-0.10",
        rcfile_path = "/dgldir/rcfiles/crawl-0.10/",
        macro_path = "/dgldir/rcfiles/crawl-0.10/",
        morgue_path = "/dgldir/morgue/%n/",
        inprogress_path = "/dgldir/inprogress/crawl-10-tut/",
        ttyrec_path = "/dgldir/ttyrec/%n/",
        socket_path = "/crawl-master/webserver/sockets",
        client_path = "/crawl-master/crawl-0.10/data/web/",
        options = ["-tutorial"])),
])

dgl_status_file = "/crawl-master/webserver/run/status"

# Set to None not to read milestones
milestone_file = "/crawl-master/crawl-git/saves/milestones"

status_file_update_rate = 5

recording_term_size = (80, 24)

max_connections = 200

# Script to initialize a user, e.g. make sure the paths
# and the rc file exist. This is not done by the server
# at the moment.
init_player_program = "/bin/init-webtiles.sh"

#ssl_options = None # No SSL
ssl_options = {
    "certfile": "/etc/ssl/private/s-z.org.crt",
    "keyfile": "/etc/ssl/private/s-z.org.key",
    "ca_certs": "/etc/ssl/private/sub.class1.server.ca.pem"
}
ssl_address = "209.222.93.171"
ssl_port = 443

connection_timeout = 600
max_idle_time = 5 * 60 * 60

# Seconds until stale HTTP connections are closed
# This needs a patch currently not in mainline tornado.
http_connection_timeout = 600

kill_timeout = 10 # Seconds until crawl is killed after HUP is sent

nick_regex = r"^[a-zA-Z0-9]{3,20}$"
max_passwd_length = 20

# crypt() algorithm, e.g. "1" for MD5 or "6" for SHA-512; see crypt(3).
# If false, use traditional DES (but then only the first eight characters
# are significant).
crypt_algorithm = "6"
# If crypt_algorithm is true, the length of the salt string to use.  If
# crypt_algorithm is false, a two-character salt is used.
crypt_salt_length = 16

login_token_lifetime = 7 # Days

uid = 1002  # If this is not None, the server will setuid to that (numeric) id
gid = 1002  # after binding its sockets.

umask = None # e.g. 0077

chroot = "/home/crawl/DGL"

pidfile = "/crawl-master/webserver/run/webtiles.pid"
daemon = True # If true, the server will detach from the session after startup