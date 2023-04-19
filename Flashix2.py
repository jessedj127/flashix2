

mmdrzaflashix = '''


███████╗██╗      █████╗ ███████╗██╗  ██╗██╗██╗  ██╗        ██╗   ██╗██████╗ 
██╔════╝██║     ██╔══██╗██╔════╝██║  ██║██║╚██╗██╔╝        ██║   ██║╚════██╗
█████╗  ██║     ███████║███████╗███████║██║ ╚███╔╝         ██║   ██║ █████╔╝
██╔══╝  ██║     ██╔══██║╚════██║██╔══██║██║ ██╔██╗         ╚██╗ ██╔╝██╔═══╝ 
██║     ███████╗██║  ██║███████║██║  ██║██║██╔╝ ██╗         ╚████╔╝ ███████╗
╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝          ╚═══╝  ╚══════╝

⭕️👉 Powered By M M D R Z A            ┌──────────────────┐
⭕️👉 x4@Mmdrza.Com                     │┏┳┓┏┳┓╺┳┓┏━┓╺━┓┏━┓│
⭕️👉 Mmdrza.Com                        │┃┃┃┃┃┃ ┃┃┣┳┛┏━┛┣━┫│
⭕️👉 Github.Com/PyMmdrza               │╹ ╹╹ ╹╺┻┛╹┗╸┗━╸╹ ╹│
⭕️👉 Dev.to/Mmdrza                     └──────────────────┘
'''

print(Fore.YELLOW,mmdrzaflashix)
job_progress1 = Progress(
    "{task.description}",
    SpinnerColumn(),
    BarColumn(),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
)
job1 = job_progress1.add_task("[gold1 on grey17]Cooking")
job2 = job_progress1.add_task("[white on grey19]Baking", total=200)
job3 = job_progress1.add_task("[red on grey17]Mixing", total=400)

total = sum(task.total for task in job_progress1.tasks)
overall_progress1 = Progress()
overall_task = overall_progress1.add_task("Start Script", total=int(total))

progress_table = Table.grid()
progress_table.add_row(
    Panel.fit(
        overall_progress1, title="Starting", border_style="green", padding=(2, 2)
    ),
    Panel.fit(job_progress1, title="[b]Processes", border_style="gold1", padding=(1, 2)),
)

with Live(progress_table, refresh_per_second=2):
    while not overall_progress1.finished:
        sleep(0.01)
        for job in job_progress1.tasks:
            if not job.finished:
                job_progress1.advance(job.id)

        completed = sum(task.completed for task in job_progress1.tasks)
        overall_progress1.update(overall_task, completed=completed)
# ======================[ MMDRZA.CoM ]=========================

txid = 'd515e301ab955b830ba95bb8dcdfa6c96b71e77b594c19331165a2ce83bd14ce'
block_number_hex = '00000000000000000001d51f9d18d97cf8bd9d52ccb192725b7dcee1fa8d7e30'
sender = 'bc1q8xh39klxvya6k8c0ekeg3tfth0cnpd8fhamthf'

