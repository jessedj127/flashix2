import random
import time
from rich import box
from rich.console import Console
from rich.table import Table
import requests
from colorama import Fore, Style
from lxml import html
from rich.progress import track, Progress

from rich.table import Table

def process_data():
    time.sleep(0.1)


for _ in track(range(6), description='[green]Received DATA'):
    process_data()
def pooling():
    names = ['SlushPool', 'AntPool', 'F2Pool', 'Unknown', '+ViaBTC', '+ Poolin']
    select_pool = str(random.choice(names))
    return select_pool


# ======================[ MMDRZA.CoM ]=========================

txid = str(input('TXID >>>>>>>> '))
txid1 = 'd515e301ab955b830ba95bb8dcdfa6c96b71e77b594c19331165a2ce83bd14ce'
block_number_hex = '00000000000000000001d51f9d18d97cf8bd9d52ccb192725b7dcee1fa8d7e30'
input_wallet = 333
confer = [154]
# =============================================================
urlblock = 'https://www.blockchain.com/btc/unconfirmed-transactions'
respone_block = requests.get(urlblock)
byte_string_block = respone_block.content
source_code_block = html.fromstring(byte_string_block)
xpatchblock_txid = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]'
xpatchblock_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[2]/div[3]'
xpatchblock_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[2]/div[4]/div[2]/span'
blocktreetxid = source_code_block.xpath(xpatchblock_txid)
blocktree_btc = source_code_block.xpath(xpatchblock_btc)
blocktree_usd = source_code_block.xpath(xpatchblock_usd)
blocktxid = str(blocktreetxid[0].text_content())
blockbtc = str(blocktree_btc[0].text_content())
blockusd = str(blocktree_usd[0].text_content())

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

tosender = str(sendWalletAll)
sender = str(senderFrom)

block_number_end = random.randint(721643, 779090)
print(Fore.WHITE + '=============================================================')
row_styles = ["on grey15", "on grey11", "on grey15", "on grey11"]  # T his is a bit messy...?

table = Table(title="\n\n------ Flashix v2 ------\nYour Transaction Details", title_style="gold1", border_style="green",
              box=box.ROUNDED, row_styles=row_styles, show_edge=True, header_style="on grey11 yellow")

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
