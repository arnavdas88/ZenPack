from ZenPack import Pack

from .install import installA, installB, installC
from .build import buildA, buildB
from .config import configureA, configureB
from .controller import controller
from .test import testA, testB

self = Pack(
    name = "Sysmon",
    os="Linux",
    install = [installA, installB, installC],
    build = [buildA, buildB],
    configure = [configureA, configureB],
    controller = controller,
    dependency = [],
    test = [testA, testB]
)


if __name__ == "__main__":
    pass