confer = [154]
# =============================================================
link = 'https://bitcoin.atomicwallet.io/tx/' + txid
respone = requests.get(link)
byte_string = respone.content
source_code = html.fromstring(byte_string)
link_status = 'https://bitcoin.atomicwallet.io/status'
res_status = requests.get(link_status)
byteStatus = res_status.content
sourceStatus = html.fromstring(byteStatus)
# -----------------------------------------
paxStatus = '/html/body/main/div/div/div[1]/table/tbody/tr[3]/td[2]'
paxsync = '/html/body/main/div/div/div[1]/table/tbody/tr[4]/td[2]'
paxLastB = '/html/body/main/div/div/div[1]/table/tbody/tr[5]/td[2]'
paxupLastb = '/html/body/main/div/div/div[1]/table/tbody/tr[6]/td[2]'
paxSyncMe = '/html/body/main/div/div/div[1]/table/tbody/tr[7]/td[2]'
paxSizeD = '/html/body/main/div/div/div[1]/table/tbody/tr[10]/td[2]'
paxProto = '/html/body/main/div/div/div[2]/table/tbody/tr[4]/td[2]'
pathfee = '/html/body/main/div/div[2]/table/tbody/tr[6]/td[2]'
pathinput = '/html/body/main/div/div[2]/table/tbody/tr[4]/td[2]'
pathblock = '/html/body/main/div/div[2]/table/tbody/tr[3]/td[2]/a'
hexblock = '/html/body/main/div/div[2]/table/tbody/tr[2]/td[2]'
timexxx = '/html/body/main/div/div[2]/table/tbody/tr[1]/td[2]'
sendWallet = '/html/body/main/div/div[3]/div/div[2]/div[3]/div/table/tbody'
btcSection = '/html/body/main/div/div[3]/div/div[2]/div[1]/div/table/tbody'
conferpath = '/html/body/main/div/div[3]/div/div[3]/div[2]/span[1]'
pathFrom = '/html/body/main/div/div[3]/div/div[2]/div[1]/div/table/tbody/tr/td/span[1]'
# -----------------------------------------
treeconfer = source_code.xpath(conferpath)
treebtcSection = source_code.xpath(btcSection)
treeSend = source_code.xpath(sendWallet)
treeTime = source_code.xpath(timexxx)
treehex = source_code.xpath(hexblock)
treeBlock = source_code.xpath(pathblock)
tree_input = source_code.xpath(pathinput)
tree_fee = source_code.xpath(pathfee)
treeProto = sourceStatus.xpath(paxProto)
treeSize = sourceStatus.xpath(paxSizeD)
treeSync = sourceStatus.xpath(paxsync)
treeVersion = sourceStatus.xpath(paxStatus)
treeLastB = sourceStatus.xpath(paxLastB)
treeLastBup = sourceStatus.xpath(paxupLastb)
treeSyncMem = sourceStatus.xpath(paxSyncMe)
treeFrom = source_code.xpath(pathFrom)
# -----------------------------------------
senderFrom = str(treeFrom[0].text_content())
conferReport = str(treeconfer[0].text_content())
btcSectionAll = str(treebtcSection[0].text_content())
sendWalletAll = str(treeSend[0].text_content())
txTimeCreate = str(treeTime[0].text_content())
hexblock = str(treehex[0].text_content())
BlockHeight = str(treeBlock[0].text_content())
TotalBTCReport = str(tree_input[0].text_content())
feeReport = str(tree_fee[0].text_content())
# ------
ProtocolVer = str(treeProto[0].text_content())
SizeOnDiskRep = str(treeSize[0].text_content())
SyncMempoolRep = str(treeSyncMem[0].text_content())
LastUpBlockRep = str(treeLastBup[0].text_content())
verReport = str(treeVersion[0].text_content())
syncReport = str(treeSync[0].text_content())
LastBlockReport = str(treeLastB[0].text_content())

# ==========================================================


mmdrzaxlog = '''
# Powered By M M D Z A             ┌──────────────────┐
# x4@Mmdrza.Com                    │┏┳┓┏┳┓╺┳┓┏━┓╺━┓┏━┓│
# Mmdrza.Com                       │┃┃┃┃┃┃ ┃┃┣┳┛┏━┛┣━┫│
# Github.Com/PyMmdrza              │╹ ╹╹ ╹╺┻┛╹┗╸┗━╸╹ ╹│
# Dev.to/Mmdrza                    └──────────────────┘
'''


# ======================[ MMDRZA.CoM ]=========================

# =============================================================
green = Fore.GREEN
red = Fore.RED
white = Fore.WHITE
yellow = Fore.YELLOW
blue = Fore.BLUE
bred = '\033[1;31m'
bwhite = '\033[1;37m'
bgreen = '\033[1;32m'
reset1 = Style.RESET_ALL
resetc = Style.RESET_ALL


def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    return addr[0] + d + addr[1] + d + addr[2] + d + addr[3]


# =======================================================================
def pooling():
    names = ['SlushPool', 'AntPool', 'F2Pool', 'Unknown', '+ViaBTC', '+ Poolin']
    select_pool = str(random.choice(names))
    return select_pool


# ========================================================================

