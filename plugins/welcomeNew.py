import sys
from nonebot import on_notice, NoticeSession
import config

sys.path.append('..')


# 函数注册为群成员通知处理器
@on_notice('group_increase')
async def _(session: NoticeSession):
    if session.event.group_id == config.GROUP_ID:
        await session.send(f'欢迎新成员{session.event.user_id}加入ReoNa应援团！请认真阅读置顶群公告。\n'
                           f'相关音视频和图像资源已上传到群文件、群相册和资源站中，'
                           f'在取用的同时请遵守未经许可不得向外转载的规定，感谢配合。')
