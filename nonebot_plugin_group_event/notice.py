
from nonebot import on_notice
from nonebot.adapters.onebot.v11 import (
    Bot, Event, PokeNotifyEvent,
    HonorNotifyEvent,
    GroupUploadNoticeEvent,
    GroupDecreaseNoticeEvent,
    GroupIncreaseNoticeEvent,
    GroupAdminNoticeEvent,
    LuckyKingNotifyEvent,
    MessageSegment,
    Message
)
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.matcher import Matcher

from datetime import datetime
from pathlib import Path
import random

from .config import all_config
from .utils import get_avatar

poke_admin = all_config.config.poke_admin
poke_path = Path().joinpath('data/group_event/poke')
poke_path.joinpath('img').mkdir(parents=True, exist_ok=True)

poke_img_list = []
for one_img in poke_path.joinpath('img').rglob('*'):
    if str(one_img).endswith({'.png','.jpg','.jpeg','.webp','.gif','.svg'}):
        poke_img_list.append(str(one_img)) 
    else:
        pass

if not poke_path.joinpath('poke.txt').is_file():
    with open(poke_path.joinpath('poke.txt'),mode='w',encoding='utf-8') as f:
        f.write('不要戳我啦')
    poke_text_list = ['不要戳我啦']
else:
    with open(poke_path.joinpath('poke.txt'),mode='r',encoding='utf-8') as f:
        poke_text_txt = f.read()
    poke_text_list = poke_text_txt.split('/n')


async def poke_event(bot :Bot, event :PokeNotifyEvent ,matcher: Matcher):
    group_id = event.group_id
    if group_id == None or not event.is_tome:
        logger.info('忽略私聊')
        await matcher.finish()
    # 判断黑白名单是否允许输出
    if poke_admin.w_or_b:
        if group_id not in poke_admin.w_group_id:
            logger.info('本群不属于白名单，忽略戳戳')
            await matcher.finish()
    else:
        if group_id in poke_admin.b_group_id:
            logger.info('本群属于白名单，忽略戳戳')
            await matcher.finish()
    
    # 判断输出类型
    if poke_admin.poke:
            await matcher.send(Message([
        MessageSegment("poke",  {
           "qq": f"{event.user_id}"
       })
    ]))
    
    if poke_admin.img and poke_admin.text:
        await matcher.finish(MessageSegment.image(random.choice(poke_img_list)) + random.choice(poke_text_list))
    elif poke_admin.img and not poke_admin.text:
        await matcher.finish(MessageSegment.image(random.choice(poke_img_list)))
    elif not poke_admin.img and poke_admin.text:
        await matcher.finish(random.choice(poke_text_list))
    else:
        logger.warning('你没有放任何可以输出的信息')
        await matcher.finish()


async def upload_files_event():
    pass

async def user_decrease_event(bot: Bot, event: GroupDecreaseNoticeEvent, matcher: Matcher):
    op = await bot.get_group_member_info(group_id=event.group_id, user_id=event.operator_id)
    casualty_name = (await bot.get_stranger_info(user_id=event.user_id)).get("nickname")
    op_name = op['card'] if op.get('card') else op['nickname']
    e_time = datetime.fromtimestamp(event.time).strftime("%Y-%m-%d %H:%M:%S")
    avatar = get_avatar(event.user_id)
    farewell_words = "感谢/o给/n送上的飞机，谢谢/o"
    farewell_self_words = "/n离群出走/n"
    # TODO 为以后自定义欢送词做准备
    if event.operator_id != event.user_id:
        reply = f"🛫 成员变动\n {farewell_words.replace('/o', f' {op_name} ').replace('/n', f' {casualty_name} ')}"
        reply += MessageSegment.image(avatar) + f" \n {e_time}\n"
    else:
        reply = f"🛫 成员变动\n {farewell_self_words.replace('/n', f' {casualty_name} ')}"
    await matcher.finish(reply)
    
async def user_increase_event():
    pass

async def admin_change_event():
    pass

async def red_packet_event():
    pass