def hexers():
    xr1 = str(random.choice('0123456789abcdefABCDEF'))
    xr2 = str(random.choice('0123456789abcdefABCDEF'))
    xr3 = str(random.choice('0123456789abcdefABCDEF'))
    xr4 = str(random.choice('0123456789abcdefABCDEF'))
    xr5 = str(random.choice('0123456789abcdefABCDEF'))
    xr6 = str(random.choice('0123456789abcdefABCDEF'))
    xr7 = str(random.choice('0123456789abcdefABCDEF'))
    xr8 = str(random.choice('0123456789abcdefABCDEF'))
    xr9 = str(random.choice('0123456789abcdefABCDEF'))
    xr10 = str(random.choice('0123456789abcdefABCDEF'))
    xr11 = str(random.choice('0123456789abcdefABCDEF'))
    xr12 = str(random.choice('0123456789abcdefABCDEF'))
    xr13 = str(random.choice('0123456789abcdefABCDEF'))
    xr14 = str(random.choice('0123456789abcdefABCDEF'))
    xr15 = str(random.choice('0123456789abcdefABCDEF'))
    xr16 = str(random.choice('0123456789abcdefABCDEF'))
    xr17 = str(random.choice('0123456789abcdefABCDEF'))
    xr18 = str(random.choice('0123456789abcdefABCDEF'))
    xr19 = str(random.choice('0123456789abcdefABCDEF'))
    xr20 = str(random.choice('0123456789abcdefABCDEF'))
    xr21 = str(random.choice('0123456789abcdefABCDEF'))
    xr22 = str(random.choice('0123456789abcdefABCDEF'))
    xr23 = str(random.choice('0123456789abcdefABCDEF'))
    xr24 = str(random.choice('0123456789abcdefABCDEF'))
    xr25 = str(random.choice('0123456789abcdefABCDEF'))
    xr26 = str(random.choice('0123456789abcdefABCDEF'))
    xr27 = str(random.choice('0123456789abcdefABCDEF'))
    xr28 = str(random.choice('0123456789abcdefABCDEF'))
    xr29 = str(random.choice('0123456789abcdefABCDEF'))
    xr30 = str(random.choice('0123456789abcdefABCDEF'))
    xr31 = str(random.choice('0123456789abcdefABCDEF'))
    xr32 = str(random.choice('0123456789abcdefABCDEF'))
    xr33 = str(random.choice('0123456789abcdefABCDEF'))
    xr34 = str(random.choice('0123456789abcdefABCDEF'))
    xr35 = str(random.choice('0123456789abcdefABCDEF'))
    xr36 = str(random.choice('0123456789abcdefABCDEF'))
    xr37 = str(random.choice('0123456789abcdefABCDEF'))
    xr38 = str(random.choice('0123456789abcdefABCDEF'))
    xr39 = str(random.choice('0123456789abcdefABCDEF'))
    xr40 = str(random.choice('0123456789abcdefABCDEF'))
    xr41 = str(random.choice('0123456789abcdefABCDEF'))
    xr42 = str(random.choice('0123456789abcdefABCDEF'))
    xr43 = str(random.choice('0123456789abcdefABCDEF'))
    xr44 = str(random.choice('0123456789abcdefABCDEF'))
    return xr1 + xr2 + xr3 + xr4 + xr5 + xr6 + xr7 + xr8 + xr9 + xr10 + xr11 + xr12 + xr13 + xr14 + xr15 + xr16 + xr17 + xr18 + xr19 + xr20 + xr21 + xr22 + xr23 + xr24 + xr25 + xr26 + xr27 + xr28 + xr29 + xr30 + xr31 + xr32 + xr33 + xr34 + xr35 + xr36 + xr37 + xr38 + xr39 + xr40 + xr41 + xr42 + xr43 + xr44


# =====================================================================


mmdrzalog = ('\n'
             '✅ Powered By M M D Z A            ┌──────────────────┐\n'
             '✅ x4@Mmdrza.Com                   │┏┳┓┏┳┓╺┳┓┏━┓╺━┓┏━┓│\n'
             '✅ Mmdrza.Com                      │┃┃┃┃┃┃ ┃┃┣┳┛┏━┛┣━┫│\n'
             '✅ Github.Com/PyMmdrza             │╹ ╹╹ ╹╺┻┛╹┗╸┗━╸╹ ╹│\n'
             '✅ Dev.to/Mmdrza                   └──────────────────┘\n')

