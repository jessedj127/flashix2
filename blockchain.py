# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# ███╗   ███╗███╗   ███╗██████╗ ██████╗ ███████╗ █████╗     ██████╗ ██████╗ ███╗   ███╗
# ████╗ ████║████╗ ████║██╔══██╗██╔══██╗╚══███╔╝██╔══██╗   ██╔════╝██╔═══██╗████╗ ████║
# ██╔████╔██║██╔████╔██║██║  ██║██████╔╝  ███╔╝ ███████║   ██║     ██║   ██║██╔████╔██║
# ██║╚██╔╝██║██║╚██╔╝██║██║  ██║██╔══██╗ ███╔╝  ██╔══██║   ██║     ██║   ██║██║╚██╔╝██║
# ██║ ╚═╝ ██║██║ ╚═╝ ██║██████╔╝██║  ██║███████╗██║  ██║██╗╚██████╗╚██████╔╝██║ ╚═╝ ██║
# ╚═╝     ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' #
# Programmer Mmdrza                                                                   #
# Web Mmdrza.Com                                                                      #
# Email X4@Mmdrza.Com                                                                 #
# GitHub.Com/PyMmdrza                                                                 #
# Dev.to/Mmdrza                                                                       #
# PythonWithMmdrza.Medium.Com                                                         #
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' #


import time

