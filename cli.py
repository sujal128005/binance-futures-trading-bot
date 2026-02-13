import click
from bot.client import get_binance_client
from bot.orders import place_futures_order
from bot.logger import setup_logging

setup_logging()

@click.command()
@click.option('--symbol', required=True, help='e.g. BTCUSDT')
@click.option('--side', type=click.Choice(['BUY', 'SELL']), required=True)
@click.option('--type', 'order_type', type=click.Choice(['MARKET', 'LIMIT']), required=True)
@click.option('--qty', type=float, required=True)
@click.option('--price', type=float, help='Required for LIMIT orders')
def main(symbol, side, order_type, qty, price):
    if order_type == 'LIMIT' and not price:
        click.echo("Error: Price is required for LIMIT orders.")
        return

    client = get_binance_client()
    
    try:
        res = place_futures_order(client, symbol, side, order_type, qty, price)
        click.secho(f"\n✅ Order Placed Successfully!", fg='green', bold=True)
        click.echo(f"ID: {res.get('orderId')} | Status: {res.get('status')}")
        click.echo(f"Avg Price: {res.get('avgPrice', 'N/A')} | Qty: {res.get('executedQty')}")
    except Exception as e:
        click.secho(f"\n❌ Order Failed: {e}", fg='red')

if __name__ == "__main__":
    main()