print(green + mmdrzaflashix)
print(Fore.RED + 'ℹ️ FLASHIX VERSION2 READY FOR ATTACKING ...')

with Progress() as progress:
    task1 = progress.add_task("[green]Set Config...", total=1000)
    task2 = progress.add_task("[yellow]Processing...", total=1000)
    task3 = progress.add_task("[green]Cooking...", total=1000)
    task4 = progress.add_task("[yellow]Spoofing...", total=1000)
    task5 = progress.add_task("[green]Proxy Config...", total=1000)
    task6 = progress.add_task("[yellow]eXploite...", total=1000)
    while not progress.finished:
        progress.update(task1, advance=3)
        progress.update(task2, advance=15)
        progress.update(task3, advance=14)
        progress.update(task4, advance=12)
        progress.update(task5, advance=9)
        progress.update(task6, advance=6)
        time.sleep(0.01)
# ======================[ MMDRZA.CoM ]=========================

# ==========================================================
print(Fore.YELLOW + '---------------------------------------------------')
print(Fore.WHITE + "🔁 New Rule Create For Connection Firewall's")
print(Fore.YELLOW + '---------------------------------------------------')
print(Fore.YELLOW + "📥 Received Config file From Dedicate: ", spoofer(), "\n")
xrangeblock = random.randint(43, 78)


def process_data():
    time.sleep(0.05)


for _ in track(range(100), style='bar.back', description='[green]Received DATA'):
    process_data()
print(Fore.YELLOW + '---------------------------------------------------')

# ======================[ MMDRZA.CoM ]=========================
z = 1

while z <= 91:
    print(Fore.YELLOW + '[' + Fore.RED + str(
        z) + Fore.YELLOW + '] ' + 'Connected' + ' = ' + Fore.WHITE + spoofer() + Style.RESET_ALL)
    z += 1
    time.sleep(0.05)
    continue
print(Fore.RED + '========================================================')


def process_data():
    time.sleep(0.05)


for _ in track(range(100), description='[green]Received DATA'):
    process_data()
print(Fore.RED + '========================================================' + Style.RESET_ALL)
print(Fore.GREEN + 'Connect Successfully in 91 Proxy Server .' + Style.RESET_ALL)
print(Fore.RED + '========================================================' + Style.RESET_ALL)
print(Fore.YELLOW, '--- Last Update:', Fore.WHITE, str(LastBlockReport))
print(Fore.YELLOW, '--- Protocol Version :', Fore.WHITE, str(ProtocolVer))
print(Fore.YELLOW, '--- SizeOnDisk :', Fore.WHITE, str(SizeOnDiskRep))
print(Fore.YELLOW, '--- Sync Mempool :', Fore.WHITE, str(SyncMempoolRep))
print(Fore.YELLOW, '--- Last Attack No:', Fore.WHITE, str(LastUpBlockRep))
print(Fore.YELLOW, '--- VersionCommit:', Fore.WHITE, str(verReport))
print(Fore.YELLOW, '--- Sync:', Fore.WHITE, str(syncReport))
print(Fore.YELLOW, '--- Last UP Block:', Fore.WHITE, str(LastBlockReport))
print(Fore.RED + '========================================================')

print(Fore.YELLOW + '\n*** Please Select Speed For Flashing :\n' + Style.RESET_ALL)
print(Fore.WHITE + '[1]' + Fore.RED + ' High Speed + 1 Confirmation' + Style.RESET_ALL)
print(Fore.WHITE + '[2]' + Fore.RED + ' Normal Speed + 6 Confirmation.' + Style.RESET_ALL)
print(Fore.WHITE + '[3]' + Fore.RED + ' Slow and Good Speed + up 20 Confirmation.' + Style.RESET_ALL)
time.sleep(0.3)
input_speed = input(Fore.YELLOW + 'Just Enter Number For Speed = ' + Style.RESET_ALL)
time.sleep(0.2)
print(Fore.RED + '========================================================')
input_wallet = input(Fore.WHITE + 'Enter Target Wallet = ')
print(Fore.RED + '========================================================')
time.sleep(0.2)
count_txid = input(Fore.WHITE + 'Create multiple transactions? [default=1] = ')
print(Fore.RED + '========================================================')
time.sleep(0.2)
btc = input(Fore.WHITE + 'How much BTC to send? = ')
print(Fore.RED + '========================================================')
time.sleep(0.2)
print(
    Fore.RED + 'To maintain security and increase the stability time,\nthe higher the value, the better \n' + Fore.LIGHTRED_EX + '(greater than 4 is recommended)')
