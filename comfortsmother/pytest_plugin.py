import coverage


def pytest_addoption(parser):
    """Add options to control coverage."""

    group = parser.getgroup(
        'comfortsmother', 'comfortsmother reporting')
    group.addoption('--comfortsmother', action='append', default=[], metavar='path',
                    nargs='?', const=True, dest='comfortsmother_source',
                    help='measure coverage for filesystem path '
                    '(multi-allowed)')
    group.addoption('--comfortsmother-output', action='store', default='.comfortsmother',
                    help='output file for smother data. '
                         'default: .comfortsmother')


def pytest_configure(config):
    """Activate plugin if appropriate."""
    if config.getvalue('comfortsmother_source'):
        if not config.pluginmanager.hasplugin('_comfortsmother'):
            plugin = Plugin(config.option)
            config.pluginmanager.register(plugin, '_comfortsmother')


class Plugin(object):

    def __init__(self, options):
        self.coverage = coverage.coverage(
            source=options.comfortsmother_source,
        )

        # The unusual import statement placement is so that
        # smother's own test suite can measure coverage of
        # smother import statements
        self.coverage.start()
        from comfortsmother.control import ComfortSmother
        self.smother = ComfortSmother(self.coverage)

        self.output = options.comfortsmother_output
        self.first_test = True

    def pytest_runtest_setup(self, item):
        if self.first_test:
            self.first_test = False
            self.coverage.stop()
            self.smother.save_context("")
        self.smother.start()

    def pytest_runtest_teardown(self, item, nextitem):
        self.coverage.stop()
        self.smother.save_context(item.nodeid)

    def pytest_terminal_summary(self):
        self.smother.write(self.output)
