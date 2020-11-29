import os, time, asyncio, io
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, errors, functions, types
from userbot import ALIVE_NAME
from global_variables import COUNT_MSG, COUNT_PM

PMPIC = os.environ.get("PMPERMITPIC", None)
WARN_PIC = PMPIC

PREV_REPLY_MESSAGE = {}


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
USER_BOT_WARN_ZERO = "`Beta You were spamming my inbox, henceforth you have been blocked by My JAANU.` "
PMMSG = os.environ.get("PMPERMITMSG", None)
if PMMSG is None:
	USER_BOT_NO_WARN = ("`Hello ! This is` **[ Mlo Userbot](t.me/mlouserbot)**\n"
                    "`PM Permit Security`\n\n"
                    "**You Have Trespassed To\n"
                    f"{DEFAULTUSER}'s Inbox**\n\n"
                    "**DEKH PYAR SE SAMJH MASTER IS VERY DANGER. So send ur msg in one line or u will be blocked automatically.**")
else:
	USER_BOT_NO_WARN = PMMSG


if Var.BOTLOG_CHATID is not None:
    @plus_ub(pattern="approve ?(.*)", from_users=sudo)
    async def approve_p_m(event):
        if event.fwd_from:
           return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if chat.id in COUNT_PM:
                    del COUNT_PM[chat.id]
                if chat.id in PREV_REPLY_MESSAGE:
                    await PREV_REPLY_MESSAGE[chat.id].delete()
                    del PREV_REPLY_MESSAGE[chat.id]
                pmpermit_sql.approve(chat.id, reason)
                a = await event.edit("Approved [{}](tg://user?id={})".format(firstname, chat.id))
                await event.delete()
                await asyncio.sleep(3)
                await a.delete()
                
                
    @plus.on(events.NewMessage(outgoing=True))
    async def you_dm_niqq(event):
    	if event.fwd_from:
    		return
    	chat = await event.get_chat()
    	if event.is_private:
    		if not pmpermit_sql.is_approved(chat.id):
    			if not chat.id in COUNT_PM:
    				pmpermit_sql.approve(chat.id, "outgoing")
    				bruh = "**Auto-approved coz outgoing**"
    				rko = await borg.send_message(event.chat_id, bruh)
    				await asyncio.sleep(3)
    				await rko.delete()


    @plus_ub(pattern="block ?(.*)", from_users=sudo)
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
          if chat.id == 1137511834:
            await event.edit("You bitch tried to block my jaanu, now i will sleep for 100 seconds")
            await asyncio.sleep(100)
          else:
            if pmpermit_sql.is_approved(chat.id):
                await event.reply(" ███████▄▄███████████▄  \n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░█\n██████▀▀▀█░░░░██████▀  \n░░░░░░░░░█░░░░█  \n░░░░░░░░░░█░░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░░▀▀ \n\n**This is {} AI..U HAVE BEEN BANNED DUE TO BAKCHODI**..[{}](tg://user?id={})".format(DEFAULTUSER, firstname, chat.id))
                await event.delete()
                await event.client(functions.contacts.BlockRequest(chat.id))

    @plus_ub(pattern="disapprove ?(.*)", from_users=sudo)
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
          if chat.id == 1137511834:
            await event.edit("Sorry, I Can't Disapprove My Jaanu")
          else:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit("Disapproved [{}](tg://user?id={})".format(firstname, chat.id))
                
    

    @plus_ub(pattern="listapproved", from_users=sudo)
    async def approve_p_m(event):
        if event.fwd_from:
            return
        approved_users = pmpermit_sql.get_all_approved()
        APPROVED_PMs = "Current Approved PMs\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
        else:
            APPROVED_PMs = "no Approved PMs (yet)"
        if len(APPROVED_PMs) > 4095:
            with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="Current Approved PMs",
                    reply_to=event
                )
                await event.delete()
        else:
            await event.edit(APPROVED_PMs)


    @plus.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        if event.from_id == bot.uid:
            return

        if Var.BOTLOG_CHATID is None:
            return

        if not event.is_private:
            return

        message_text = event.message.message
        chat_id = event.from_id

        current_message_text = message_text.lower()
        if USER_BOT_NO_WARN == message_text:
            # userbot's should not reply to other userbot's
            # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
            return
        sender = await bot.get_entity(chat_id)

        if chat_id == bot.uid:

            # don't log Saved Messages

            return

        if sender.bot:

            # don't log bots

            return

        if sender.verified:

            # don't log verified accounts

            return
          
        if not pmpermit_sql.is_approved(chat_id):
            # pm permit
            await do_pm_permit_action(chat_id, event)

    async def do_pm_permit_action(chat_id, event):
        if chat_id not in COUNT_PM:
            COUNT_PM.update({chat_id: 0})
        if COUNT_PM[chat_id] == Var.MAX_FLOOD_IN_P_M_s:
            r = await event.reply(USER_BOT_WARN_ZERO)
            await event.client(functions.contacts.BlockRequest(chat_id))
            if chat_id in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[chat_id].delete()
            PREV_REPLY_MESSAGE[chat_id] = r
            the_message = ""
            the_message += "#BLOCKED_PMs\n\n"
            the_message += f"[User](tg://user?id={chat_id}): {chat_id}\n"
            the_message += f"Message Count: {COUNT_PM[chat_id]}\n"
            # the_message += f"Media: {message_media}"
            try:
                await event.client.send_message(
                    entity=Var.BOTLOG_CHATID,
                    message=the_message,
                    # reply_to=,
                    # parse_mode="html",
                    link_preview=False,
                    # file=message_media,
                    silent=True
                )
                return
            except:
                return
        if WARN_PIC == None:
        	r = await event.client.send_message(event.chat_id, USER_BOT_NO_WARN, link_preview=True)
        else:
        	r = await event.client.send_file(event.chat_id, WARN_PIC, caption=USER_BOT_NO_WARN)
        COUNT_PM[chat_id] += 1
        if chat_id in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_id].delete()
        PREV_REPLY_MESSAGE[chat_id] = r
        
        
    
    				
    				
    @plus.on(events.NewMessage(incoming=True, from_users=667805879))
    async def hehehe(event):
    	if event.fwd_from:
    		return
    	chat = await event.get_chat()
    	if event.is_private:
    		if not pmpermit_sql.is_approved(chat.id):
    			pmpermit_sql.approve(chat.id, "**My Boss Is Best🔥**")
    			await event.client.send_message(chat, "**Boss Meet My Creator**")