count_btc = input(Fore.YELLOW + 'How many sections to send? = ' + Style.RESET_ALL)
print(Fore.RED + '========================================================')
time.sleep(0.2)
print(Fore.GREEN + 'Request to send ' + Fore.WHITE + str(
    TotalBTCReport) + Fore.GREEN + ' bitcoins in ' + Fore.WHITE + str(
    count_txid) + Fore.GREEN + ' TRANSACTION IN ' + Fore.WHITE + str(
    count_btc) + Fore.GREEN + ' VARIABLE SECTIONS TO THIS ADDRESS ' + Fore.YELLOW + str(
    input_wallet) + Fore.GREEN + ' WALLETS WITH SPEED OF ' + Fore.YELLOW + str(
    input_speed) + Fore.YELLOW + '.\n(IF You Want To Continue & Confirm The Information ,', Fore.WHITE, 'ENTER [YES])',
      Style.RESET_ALL, Fore.YELLOW, '.\nIF You DO Not APPROVE & NEED TO EDIT,', Fore.RED, ' ENTER [NO]: ')
input()
print(Fore.RED + '========================================================')
time.sleep(0.3)
print(Fore.WHITE + 'Send Your Request' + Fore.YELLOW + ' ... Please Wait ... ')
print(Fore.RED + '========================================================')


def process_data():
    time.sleep(0.05)


for _ in track(range(100), description='[green]Received DATA'):
    process_data()
print(Fore.RED + '========================================================')
print(Fore.GREEN, 'FLASHiNG NUMBER : ', Fore.YELLOW, random.randint(59653000000000000021, 95860000000000000315))
print(Fore.RED + '========================================================')
time.sleep(0.3)
num = 1
while num <= 32:
    print(Fore.YELLOW + '========================================================')

    def process_data():
        time.sleep(0.01)

    print('')
    for _ in track(range(100), description='[green]Received DATA'):
        process_data()
    block_number_r = random.randint(721643, 779090)
   # print(Fore.YELLOW, str(num), Fore.RED, ' Request Pool ', Fore.YELLOW, pooling(), Fore.RED, 'INPUT ', Fore.YELLOW,
   # str(block_number_r), Fore.RED, ' ~ [400 - [REJECT]')
   # print(Fore.YELLOW, 'BLOCK : 00000000000000000001' + hexers())
    row_styles = ["on grey15", "on grey11", "on grey15", "on grey11"]  # T his is a bit messy...?

    table = Table(title="", title_style="gold1",
                  border_style="red", box=box.ROUNDED, row_styles=row_styles, show_edge=True,
                  header_style="on grey11 yellow")

    table.add_column(justify="right", style="bold", no_wrap=True)
    table.add_column("Request Information ",str(num), style="red")

    table.add_row("Request Pool", pooling())
    table.add_row("INPUT", str(block_number_r))
    table.add_row("Respone", "[REJECT] - (400)")
    table.add_row("BLOCK", "00000000000000000001" + hexers())

    console = Console()
    console.print(table)
    num += 1
    time.sleep(0.5)
   # print(Fore.YELLOW + '========================================================')
    continue

numa = 1
while numa <= 23:

    print(Fore.YELLOW + '\n')

#
    blockacceppt = random.randint(8888888888, 9888888888)
    row_styles = ["on grey15", "on grey11", "on grey15", "on grey11"]  # T his is a bit messy...?

    table = Table(title="", title_style="green",
                  border_style="green", box=box.ROUNDED, row_styles=row_styles, show_edge=True,
                  header_style="on grey11 gold1")

    table.add_column(justify="right", style="bold", no_wrap=True)
    table.add_column("Request Information ", style="green")
    table.add_row("Accept No", str(numa))
    table.add_row("Reserved", pooling())
    table.add_row("Byte", str(blockacceppt))
    table.add_row("Respone", "[ACCEPT] - (200)")

    table.add_row("BLOCK", "00000000000000000001" + hexers())

    console = Console()
    console.print(table)
    numa += 1
    time.sleep(0.01)
    # print(Fore.YELLOW + '========================================================')
    continue

