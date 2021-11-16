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
