from typing import Any

x: Any = dict()
y: object = dict()

x.foo()
y.foo()
# error: "object" has no attribute "foo"