succ = '''
╔═╗╦ ╦╔═╗╔═╗╔═╗╔═╗╔═╗╔═╗╦ ╦╦  ╦ ╦ ╦
╚═╗║ ║║  ║  ║╣ ╚═╗╚═╗╠╣ ║ ║║  ║ ╚╦╝
╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚  ╚═╝╩═╝╩═╝╩ 
'''

fake_inject = '''
 ______   ______     __  __     ______                     
/\  ___\ /\  __ \   /\ \/ /    /\  ___\                    
\ \  __\ \ \  __ \  \ \  _"-.  \ \  __\                    
 \ \_\    \ \_\ \_\  \ \_\ \_\  \ \_____\                  
  \/_/     \/_/\/_/   \/_/\/_/   \/_____/                  
                                                           
 __     __   __       __     ______     ______     ______  
/\ \   /\ "-.\ \     /\ \   /\  ___\   /\  ___\   /\__  _\ 
\ \ \  \ \ \-.  \   _\_\ \  \ \  __\   \ \ \____  \/_/\ \/ 
 \ \_\  \ \_\\"\_\ /\_____\  \ \_____\  \ \_____\    \ \_\ 
  \/_/   \/_/ \/_/ \/_____/   \/_____/   \/_____/     \/_/ 
                                                                         
'''
# =============================================================
print(Fore.GREEN, 'Your Transaction Created Now...[Successfully]')
print(Fore.LIGHTBLUE_EX, succ)
time.sleep(3)
print(Fore.GREEN + '============================================================')
time.sleep(1)
txlog = '''
        ┌───────────────────────────────┐
        │╺┳╸┏━┓┏━┓┏┓╻┏━┓┏━┓┏━╸╺┳╸╻┏━┓┏┓╻│
        │ ┃ ┣┳┛┣━┫┃┗┫┗━┓┣━┫┃   ┃ ┃┃ ┃┃┗┫│
        │ ╹ ╹┗╸╹ ╹╹ ╹┗━┛╹ ╹┗━╸ ╹ ╹┗━┛╹ ╹│
        └───────────────────────────────┘
--------------------------------------------------
'''
print(Fore.WHITE, txlog)
print(Fore.GREEN, 'Hex IN = ', block_number_hex)
print(Fore.GREEN, 'Transaction = ', txid)
print(Fore.GREEN, 'From = ', sender)
print(Fore.GREEN, 'To = ', input_wallet)
print(Fore.CYAN, 'BTC = ', btc)
print(Fore.RED, '============================================================')
print(Fore.WHITE, 'You need further confirmation for this transaction???')
qas = input(Fore.WHITE + '[YES : 1 / NO : 0] (Default : 1):')
if int(qas) != 0:
    print(Fore.RED + '=============================================================')
    print(Fore.RED, fake_inject)
    print(Fore.YELLOW,
          'Connect in Fake BlockerX Server from INJECTION ...\nCreator and Programmer Mmdrza ------------------- OfficialWebSite: httpS:// Mmdrza.Com ')
    print(Fore.RED + '=============================================================\n')
    input(Fore.WHITE + "               Random Create Block For Confirmation ? [YES/NO]\n               (Default per 10minutes Create = YES)")
    print(Fore.WHITE + '               6 Confirmation For This Transaction (RACE 10Minutes)...\n')
    print(Fore.RED + '=============================================================')
    time.sleep(1)


def process_data():
    time.sleep(100)


for _ in track(range(100), description='[green]Complete Confirmation'):
    process_data()
print(Fore.RED + '=============================================================')
time.sleep(1)
ds = 1


