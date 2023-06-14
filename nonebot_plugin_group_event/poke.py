
from nonebot import on_notice
from nonebot.adapters.onebot.v11 import (
    PokeNotifyEvent,
    Message,
    MessageSegment,
    Bot,
    )
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.matcher import Matcher

from pathlib import Path
import random

from .config import all_config

poke_event = all_config.config.poke_envet
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

poke_ = on_notice(rule=to_me())
@poke_.handle()
async def _(bot :Bot, event :PokeNotifyEvent ,matcher: Matcher):
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
    if poke_event.poke:
            await matcher.send(Message([
        MessageSegment("poke",  {
           "qq": f"{event.user_id}"
       })
    ]))
    
    if poke_event.img and poke_event.text:
        await matcher.finish(MessageSegment.image(random.choice(poke_img_list)) + random.choice(poke_text_list))
    elif poke_event.img and not poke_event.text:
        await matcher.finish(MessageSegment.image(random.choice(poke_img_list)))
    elif not poke_event.img and poke_event.text:
        await matcher.finish(random.choice(poke_text_list))
    else:
        logger.warning('你没有放任何可以输出的信息')
        await matcher.finish()
