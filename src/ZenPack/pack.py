import platform, warnings

from typing import Any

class Pack():
    def __init__(self,
            name,
            description = "",
            version = "v1.0",
            os = None,
            install = [],
            build = [],
            configure = [],
            controller = None,
            dependency = [],
            test = []
        ) -> None:
        self.name = name
        self.description = description
        self.version = version
        self.os = os
        self.install = install
        self.build = build
        self.configure = configure
        self.controller = controller
        self.dependency = dependency
        self.test = test

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def check_os_and_run(self, routine):
        if platform.system() == self.os:
            return routine()
        else:
            return f"[ SKIPPING ] {self.name}"

    def routine(self, ):
        log = {
            "install" : {},
            "build" : {},
            "configure" : {},
            "controller" : None,
            "dependency" : {},
            "test" : {},
        }

        # dependency
        for dependency in self.dependency:
            log["dependency"][dependency.__name__] = self.check_os_and_run(dependency)

            if log["dependency"][dependency.__name__] is not True:
                warnings.warn(f"[ FAILED ] Building dependency {dependency.__name__} from pack {self.name}")
                return log

        # install
        for installer in self.install:
            log["install"][installer.__name__] = self.check_os_and_run(installer)

        # build
        for builder in self.build:
            log["build"][builder.__name__] = self.check_os_and_run(builder)

        # configure
        for configure in self.configure:
            log["configure"][configure.__name__] = self.check_os_and_run(configure)

        # controller
        log["controller"] = self.check_os_and_run(self.controller)

        return log