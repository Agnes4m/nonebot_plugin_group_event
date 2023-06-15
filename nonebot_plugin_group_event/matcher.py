from nonebot import get_bot
from nonebot import on_command,on_notice
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
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.typing import T_State

from pathlib import Path
import random

from .notice import (
    poke_event,
    upload_files_event,
    user_decrease_event,
    user_increase_event,
    admin_change_event,
    red_packet_event
    )

async def _is_poke(bot: Bot, event: Event, state: T_State) -> bool:
    """获取戳一戳状态"""
    return isinstance(event, PokeNotifyEvent) and event.is_tome()


async def _is_honor(bot: Bot, event: Event, state: T_State) -> bool:
    """获取群荣誉变更"""
    return isinstance(event, HonorNotifyEvent)


async def _is_checker(bot: Bot, event: Event, state: T_State) -> bool:
    """获取文件上传"""
    return isinstance(event, GroupUploadNoticeEvent)


async def _is_user_decrease(bot: Bot, event: Event, state: T_State) -> bool:
    """群成员减少"""
    return isinstance(event, GroupDecreaseNoticeEvent)


async def _is_user_increase(bot: Bot, event: Event, state: T_State) -> bool:
    """群成员增加"""
    return isinstance(event, GroupIncreaseNoticeEvent)


async def _is_admin_change(bot: Bot, event: Event, state: T_State) -> bool:
    """管理员变动"""
    return isinstance(event, GroupAdminNoticeEvent)


async def _is_red_packet(bot: Bot, event: Event, state: T_State) -> bool:
    """红包运气王"""
    return isinstance(event, LuckyKingNotifyEvent)


notice = on_notice(_is_poke, priority=50, block=True)
honor = on_notice(_is_honor, priority=50, block=True)
upload_files = on_notice(_is_checker, priority=50, block=True)
user_decrease = on_notice(_is_user_decrease, priority=50, block=True)
user_increase = on_notice(_is_user_increase, priority=50, block=True)
admin_change = on_notice(_is_admin_change, priority=50, block=True)
red_packet = on_notice(_is_red_packet, priority=50, block=True)

@notice.handle()
async def _(bot:Bot,event:PokeNotifyEvent,matcher: Matcher):
    await poke_event(bot,event,matcher)
    
@upload_files.handle()
async def _(bot:Bot,event:HonorNotifyEvent,matcher: Matcher):
    await upload_files_event(bot,event,matcher)
    
@user_decrease.handle()
async def _(bot:Bot,event:HonorNotifyEvent,matcher: Matcher):
    await user_decrease_event(bot,event,matcher) 
    
@user_increase.handle()
async def _(bot:Bot,event:HonorNotifyEvent,matcher: Matcher):
    await user_increase_event(bot,event,matcher) 
       
@admin_change.handle()
async def _(bot:Bot,event:HonorNotifyEvent,matcher: Matcher):
    await admin_change_event(bot,event,matcher)  
      
@red_packet.handle()
async def _(bot:Bot,event:HonorNotifyEvent,matcher: Matcher):
    await red_packet_event(bot,event,matcher)    
