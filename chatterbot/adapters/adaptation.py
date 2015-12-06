from chatterbot.utils.module_loading import import_module


class Adaptation(object):
    """
    An adaptation is a base object that holds and
    configures the three main adapter types.
    """

    class adapters(object):
        storage_adapter = None
        logic_adapter = None
        io_adapter = None

    def __init__(self, **kwargs):

        # Default adapters
        default_storage_adapter = "chatterbot.adapters.storage.JsonDatabaseAdapter"
        default_logic_adapter = "chatterbot.adapters.logic.ClosestMatchAdapter"
        default_io_adapter = "chatterbot.adapters.io.TerminalAdapter"

        storage_adapter = kwargs.get("storage_adapter", default_storage_adapter)
        logic_adapter = kwargs.get("logic_adapter", default_logic_adapter)
        io_adapter = kwargs.get("io_adapter", default_io_adapter)

        StorageAdapter = import_module(storage_adapter)
        self.adapters.storage_adapter = StorageAdapter(self.adapters, **kwargs)

        LogicAdapter = import_module(logic_adapter)
        self.adapters.logic_adapter = LogicAdapter(self.adapters, **kwargs)

        IOAdapter = import_module(io_adapter)
        self.adapters.io_adapter = IOAdapter(self.adapters, **kwargs)

        PluginChooser = import_module("chatterbot.adapters.plugins.PluginChooser")
        self.plugin_chooser = PluginChooser(**kwargs)

    @property
    def storage(self):
        return self.adapters.storage_adapter

    @property
    def logic(self):
        return self.adapters.logic_adapter

    @property
    def io(self):
        return self.adapters.io_adapter

