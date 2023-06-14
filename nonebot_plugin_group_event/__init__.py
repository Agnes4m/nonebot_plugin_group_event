# -*- coding: utf-8 -*-
from nonebot.plugin import PluginMetadata

from .poke import poke_event

__version__ = "0.0.1"
__plugin_meta__ = PluginMetadata(
    name="群聊助手",
    description='简单互动群聊事件处理',
    usage='q群聊简单事件处理',
    type="application",
    homepage="https://github.com/Agnes4m/nonebot_plugin_group_event",
    supported_adapters={"~onebot.v11"},
    extra={
        "version": __version__,
        "author": "Agnes4m <Z735803792@163.com>",
    },
)
