# -*- coding: utf-8 -*-
from nonebot.plugin import PluginMetadata
from nonebot import on_notice
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import (
    Bot, Event, PokeNotifyEvent,
    HonorNotifyEvent,
    GroupUploadNoticeEvent,
    GroupDecreaseNoticeEvent,
    GroupIncreaseNoticeEvent,
    GroupAdminNoticeEvent,
    LuckyKingNotifyEvent,
    MessageSegment
)


from nonebot.matcher import Matcher
from nonebot.plugin import on_notice
from nonebot.typing import T_State

import asyncio
from datetime import datetime

from .matcher import *

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





# @honor.handle()
# async def _(bot: Bot, event: HonorNotifyEvent, state: T_State, matcher: Matcher):
#     honor_type = event.honor_type
#     uid = event.user_id
#     reply = ""
#     honor_map = {"performer": ["🔥", "群聊之火"], "emotion": ["🤣", "快乐源泉"]}
#     # 龙王
#     u_info = await bot.get_group_member_info(user_id=event.user_id)
#     u_name = u_info["card"] if u_info["card"] else u_info["nickname"]
#     if honor_type == "talkative":
#         if uid == bot.self_id:
#             reply = "💦 新龙王诞生，原来是我自己~"
#         else:
#             reply = f"💦 恭喜 {u_name} 荣获龙王标识~"
#     for key, value in honor_map.items():
#         if honor_type == key:
#             reply = f"{value[0]} 恭喜{u_name}荣获【{value[1]}】标识~"
#     await fi(matcher, reply)


# @upload_files.handle()
# async def _(bot: Bot, event: GroupUploadNoticeEvent, state: T_State, matcher: Matcher):
#     # TODO 在本地做记录
#     ...


# @user_decrease.handle()
# async def _(bot: Bot, event: GroupDecreaseNoticeEvent, state: T_State, matcher: Matcher):
#     op = await bot.get_group_member_info(group_id=event.group_id, user_id=event.operator_id)
#     casualty_name = (await bot.get_stranger_info(user_id=event.user_id)).get("nickname")
#     op_name = op['card'] if op.get('card') else op['nickname']
#     e_time = datetime.fromtimestamp(event.time).strftime("%Y-%m-%d %H:%M:%S")
#     avatar = get_avatar(event.user_id)
#     farewell_words = "感谢/o给/n送上的飞机，谢谢/o"
#     farewell_self_words = "/n离群出走/n"
#     # TODO 为以后自定义欢送词做准备
#     if event.operator_id != event.user_id:
#         reply = f"🛫 成员变动\n {farewell_words.replace('/o', f' {op_name} ').replace('/n', f' {casualty_name} ')}"
#         reply += MessageSegment.image(avatar) + f" \n {e_time}\n"
#     else:
#         reply = f"🛫 成员变动\n {farewell_self_words.replace('/n', f' {casualty_name} ')}"
#     await fi(matcher, reply)


# @user_increase.handle()
# async def _(bot: Bot, event: GroupIncreaseNoticeEvent, state: T_State, matcher: Matcher):
#     await asyncio.sleep(1)
#     avatar = get_avatar(event.user_id)
#     new_be = (await bot.get_group_member_info(group_id=event.group_id, user_id=event.user_id))['nickname']
#     wel_words = "欢迎/n加入"
#     # TODO 为以后自定义欢迎词做准备
#     reply = "✨ 成员变动\n"+MessageSegment.image(avatar) + MessageSegment.at(event.user_id) + f"\n {wel_words.replace('/n', f' {new_be} ')}\n "
#     await fi(matcher, reply)


# @admin_change.handle()
# async def _(bot: Bot, event: GroupAdminNoticeEvent, state: T_State, matcher: Matcher):
#     reply = ""
#     sub_type = event.sub_type
#     uid = event.user_id
#     user = await bot.get_group_member_info(group_id=event.group_id, user_id=uid)
#     u_name = user['card'] if user.get('card') else user['nickname']
#     cong_words = "恭喜/n成为管理"
#     re_words = "Ops! /n不再是本群管理"
#     if uid == bot.self_id:
#         if sub_type == "set":
#             reply = f"🚔 管理员变动\n{cong_words.replace('/n', '我')}"
#         if sub_type == "unset":
#             reply = f"🚔 管理员变动\n{re_words.replace('/n', '我')}"
#     else:
#         if sub_type == "set":
#             reply = f"🚔 管理员变动\n{cong_words.replace('/n', f' {u_name} ')}"
#         if sub_type == "unset":
#             reply = f"🚔  管理员变动\n{re_words.replace('/n', f' {u_name} ')}"
#     await fi(matcher, reply)



