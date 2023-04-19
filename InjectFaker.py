from rich.console import Console
from rich.table import Table
import random
from rich.console import Console
from rich.table import Table
from rich import box

txTimeCreate = random.randint(896699867,996699867)
txid = random.randint(8966000000000000000000000000000099867,9966900000000000000000000000000009867)
TotalBTCReport = random.randint(8,9967)
feeReport = random.randint(896699867,996699867)
conferReport = random.randint(896699867,996699867)

row_styles = ["on grey15", "on grey11", "on grey15", "on grey11"]  # T his is a bit messy...?

table = Table(title="------ Flashix v2 ------\nYour Transaction Details", title_style="gold1",border_style="green", box=box.ROUNDED, row_styles=row_styles, show_edge=True, header_style="on grey11 yellow")

table.add_column(justify="right", style="bold", no_wrap=True)
table.add_column("DETAILS TRANSACTION", style="green")

table.add_row("Create Mined",str(txTimeCreate))
table.add_row("Transaction", str(txid))
table.add_row("Total Send", str(TotalBTCReport))
table.add_row("Fee", str(feeReport))
table.add_row("Conformation", str(conferReport))


console = Console()
console.print(table)