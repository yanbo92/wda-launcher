# -*- coding: utf-8 -*-
# @Time    : 2022/2/28 4:08 上午
# @Author  : yanbo92
# @File    : wda_launcher.py
from tidevice import Device
from tidevice._relay import relay
from threading import Thread
from argparse import ArgumentParser


def start_xctest(device, bundleid):
    device.xctest(fuzzy_bundle_id=bundleid)


def start_relay(device, local_port=8101):
    relay(device, local_port, 8100)


parser = ArgumentParser()
parser.add_argument("--udid", type=str, required=False, default="")
parser.add_argument("--port", type=int, required=False, default=8100)
parser.add_argument("--bundleid", type=str, required=False, default="com.*.WebDriverAgentRunner.xctrunner")
args = parser.parse_args()

if args.udid == "":
    d = Device()
else:
    d = Device(udid=args.udid)

t1 = Thread(target=start_xctest, args=(d, args.bundleid))
t1.start()
start_relay(device=d, local_port=args.port)