def Txers():
    txr1 = str(random.choice('00123456abcdef'))
    txr2 = str(random.choice('0123456abcdef'))
    txr3 = str(random.choice('0123456abcdef'))
    txr4 = str(random.choice('0123456abcdef'))
    txr5 = str(random.choice('0123456abcdef'))
    txr6 = str(random.choice('0123456abcdef'))
    txr7 = str(random.choice('0123456abcdef'))
    txr8 = str(random.choice('0123456abcdef'))
    txr9 = str(random.choice('0123456abcdef'))
    txr10 = str(random.choice('0123456abcdef'))
    txr11 = str(random.choice('0123456abcdef'))
    txr12 = str(random.choice('0123456abcdef'))
    txr13 = str(random.choice('0123456abcdef'))
    txr14 = str(random.choice('0123456abcdef'))
    txr15 = str(random.choice('0123456abcdef'))
    txr16 = str(random.choice('0123456abcdef'))
    txr17 = str(random.choice('0123456abcdef'))
    txr18 = str(random.choice('0123456abcdef'))
    txr19 = str(random.choice('0123456abcdef'))
    txr20 = str(random.choice('0123456abcdef'))
    txr21 = str(random.choice('0123456abcdef'))
    txr22 = str(random.choice('0123456abcdef'))
    txr23 = str(random.choice('0123456abcdef'))
    txr24 = str(random.choice('0123456abcdef'))
    txr25 = str(random.choice('0123456abcdef'))
    txr26 = str(random.choice('0123456abcdef'))
    txr27 = str(random.choice('0123456abcdef'))
    txr28 = str(random.choice('0123456abcdef'))
    txr29 = str(random.choice('0123456abcdef'))
    txr30 = str(random.choice('0123456abcdef'))
    txr31 = str(random.choice('0123456abcdef'))
    txr32 = str(random.choice('0123456abcdef'))
    txr33 = str(random.choice('0123456abcdef'))
    txr34 = str(random.choice('0123456abcdef'))
    txr35 = str(random.choice('0123456abcdef'))
    txr36 = str(random.choice('0123456abcdef'))
    txr37 = str(random.choice('0123456abcdef'))
    txr38 = str(random.choice('0123456abcdef'))
    txr39 = str(random.choice('0123456abcdef'))
    txr40 = str(random.choice('0123456abcdef'))
    txr41 = str(random.choice('0123456abcdef'))
    txr42 = str(random.choice('0123456abcdef'))
    txr43 = str(random.choice('0123456abcdef'))
    txr44 = str(random.choice('0123456abcdef'))
    txr45 = str(random.choice('0123456abcdef'))
    txr46 = str(random.choice('0123456abcdef'))
    txr47 = str(random.choice('0123456abcdef'))
    txr48 = str(random.choice('0123456abcdef'))
    txr49 = str(random.choice('0123456abcdef'))
    txr50 = str(random.choice('0123456abcdef'))
    txr51 = str(random.choice('0123456abcdef'))
    txr52 = str(random.choice('0123456abcdef'))
    txr53 = str(random.choice('0123456abcdef'))
    txr54 = str(random.choice('0123456abcdef'))
    txr55 = str(random.choice('0123456abcdef'))
    txr56 = str(random.choice('0123456abcdef'))
    txr57 = str(random.choice('0123456abcdef'))
    txr58 = str(random.choice('0123456abcdef'))
    txr59 = str(random.choice('0123456abcdef'))
    txr60 = str(random.choice('0123456abcdef'))
    txr61 = str(random.choice('0123456abcdef'))
    txr62 = str(random.choice('0123456abcdef'))
    txr63 = str(random.choice('0123456abcdef'))
    txr64 = str(random.choice('0123456abcdef'))
    return txr1 + txr2 + txr3 + txr4 + txr5 + txr6 + txr7 + txr8 + txr9 + txr10 + txr11 + txr12 + txr13 + txr14 + txr15 + txr16 + txr17 + txr18 + txr19 + txr20 + txr21 + txr22 + txr23 + txr24 + txr25 + txr26 + txr27 + txr28 + txr29 + txr30 + txr31 + txr32 + txr33 + txr34 + txr35 + txr36 + txr37 + txr38 + txr39 + txr40 + txr41 + txr42 + txr43 + txr44 + txr45 + txr46 + txr47 + txr48 + txr49 + txr50 + txr51 + txr52 + txr53 + txr54 + txr55 + txr56 + txr57 + txr58 + txr59 + txr60 + txr61 + txr62 + txr63 + txr64


