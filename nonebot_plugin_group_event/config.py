
from pathlib import Path
from typing import List

from pydantic import BaseModel,Field
from ruamel import yaml

CONFIG_PATH = Path() / 'data' / 'group_event' / 'config.yml'
CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)

class Poke_mode(BaseModel):
    img :bool = Field(False, alias='图片')
    text :bool = Field(False, alias='文字')
    poke :bool = Field(True, alias='反击戳戳')

class GROUP_ADMIN(BaseModel):
    able :bool = Field(True, alias='是否启用此功能')
    w_or_b :bool = Field(False, alias='是否启用白名单')
    b_group_id :List[int] = Field([114514], alias='黑名单组')
    w_group_id :List[int] = Field([9191810], alias='白名单组')

class GROUP_EVENT(BaseModel):
    total_enable: bool = Field(True, alias='是否全局启用功能')
    poke_envet: Poke_mode = Field(Poke_mode(),alias='戳一戳事件')
    poke_admin: GROUP_ADMIN = Field(GROUP_ADMIN(),alias='戳一戳管理')
    
    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.__fields__:
                self.__setattr__(key, value)


class GROUP_EVENT_CONFIG:

    def __init__(self):
        self.file_path = CONFIG_PATH
        if self.file_path.exists():
            self.config = GROUP_EVENT.parse_obj(
                yaml.load(self.file_path.read_text(encoding='utf-8'), Loader=yaml.Loader))
        else:
            self.config = GROUP_EVENT()
        self.save()


    @property
    def config_list(self) -> List[str]:
        return list(self.config.dict(by_alias=True).keys())

    def save(self):
        with self.file_path.open('w', encoding='utf-8') as f:
            yaml.dump(
                self.config.dict(by_alias=True),
                f,
                indent=2,
                Dumper=yaml.RoundTripDumper,
                allow_unicode=True)
     

# global  
all_config = GROUP_EVENT_CONFIG()

async def Above():
    """是否全局开启"""
    return all_config.config.total_enable
            