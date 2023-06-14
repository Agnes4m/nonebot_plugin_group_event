from pathlib import Path
from nonebot import require, load_plugin

dir_ = Path(__file__).parent
require('nonebot_plugin_apscheduler')
load_plugin(dir_.joinpath("nonebot_plugin_group_event"))