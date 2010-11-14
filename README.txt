python-continuum - Consistent hashing
========================================================================

Copyright (c) 2010 by Joachim Bauch, mail@joachim-bauch.de
http://www.joachim-bauch.de/projects/python-continuum/

python-continuum provides a function to do consistent hashing. See
wikipedia [1]_ for more informations about this technique.

First we need the continuum object that serves as storage for server
informations and can later be used to resolve keys::

	>>> from continuum import Continuum
	>>> c = Continuum()

Empty continuums obviously can't be queried::

	>>> c.resolve('my-key1')
	Traceback (most recent call last):
	...
	IndexError: empty continuum

Add the server objects that are available as backends::

	>>> c.add_server('192.168.0.1', 8080)
	<Server "192.168.0.1:8080", capacity=1>
	>>> c.add_server('192.168.0.2', 8080)
	<Server "192.168.0.2:8080", capacity=1>

You can also specify different capacities of the server to priorize
them (this defaults to 1)::

	>>> c.add_server('192.168.0.3', 8080, 2)
	<Server "192.168.0.3:8080", capacity=2>

Server objects can also be removed::

	>>> server = c.add_server('192.168.0.4', 8080)
	>>> c.remove_server(server)
	>>> len(c)
	3

Please note that a server can only be added once::

	>>> c.add_server('192.168.0.2', 8080)
	Traceback (most recent call last):
	...
	TypeError: server already added

After all servers have been added, the continuum can be queried for the
server that should be used for a given (string) key::

	>>> c.resolve('my-first-key')
	<Server "192.168.0.1:8080", capacity=1>
	>>> c.resolve('my-other-key')
	<Server "192.168.0.3:8080", capacity=2>


.. [1] http://en.wikipedia.org/wiki/Consistent_hashing