from Tools.scripts.generate_opcode_h import footer
from rich.progress import track, Progress, SpinnerColumn, BarColumn, TextColumn
import requests
from lxml import html
from rich import box
from rich.console import Console
from rich.table import Table
import rich
count = 1
while True:
    urlblock = 'https://www.blockchain.com/btc/unconfirmed-transactions'
    respone_block = requests.get(urlblock)
    byte_string_block = respone_block.content
    source_code_block = html.fromstring(byte_string_block)
    xpatchblock_txid = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]'
    xpatchblock_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[2]/div[3]/div[2]/span'
    xpatchblock_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[2]/div[4]/div[2]/span'
    xpatchblock3_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[4]/div[1]/div[2]'
    xpatchblock3_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[4]/div[3]/div[2]/span'
    xpatchblock3_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[4]/div[4]/div[2]/span'
    xpatchblock4_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[5]/div[1]/div[2]'
    xpatchblock4_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[5]/div[3]/div[2]'
    xpatchblock4_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[5]/div[4]/div[2]'
    xpatchblock6_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[6]/div[1]/div[2]'
    xpatchblock6_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[6]/div[3]/div[2]/span'
    xpatchblock6_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[6]/div[4]/div[2]/span'
    xpatchblock7_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[7]/div[1]/div[2]'
    xpatchblock7_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[7]/div[3]/div[2]/span'
    xpatchblock7_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[7]/div[4]/div[2]/span'
    xpatchblock8_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[8]/div[1]/div[2]'
    xpatchblock8_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[8]/div[3]/div[2]/span'
    xpatchblock8_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[8]/div[4]/div[2]/span'
    xpatchblock9_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[9]/div[1]/div[2]'
    xpatchblock9_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[9]/div[3]/div[2]/span'
    xpatchblock9_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[9]/div[4]/div[2]/span'
    xpatchblock10_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[10]/div[1]/div[2]'
    xpatchblock10_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[10]/div[3]/div[2]/span'
    xpatchblock10_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[10]/div[4]/div[2]/span'
    xpatchblock11_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[11]/div[1]/div[2]'
    xpatchblock11_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[11]/div[3]/div[2]/span'
    xpatchblock11_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[11]/div[4]/div[2]/span'
    xpatchblock12_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[12]/div[1]/div[2]'
    xpatchblock12_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[12]/div[3]/div[2]/span'
    xpatchblock12_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[12]/div[4]/div[2]/span'
    xpatchblock13_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[13]/div[1]/div[2]'
    xpatchblock13_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[13]/div[3]/div[2]/span'
    xpatchblock13_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[13]/div[4]/div[2]/span'
    xpatchblock14_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[14]/div[1]/div[2]'
    xpatchblock14_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[14]/div[3]/div[2]/span'
    xpatchblock14_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[14]/div[4]/div[2]/span'
    xpatchblock15_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[15]/div[1]/div[2]'
    xpatchblock15_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[15]/div[3]/div[2]/span'
    xpatchblock15_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[15]/div[4]/div[2]/span'
    xpatchblock16_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[16]/div[1]/div[2]'
    xpatchblock16_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[16]/div[3]/div[2]/span'
    xpatchblock16_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[16]/div[4]/div[2]/span'
    xpatchblock17_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[17]/div[1]/div[2]'
    xpatchblock17_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[17]/div[3]/div[2]/span'
    xpatchblock17_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[17]/div[4]/div[2]/span'
    xpatchblock18_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[18]/div[1]/div[2]'
    xpatchblock18_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[18]/div[3]/div[2]/span'
    xpatchblock18_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[18]/div[4]/div[2]/span'
    xpatchblock19_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[19]/div[1]/div[2]'
    xpatchblock19_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[19]/div[3]/div[2]/span'
    xpatchblock19_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[19]/div[4]/div[2]/span'
    xpatchblock20_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[20]/div[1]/div[2]'
    xpatchblock20_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[20]/div[3]/div[2]/span'
    xpatchblock20_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[20]/div[4]/div[2]/span'
    # =========================================[MMDRZA.COM]=============================================
    blocktreetxid = source_code_block.xpath(xpatchblock_txid)
    blocktree_btc = source_code_block.xpath(xpatchblock_btc)
    blocktree_usd = source_code_block.xpath(xpatchblock_usd)
    blocktree3_hex = source_code_block.xpath(xpatchblock3_hex)
    blocktree4_hex = source_code_block.xpath(xpatchblock4_hex)
    blocktree3_btc = source_code_block.xpath(xpatchblock3_btc)
    blocktree4_btc = source_code_block.xpath(xpatchblock4_btc)
    blocktree3_usd = source_code_block.xpath(xpatchblock3_usd)
    blocktree4_usd = source_code_block.xpath(xpatchblock4_usd)
    blocktree_6_hex = source_code_block.xpath(xpatchblock6_hex)
    blocktree_6_btc = source_code_block.xpath(xpatchblock6_btc)
    blocktree_6_usd = source_code_block.xpath(xpatchblock6_usd)
    blocktree_7_hex = source_code_block.xpath(xpatchblock7_hex)
    blocktree_7_btc = source_code_block.xpath(xpatchblock7_btc)
    blocktree_7_usd = source_code_block.xpath(xpatchblock7_usd)
    blocktree_8_hex = source_code_block.xpath(xpatchblock8_hex)
    blocktree_8_btc = source_code_block.xpath(xpatchblock8_btc)
    blocktree_8_usd = source_code_block.xpath(xpatchblock8_usd)
    blocktree_9_hex = source_code_block.xpath(xpatchblock9_hex)
    blocktree_9_btc = source_code_block.xpath(xpatchblock9_btc)
    blocktree_9_usd = source_code_block.xpath(xpatchblock9_usd)
    blocktree_10_hex = source_code_block.xpath(xpatchblock10_hex)
    blocktree_10_btc = source_code_block.xpath(xpatchblock10_btc)
    blocktree_10_usd = source_code_block.xpath(xpatchblock10_usd)
    blocktree_11_hex = source_code_block.xpath(xpatchblock11_hex)
    blocktree_11_btc = source_code_block.xpath(xpatchblock11_btc)
    blocktree_11_usd = source_code_block.xpath(xpatchblock11_usd)
    blocktree_12_hex = source_code_block.xpath(xpatchblock12_hex)
    blocktree_12_btc = source_code_block.xpath(xpatchblock12_btc)
    blocktree_12_usd = source_code_block.xpath(xpatchblock12_usd)
    blocktree_13_hex = source_code_block.xpath(xpatchblock13_hex)
    blocktree_13_btc = source_code_block.xpath(xpatchblock13_btc)
    blocktree_13_usd = source_code_block.xpath(xpatchblock13_usd)
    blocktree_14_hex = source_code_block.xpath(xpatchblock14_hex)
    blocktree_14_btc = source_code_block.xpath(xpatchblock14_btc)
    blocktree_14_usd = source_code_block.xpath(xpatchblock14_usd)
    blocktree_15_hex = source_code_block.xpath(xpatchblock15_hex)
    blocktree_15_btc = source_code_block.xpath(xpatchblock15_btc)
    blocktree_15_usd = source_code_block.xpath(xpatchblock15_usd)
    blocktree_16_hex = source_code_block.xpath(xpatchblock16_hex)
    blocktree_16_btc = source_code_block.xpath(xpatchblock16_btc)
    blocktree_16_usd = source_code_block.xpath(xpatchblock16_usd)
    blocktree_17_hex = source_code_block.xpath(xpatchblock17_hex)
    blocktree_17_btc = source_code_block.xpath(xpatchblock17_btc)
    blocktree_17_usd = source_code_block.xpath(xpatchblock17_usd)
    blocktree_18_hex = source_code_block.xpath(xpatchblock18_hex)
    blocktree_18_btc = source_code_block.xpath(xpatchblock18_btc)
    blocktree_18_usd = source_code_block.xpath(xpatchblock18_usd)
    blocktree_19_hex = source_code_block.xpath(xpatchblock19_hex)
    blocktree_19_btc = source_code_block.xpath(xpatchblock19_btc)
    blocktree_19_usd = source_code_block.xpath(xpatchblock19_usd)
    blocktree_20_hex = source_code_block.xpath(xpatchblock20_hex)
    blocktree_20_btc = source_code_block.xpath(xpatchblock20_btc)
    blocktree_20_usd = source_code_block.xpath(xpatchblock20_usd)
    # =========================================[MMDRZA.COM]=============================================
    block3btc = str(blocktree3_btc[0].text_content())
    block4hex = str(blocktree4_hex[0].text_content())
    block4btc = str(blocktree4_btc[0].text_content())
    block3usd = str(blocktree3_usd[0].text_content())
    block4usd = str(blocktree4_usd[0].text_content())
    block3hex = str(blocktree3_hex[0].text_content())
    blocktxid = str(blocktreetxid[0].text_content())
    blockbtc = str(blocktree_btc[0].text_content())
    blockusd = str(blocktree_usd[0].text_content())
    chblock1btc = str(blockbtc)[0]
    chblock2btc = str(block3btc)[0]
    chblock3btc = str(block4btc)[0]
    blockhex_6 = str(blocktree_6_hex[0].text_content())
    blockhex_7 = str(blocktree_7_hex[0].text_content())
    blockhex_8 = str(blocktree_8_hex[0].text_content())
    blockhex_9 = str(blocktree_9_hex[0].text_content())
    blockhex_10 = str(blocktree_10_hex[0].text_content())
    blockhex_11 = str(blocktree_11_hex[0].text_content())
    blockhex_12 = str(blocktree_12_hex[0].text_content())
    blockhex_13 = str(blocktree_13_hex[0].text_content())
    blockhex_14 = str(blocktree_14_hex[0].text_content())
    blockhex_15 = str(blocktree_15_hex[0].text_content())
    blockhex_16 = str(blocktree_16_hex[0].text_content())
    blockhex_17 = str(blocktree_17_hex[0].text_content())
    blockhex_18 = str(blocktree_18_hex[0].text_content())
    blockhex_19 = str(blocktree_19_hex[0].text_content())
    blockhex_20 = str(blocktree_20_hex[0].text_content())
    blockbtc_6 = str(blocktree_6_btc[0].text_content())
    blockbtc_7 = str(blocktree_7_btc[0].text_content())
    blockbtc_8 = str(blocktree_8_btc[0].text_content())
    blockbtc_9 = str(blocktree_9_btc[0].text_content())
    blockbtc_10 = str(blocktree_10_btc[0].text_content())
    blockbtc_11 = str(blocktree_11_btc[0].text_content())
    blockbtc_12 = str(blocktree_12_btc[0].text_content())
    blockbtc_13 = str(blocktree_13_btc[0].text_content())
    blockbtc_14 = str(blocktree_14_btc[0].text_content())
    blockbtc_15 = str(blocktree_15_btc[0].text_content())
    blockbtc_16 = str(blocktree_16_btc[0].text_content())
    blockbtc_17 = str(blocktree_17_btc[0].text_content())
    blockbtc_18 = str(blocktree_18_btc[0].text_content())
    blockbtc_19 = str(blocktree_19_btc[0].text_content())
    blockbtc_20 = str(blocktree_20_btc[0].text_content())
    blockusd_6 = str(blocktree_6_usd[0].text_content())
    blockusd_7 = str(blocktree_7_usd[0].text_content())
    blockusd_8 = str(blocktree_8_usd[0].text_content())
    blockusd_9 = str(blocktree_9_usd[0].text_content())
    blockusd_10 = str(blocktree_10_usd[0].text_content())
    blockusd_11 = str(blocktree_11_usd[0].text_content())
    blockusd_12 = str(blocktree_12_usd[0].text_content())
    blockusd_13 = str(blocktree_13_usd[0].text_content())
    blockusd_14 = str(blocktree_14_usd[0].text_content())
    blockusd_15 = str(blocktree_15_usd[0].text_content())
    blockusd_16 = str(blocktree_16_usd[0].text_content())
    blockusd_17 = str(blocktree_17_usd[0].text_content())
    blockusd_18 = str(blocktree_18_usd[0].text_content())
    blockusd_19 = str(blocktree_19_usd[0].text_content())
    blockusd_20 = str(blocktree_20_usd[0].text_content())
    # =========================================[MMDRZA.COM]=============================================
    row_styles = ["on grey15", "on grey11", "on grey15", "on grey11"]  # T his is a bit messy...?

    table = Table(title_style="italic gold1", header_style="italic", title="\n\n\nBitcoin Transaction Reporter V3\n------- M M D R Z A . C o M -------",
                  border_style="green",
                  box=box.ROUNDED, show_lines=False, row_styles=row_styles, show_edge=True)

    table.add_column("TXID",justify="center", style="bold", no_wrap=True)
    table.add_column("BTC", style="green", no_wrap=True)
    table.add_column("USD", style="gold1", no_wrap=True)
    table.add_row(str(blocktxid),str(blockbtc),str(blockusd))
    table.add_row(str(block3hex), str(block3btc), str(block3usd))
    table.add_row(str(block4hex), str(block4btc), str(block4usd))
    table.add_row(str(blockhex_6), str(blockbtc_6), str(blockusd_6))
    table.add_row(str(blockhex_7), str(blockbtc_7), str(blockusd_7))
    table.add_row(str(blockhex_8), str(blockbtc_8), str(blockusd_8))
    table.add_row(str(blockhex_9), str(blockbtc_9), str(blockusd_9))
    table.add_row(str(blockhex_10), str(blockbtc_10), str(blockusd_10))
    table.add_row(str(blockhex_11), str(blockbtc_11), str(blockusd_11))
    table.add_row(str(blockhex_12), str(blockbtc_12), str(blockusd_12))
    table.add_row(str(blockhex_13), str(blockbtc_13), str(blockusd_13))
    table.add_row(str(blockhex_14), str(blockbtc_14), str(blockusd_14))
    table.add_row(str(blockhex_15), str(blockbtc_15), str(blockusd_15))
    table.add_row(str(blockhex_16), str(blockbtc_16), str(blockusd_16))
    table.add_row(str(blockhex_17), str(blockbtc_17), str(blockusd_17))
    table.add_row(str(blockhex_18), str(blockbtc_18), str(blockusd_18))
    table.add_row(str(blockhex_19), str(blockbtc_19), str(blockusd_19))
    table.add_row(str(blockhex_20), str(blockbtc_20), str(blockusd_20))


    def process_data():
        time.sleep(0.1)


    for _ in track(range(90), style="gold1 blink2", description='[gold1 blink2]Send Requests\n'):
        process_data()

    console = Console()
    console.print(table)
  # ============================
    continue


# ================================================
# DONATE (BTC) : 16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8
# Website : Mmdrza.Com
# Email : X4@mmdrza.Com
# Dev.to/Mmdrza
# Github.com/Pymmdrza
# ================================================