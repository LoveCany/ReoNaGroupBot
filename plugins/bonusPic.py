import sys
from nonebot import on_command, CommandSession, permission
import config

sys.path.append('..')


@on_command('bonus', aliases=('特典', '特典图'), only_to_me=False)
async def bonusPic(session: CommandSession):
    if session.event.group_id == config.GROUP_ID:
        title = session.get('title')
        bonusPic = await getBonusPic(title, session.event.user_id)
        await session.send(bonusPic)


@bonusPic.args_parser
async def _(session: CommandSession):
    arg = session.current_arg_text.strip()
    if arg:
        session.state['title'] = arg
    if not arg:
        session.pause(f'[CQ:at,qq={session.event.user_id}]标题不能为空！')
        return
    session.state[session.current_key] = arg


async def getBonusPic(title: str, user_id: int) -> str:
    # 需要将resources文件夹下的bonusPic子文件夹复制到CoolQ Pro的data\image文件夹下以保证图片正常发送
    titleList = ['ELZA', 'SWEET HURT', 'forget-me-not', 'Prologue', 'Null']  # 对应标题名称
    for tmpTitle in titleList:
        if title.lower() == tmpTitle.lower():
            return f'[CQ:image,file=bonusPic/{tmpTitle}.jpg]'
    return f'[CQ:at,qq={user_id}]未找到对应标题，请确认拼写是否正确！'
