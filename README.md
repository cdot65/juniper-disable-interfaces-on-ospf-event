# Disable interfaces on event

This is a proof of concept script that will disable interfaces ge-0/0/0 and ge-0/0/1 when an OSPF neighbor is lost.

## JunOS configuration

You will need to have the appropriate configuration running on your device

```junos
event-options {
    policy SHUTDOWN_IFACE_PYTHON {
        events rpd_ospf_nbrdown;
        then {
            event-script app.py;
        }
    }
    event-script {
        file app.py {
            python-script-user cdot;
        }
    }
}
```

## Script

Simplicity is always best when you can get away with it

```python
#!/usr/bin/env python3

# import PyEZ packages from local system
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import jcs

# with loop will be executed when event is triggered
with Device() as router:
    with Config(router) as update_config:
        update_config.load("set interfaces ge-0/0/0 disable", format="set")
        update_config.load("set interfaces ge-0/0/1 disable", format="set")
        update_config.commit(comment="OSPF neighbor down, disabling physical interfaces through event script", timeout=300)
```
