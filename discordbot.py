import discord
import praw
import random
import datetime

#set global variables.
now = datetime.datetime.now()
TOKEN = "https://discord.com/developers/applications"
client = discord.Client()
last_update = """Added the submission.title above the 
submission.url when posted on discord."""

# Login to the reddit account
# This will be changed to OAUTH in the future for better security.
reddit = praw.Reddit(client_id="zojaJq_BJzDZzA",
                     client_secret="ltSFEY3CiJ7PKMcIttnrJTCplzM",
                     password="N#1vRhNTLCqa%WevfPGn",
                     user_agent="testscript by /u/fakebot3",
                     username="ThaBestServer_Bot")
# Because fuck typing "print('-'*50)" over and over again.
def dash():
	print('-'*50)

#take <subreddit> from "from_sub" and dump a random matching title and image from it.
def sub_random(from_sub):
	sub = reddit.subreddit(from_sub).hot(limit=100)
	listme = []	
	for submission in sub:
		if submission.stickied is False:
			listme.append(submission)

	subid = random.choice(listme)
	ransub = reddit.submission(id=subid)
	if ransub.over_18 is True:
		return('NSFW | {}\n{}'.format(ransub.title,ransub.url))
	elif ransub.is_self is True:
		return('/r/{}\n\n{}'.format(submission.subreddit,submission.selftext))
	else:
		return('{}\n{}'.format(ransub.title,ransub.url))
@client.event
#Initial print of logging information.
async def on_ready():
	print('\n')
	dash()
	print('Logged in as "{}"'.format(client.user.name))
	print('time: '+str(now))
	print(last_update)
	dash()

@client.event
async def on_message(message):
	#Don't want to have the bot respond to itself.
	if message.author == client.user:
		return
	if message.content.startswith("!!"):
		NSFW = ("This post is NSFW and this is not and NSFW Channel.")
		msgstart = sub_random(message.content[2:])
		if msgstart.startswith('NSFW | ') and message.channel.nsfw is False:
			await message.channel.send(NSFW)
			#App server logging data
			print('Time: {}\nServer: {}\nChannel: {}\nAuthor: {}\nMessage: {}\nNSFW: {}\nReturn: {}'.format(now,
											message.guild,
											message.channel,
											message.author,
											message.content,
											msgstart))
		else:
			await message.channel.send(msgstart)
			#App server logging data
			print('Time: {}\nServer: {}\nChannel: {}\nAuthor: {}\nMessage: {}\nReturn: {}'.format(now,
											message.guild,
											message.channel,
											message.author,
											message.content,
											msgstart))
		dash()
	if message.guild.id == 254050713141903361 and message.author.id == 160917036325797888:
		await message.add_reaction(r':Patrick:257719535187001347')

client.run(TOKEN)
