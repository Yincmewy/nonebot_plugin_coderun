from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import MessageEvent, Message, Bot, GroupMessageEvent
import re
from .runcode import code

runcode = code()
command = on_command("run", aliases={"code", "运行"}, priority=5, block=False)


@command.handle()
async def main(bot: Bot, event: MessageEvent, args: Message = CommandArg()):
    code = args.extract_plain_text()
    if not code:
        await command.finish(
            "请输入运行语言和代码...\n目前支持的语言有:\nkotlin/java/lua/nodejs/go/swift/rust/ruby/c#/c++/c/py/php")
    split = re.findall("(.+?)[\r\n](\n)([\s\S]*)", code)
    try:
        await command.finish(await runcode.run(split[0][0],split[0][2]))
    except IndexError:
        await command.finish("不支持的语言\n目前仅支持\nkotlin/java/lua/nodejs/go/swift/rust/ruby/c#/c++/c/py/php\n请输入全称")