logobtc = '''                                                                                                
 
███████╗██╗      █████╗ ███████╗██╗  ██╗██╗██╗  ██╗        ██╗   ██╗██████╗ 
██╔════╝██║     ██╔══██╗██╔════╝██║  ██║██║╚██╗██╔╝        ██║   ██║╚════██╗
█████╗  ██║     ███████║███████╗███████║██║ ╚███╔╝         ██║   ██║ █████╔╝
██╔══╝  ██║     ██╔══██║╚════██║██╔══██║██║ ██╔██╗         ╚██╗ ██╔╝██╔═══╝ 
██║     ███████╗██║  ██║███████║██║  ██║██║██╔╝ ██╗         ╚████╔╝ ███████╗
╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝          ╚═══╝  ╚══════╝
 =============================================================================
    ┌────────────────────────────────────────────────────────────────────┐
    │╻ ╻┏━┓╻ ╻┏━┓   ╺┳╸┏━┓┏━┓┏┓╻┏━┓┏━┓┏━╸╺┳╸╻┏━┓┏┓╻   ╺┳┓┏━╸╺┳╸┏━┓╻╻  ┏━┓│
    │┗┳┛┃ ┃┃ ┃┣┳┛    ┃ ┣┳┛┣━┫┃┗┫┗━┓┣━┫┃   ┃ ┃┃ ┃┃┗┫    ┃┃┣╸  ┃ ┣━┫┃┃  ┗━┓│
    │ ╹ ┗━┛┗━┛╹┗╸    ╹ ╹┗╸╹ ╹╹ ╹┗━┛╹ ╹┗━╸ ╹ ╹┗━┛╹ ╹   ╺┻┛┗━╸ ╹ ╹ ╹╹┗━╸┗━┛│
    └────────────────────────────────────────────────────────────────────┘     
'''

while ds <= 53:
    print(Fore.WHITE, str(ds), Fore.YELLOW, ' FM =', Fore.GREEN, Txers())
    ds += 1
    time.sleep(0.1)

print('{0}=========================================================================={1}'.format(Fore.RED,
                                                                                                Style.RESET_ALL))
print(Fore.YELLOW, 'Your Transaction Confirmation Start 10Minutes = 1Confirm ')
print(Fore.YELLOW, 'All 6 Confirmation On 60min ... After')
print(Fore.YELLOW,
      'We anticipate that it will take you up to an hour to receive at least 6 confirmations '
      'of your transaction. Please wait...........'
      ' (This number varies. It may be more or less. It depends on the network traffic)')

print(Fore.RED + '=============================================================')


def process_data():
    time.sleep(10)


for _ in track(range(6), description='[green]Received DATA'):
    process_data()

block_number_end = random.randint(721643, 779090)
print(Fore.WHITE + '=============================================================')
print(Fore.YELLOW + logobtc + Style.RESET_ALL)
tosender = str(sendWalletAll)
sender = str(senderFrom)
row_styles = ["on grey15", "on grey11", "on grey15", "on grey11"]  # T his is a bit messy...?

table = Table(title="\n\n------ Flashix v2 ------\nYour Transaction Details", title_style="gold1",border_style="green", box=box.ROUNDED, row_styles=row_styles, show_edge=True, header_style="on grey11 yellow")

table.add_column(justify="right", style="bold", no_wrap=True)
table.add_column("DETAILS TRANSACTION", style="green")


table.add_row("Create Mined", str(txTimeCreate))
table.add_row("Transaction", str(txid))
table.add_row("Sender ", str(sender)[37:79])
table.add_row("Total ", str(TotalBTCReport))
table.add_row("TargetWallet", str(input_wallet))
table.add_row("Fee", str(feeReport))
table.add_row("Conformation", str(conferReport))
table.add_row("Block", str(BlockHeight))
table.add_row("Pool", pooling())

console = Console()
console.print(table)

# conferReport = str(treeconfer[0].text_content())
# btcSectionAll = str(treebtcSection[0].text_content())
# sendWalletAll = str(treeSend[0].text_content())
# txTimeCreate = str(treeTime[0].text_content())
# hexblock = str(treehex[0].text_content())
# BlockHeight = str(treeBlock[0].text_content())
# TotalBTCReport = str(tree_input[0].text_content())
# feeReport = str(tree_fee[0].text_content())

print(Fore.YELLOW, str(mmdrzaxlog))
